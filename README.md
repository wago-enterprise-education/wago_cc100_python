# WAGO CC100 Python IO Package

Basic python module to control the input and output ports of a WAGO CC100 (751-9301). Module can be used native on WAGO CC100 or in Docker Container running on WAGO CC100.

> [!CAUTION]
> **This repository is a development repository that was created as part of a student project and is not regularly maintained. It is neither a stable version nor an official repository of WAGO GmbH & Co. KG.**

## Contributors

- Maik Rehburg <maik.rehburg@wago.com>
- André Alexander Bell <andre.bell@wago.com>
- Konrad Holsmölle
- Bjarne Zaremba
- Tobias Pape
- Tobias Schäkel
- Mattis Schrade
- Bekim Imrihor
- Nele Stocksmeyer
- Sascha Hahn
- Danny Meihöfer

## Prerequisites

- Firmware Version >= 21(03.09.04)
- Python >= 3.7 on WAGO CC100

## Installation

```bash
pip install cc100io
```

## Example

```python
import cc100io

def armHoch():
    cc100io.digitalWrite(3, True)
    if cc100io.digitalReadWait(4, False):
        cc100io.digitalWrite(3, False)
        return True
```

## Description of functions

- **`digitalWrite (output, value)`**:

  - output: Digital output to be switched (1-4)
  - value: Value which the selected output should be set to (True or False)
  - Function switches the output to the specified value.
  - Function does not check the current value of the output.
  - Function returns True if value is written, returns False if an error occured.

- **`analogWrite (output, voltage)`**:

  - output: Analog output to be switched(1 or 2)
  - voltage: Voltage which the selected output should be set to (0 - 10000 mV)
  - Function switches the output to the specified voltage.
  - Function does not check the current value of the output.
  - Function returns True if value is written, returns False if an error occured.

- **`digitalRead (input)`**:

  - input: Digital input to be read (1-8)
  - Function reads the input.
  - Function does not check the current value of the output.
  - Returns True or False depending on the value.

- **`digitalReadWait (input, value)`**:

  - input: Digital input to be checked (1-8)
  - value: State to be queried at the input
  - Reads the specified input until the desired state is reached, by another Function or external factors and then returns True.
  - Function runs until the state is reached.

- **`analogRead (input)`**:

  - input: Analog input to be read (1 or 2)
  - Function reads the input and returns the calibrated value in mV as an Integer.

- **`delay (iTime)`**:

  - Function makes the programm in a period of time late or slow. (in ms)

- **`tempRead (input)`**:

  - input: PT input to be switched ("PT1" or "PT2")
  - Function reads the input and returns the calibrated value in °C as an Integer.

- **`serialReadLine()`**:

  - Reads incoming message on RS485 Port till eol

- **`serialReadBytes(n)`**:

  - n: number of bytes to read
  - Reads n incoming message on RS485 Port

- **`serialWrite(message)`**:

  - message: String to write
  - Write message to RS485 serial interface
  - returns number of written bytes

## Examples

Examples can be found in directory [*sample-scripts*](/sample_scripts)
