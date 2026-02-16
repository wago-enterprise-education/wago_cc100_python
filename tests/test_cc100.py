import unittest

import CC100IO as cc
import unittest

class Test_cc100(unittest.TestCase):
    def test_non_existing_output(self):
        with self.assertLogs(level="WARNING") as cm:
            cc.digitalWrite(5)
        self.assertEqual(cm.output, ["WARNING:CC100IO:Output does not exist"])

    def test_digital_write(self):
        for i in range(1, 5):
            for j in range(2):
                cc.digitalWrite(i,j)

    def test_non_existing_input(self):
        with self.assertLogs(level="WARNING") as cm:
                cc.digitalRead(9)
        self.assertEqual(cm.output, ["WARNING:CC100IO:Input does not exist"])
              
    def test_digital_read(self):
        for i in range(1,9):
            cc.digitalRead(i)
            
    def test_non_existing_analog_output(self):
        with self.assertLogs(level="WARNING") as cm:
            cc.analogWrite(3)
        self.assertEqual(cm.output,["WARNING:CC100IO:Output does not exist"])


    def test_analog_write(self):
        for i in range(1,2):
            for j in range(0,10001,1000):
                cc.analogWrite(i,j)
        
    def test_non_existing_analog_input(self):
        with self.assertLogs(level="WARNING") as cm:
            cc.analogRead(3)
        self.assertEqual(cm.output,["WARNING:CC100IO:Input does not exist"])

    def test_analog_read(self):
        for i in range(1,2):
            cc.analogRead(i)
        
    def test_delay(self):
        pass
    
    def test_temp_read(self):
        pass

    def TestSerialReadLine(self):
        pass

    def test_serial_read_bytes(self):
        pass

    def test_serial_write(self):
        pass

    def test_read_calibration_data(self):
        pass

    def test_get_calibration_data(self):
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

if __name__ == '__main__':
    unittest.main()