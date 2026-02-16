import unittest

import CC100IO as cc

class TestCC100(unittest.TestCase):
    def test_non_existing_output(self):
        with self.assertLogs(level="WARNING") as cm:
            cc.digitalWrite(5)
        self.assertEqual(cm.output, ["WARNING:CC100IO:Output does not exist"])

    def TestDigitalWrite():
        for i in range(1, 9):
            for j in range(2):
                cc.digitalWrite(i,j)

    def TestDigitalRead():
        for i in range(1,9):
            cc.digitalRead(i)

    def TestAnalogWrite():
        for i in range(1,2):
            for j in range(0,10001,1000):
                cc.analogWrite(i,j)

    def TestAnalogRead():
        for i in range(1,2):
            cc.analogRead(i)
        
    def TestDelay():
        pass
    
    def TestTempRead():
        pass

    def TestSerialReadLine():
        pass

    def TestSerialReadBytes():
        pass

    def TestSerialWrite():
        pass

    def TestReadCalibarationData():
        pass

    def TestgetCalibartionData():
        pass

    def TestgetCalcCalibrate():
        pass

    def TestCalibrateOut():
        pass

    def TestReadCalibrationData():
        pass

    def TestCalibrateIn():
        pass

    def TestCalibrateTemp():
        pass

    def TestIsDocker():
        pass