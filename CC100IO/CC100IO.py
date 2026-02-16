# -*- coding: utf-8 -*-

"""
Access onboard I/O of the 751-9301 CC100 controller.

Technical details at https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py
"""

import time
import logging

logger = logging.getLogger(__name__)

def digitalWrite(output, value):
    """Switch the output to the specified value.

    output: Digital output to be switched
    value: Value which the selected output should be set to
    Return True if value is written, False if an error occured
    """
    # Read the current state to calculate the new value in the file
    file = open(DOUT_DATA, "r")
    currentValue = int(file.read())
    file.close()

    # Addition or rather subtraction to the current state to switch the corresponding output
    # Least Significant Bit corresponds to digital output 1, the 4th bit corresponds to output 4
    # A number from 0 to 15 is written to the file
    if output in range(1, 5):
        mask = (1 << (output - 1))
        if value:
            currentValue = currentValue | mask
        else:
            currentValue = currentValue & ~mask
    else:
        logger.warning("Output does not exist")

    # Writes the calculated value for the new configuration to the file on the CC100
    file = open(DOUT_DATA, "w")
    file.write(str(currentValue))
    file.close()

    return True


def analogWrite(output, voltage):
    """Switch the output to the specified voltage.
    
    output: Analog output to be switched
    voltage: Voltage which the selected output should be set to
    """
    if (voltage>0 and voltage <10000):
        voltage = calibrateOut(voltage, output)
    if voltage < 0:
        voltage = 0

    # Activate the analog outputs on the CC100
    file = open(OUT_VOLTAGE1_POWERDOWN, "w")
    file.write("0")
    file.close()

    file = open(OUT_VOLTAGE2_POWERDOWN, "w")
    file.write("0")
    file.close()

    # Write the voltage, taken from the calibration for the corresponding output,
    # for the voltage to the file for the output
    # When turning off, zero is written to the file
    if output == 1:
        file = open(OUT_VOLTAGE1_RAW, "w")
        file.write(str(voltage))
        file.close()

    elif output == 2:
        file=open(OUT_VOLTAGE2_RAW, "w")
        file.write(str(voltage))
        file.close()
        
    return True

def digitalRead(input):
    """Read the specified digital input and return the value as boolean.

    input: Digital input to be read
    """

    # Read the state of the digital inputs on the CC100
    datei = open (DIN, "r")
    value = datei.readline()
    datei.close()

    # Format the current state into an 8-digit binary code
    value = int(value)
    value0B = format(value, "08b")

    # Calculate the position of the bit from the desired input
    inputBit = 8 - input

    # Return the value of the state of the desired input
    # Note: Last index(read from left to right) ist the Least Significant Bit.
    if int(value0B[inputBit]) == 1:
        return True
    else:
        return False

def digitalReadWait(input, value):
    """Read specified input until desired state is reached, then return True.

    input: Digital input to be checked
    value: State to be queried at the input
    """
    value = int(value)

    # Check the input as long as it reaches the given state
    # Then end the loop and return True
    while True:
        if digitalRead(input) == value:
            break
    return True

def analogRead(input):
    """Read analog input and return calibrated value in mV.

    input: Analog input to be read
    """

    # Read the state of the analog input on the CC100
    if input == 1:
        path=IN_VOLTAGE3_RAW
    elif input == 2:
        path=IN_VOLTAGE0_RAW

    file = open(path, "r")
    voltage = int(file.readline())
    file.close()

    return(calibrateIn(voltage, input))

def delay(iTime):
    iTime = iTime/1000
    time.sleep(iTime)

def tempRead(input):
    """Read PT input and return calibrated value in °C.

    input: PT input to be read
    """
    
    if input == "PT1":
        path=IN_VOLTAGE13_RAW
    elif input == "PT2":
        path=IN_VOLTAGE1_RAW
    
    file = open(path, "r")
    voltage = int(file.readline())
    file.close()

    # Calibrate the value and returns it
    return(calibrateTemp(voltage, input))

def serialReadLine():
    """Read incoming message on RS485 Port till eol and return data."""
    data = ""
    with open(SERIAL_PORT) as ser:
        data = ser.readline()
    return data
    

def serialReadBytes(n):
    """Read a specified number of bytes in RS485 port and return data.

    n: number of bytes to read
    """
    data = ""
    with open(SERIAL_PORT, "r") as ser:
        data = ser.read(n)
    return data


def serialWrite(message):
    """Write message to RS485 serial interface and return number of written bytes.

    message: String to write
    """
    written = -1
    with open(SERIAL_PORT, "w") as ser:
        written = ser.write(message)
    return written


# Output calibration from: https://github.com/WAGO/cc100-howtos/blob/main/HowTo_Access_Onboard_IO/accessIO_CC100.py
def readCalibrationData():
    """Read out calibration data from the CC100 and save it in global variable calib_data."""
    global calib_data
    file = open(CALIB_DATA, "r")
    calib_data = file.readlines()[1:]    
    file.close()

