import CC100IO as cc
import unittest

class test_cc100(unittest.TestCase):
    def TestDigitalWrite(self):
        for i in range(1, 9):
            for j in range(2):
                cc.digitalWrite(i,j)
            
    def TestDigitalRead(self):
        for i in range(1,9):
            cc.digitalRead(i)
            
    def TestAnalogWrite(self):
        for i in range(1,2):
            for j in range(0,10001,1000):
                cc.analogWrite(i,j)

    def TestAnalogRead(self):
        for i in range(1,2):
            cc.analogRead(i)
        
    def TestDelay(self):
        pass
    
    def TestTempRead(self):
        pass

    def TestSerialReadLine(self):
        pass

    def TestSerialReadBytes(self):
        pass

    def TestSerialWrite(self):
        pass

    def TestReadCalibarationData(self):
        pass

    def TestgetCalibartionData(self):
        pass

    def TestgetCalcCalibrate(self):
        pass

    def TestCalibrateOut(self):
        pass

    def TestReadCalibrationData(self):
        pass

    def TestCalibrateIn(self):
        pass

    def TestCalibrateTemp(self):
        pass

    def TestIsDocker(self):
        pass