def getCalibrationData(value):
    """Return the calibration data for the required row of the table.

    value: the row to read
    """
    return calib_data[value].rstrip().split(' ', 4)

def calcCalibrate(val_uncal, calib):
    """Calculate the value of the voltage for the required output.

    val_uncal: uncalibrated value
    calib: calibration data
    """
    x1=int(calib[0])
    y1=int(calib[1])
    x2=int(calib[2])
    y2=int(calib[3])

    val_cal=(y2-y1)*int(val_uncal-x1)
    val_cal=val_cal/(x2-x1)
    val_cal=val_cal+y1

    return int(val_cal)

def calibrateOut(voltage, output):
    """Calibrate and return voltage to be applied to analog output.
    
    voltage: Voltage to be applied to the output.
    output: Output which should be switched
    """
    
    readCalibrationData()
    # Take a different set of calibration data depending on the output
    if output == 1:
        cal_ao = getCalibrationData(4)
    elif output == 2:
        cal_ao = getCalibrationData(5)
    # Calculate and return the value
    return calcCalibrate(voltage, cal_ao)

def calibrateIn(value, input):
    """Convert value read at analog input to mV and return it.

    value: Value given for the file from the output
    input: Input at which the value was read
    """
    readCalibrationData()
    if input == 1:
        cal_ai = getCalibrationData(2)
    if input == 2:
        cal_ai = getCalibrationData(3)
    #Return the calculated value 
    return calcCalibrate(value, cal_ai)

def calibrateTemp(value, input):
    """Calibrate and return temperature read at PT input in °C.

    value: Value given for the file from the output
    input: Input at which the value was read
    """
    readCalibrationData()
    if input == "PT1":
        cal_Temp = getCalibrationData(0)
    if input == "PT2":
        cal_Temp = getCalibrationData(1)
    #Return the calculated value in °C
    return (calcCalibrate(value, cal_Temp)-1000)/(3.91)

def osIsDocker():
    """Return True if the method is run by CC100Interface-Docker"""
    os_data = open(OS_VERSION, "r")
    lines = os_data.readlines()
    for line in lines:
        if line.strip('\n') == 'NAME="Ubuntu"':
            os_data.close()
            return True
    os_data.close()        
    return False
    
# data paths on CC100
DOUT_DATA = "/sys/kernel/dout_drv/DOUT_DATA"
OUT_VOLTAGE1_POWERDOWN = "/sys/bus/iio/devices/iio:device0/out_voltage1_powerdown"
OUT_VOLTAGE2_POWERDOWN = "/sys/bus/iio/devices/iio:device1/out_voltage2_powerdown"
OUT_VOLTAGE1_RAW = "/sys/bus/iio/devices/iio:device0/out_voltage1_raw"
OUT_VOLTAGE2_RAW = "/sys/bus/iio/devices/iio:device1/out_voltage2_raw"
DIN = "/sys/devices/platform/soc/44009000.spi/spi_master/spi0/spi0.0/din"
IN_VOLTAGE3_RAW = "/sys/bus/iio/devices/iio:device3/in_voltage3_raw"
IN_VOLTAGE0_RAW = "/sys/bus/iio/devices/iio:device3/in_voltage0_raw"
IN_VOLTAGE13_RAW = "/sys/bus/iio/devices/iio:device2/in_voltage13_raw"
IN_VOLTAGE1_RAW = "/sys/bus/iio/devices/iio:device2/in_voltage1_raw"
CALIB_DATA = "/etc/calib"
OS_VERSION = "/etc/os-release"
SERIAL_PORT = "/dev/ttySTM1"
if osIsDocker():
    # data paths on the docker container
    DOUT_DATA = "/home/ea/dout/DOUT_DATA"
    OUT_VOLTAGE1_POWERDOWN = "/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_powerdown"
    OUT_VOLTAGE2_POWERDOWN = "/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_powerdown"
    OUT_VOLTAGE1_RAW = "/home/ea/anout/40017000.dac:dac@1/iio:device0/out_voltage1_raw"
    OUT_VOLTAGE2_RAW = "/home/ea/anout/40017000.dac:dac@2/iio:device1/out_voltage2_raw"
    DIN = "/home/ea/din/din"
    IN_VOLTAGE3_RAW = "/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage3_raw"
    IN_VOLTAGE0_RAW = "/home/ea/anin/48003000.adc:adc@100/iio:device3/in_voltage0_raw"
    IN_VOLTAGE13_RAW = "/sys/bus/iio/devices/iio:device2/in_voltage13_raw"
    IN_VOLTAGE1_RAW = "/sys/bus/iio/devices/iio:device2/in_voltage1_raw"
    CALIB_DATA = "/home/ea/cal/calib"
    OS_VERSION = "/etc/os-release"
