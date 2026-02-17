import os
import unittest
from unittest import mock

from pyfakefs import fake_filesystem_unittest

import CC100IO as cc
from CC100IO.CC100IO import SYSTEM_PATHS

TEST_CALIB_DATA = """PT1 PT2 AI1 AI2 A01 A02
12452 1182 21785 1777
12402 1179 21767 1788
5898 1025 50375 9022
5698 990 50205 8997
1064 350 8976 3000
1053 350 8966 3000
"""

class Test_9301(fake_filesystem_unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.setUpClassPyfakefs()

        # create files and directories
        for path in SYSTEM_PATHS:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                if path.startswith("/sys/"):
                    f.write("0")
                elif path == "/etc/calib":
                    f.write(TEST_CALIB_DATA)

    def test_non_existing_output(self):
        with self.assertLogs(level="WARNING") as cm:
            self.assertFalse(cc.digitalWrite(5, True))
            self.assertFalse(cc.analogWrite(3, 1000))
        self.assertEqual(
            cm.output,
            [
                "WARNING:CC100IO.CC100IO:Digital output does not exist",
                "WARNING:CC100IO.CC100IO:Analog output does not exist"
            ]
        )

    # Read from digital output file to control written value
    @mock.patch("CC100IO.CC100IO.DIN", cc.CC100IO.DOUT_DATA)
    def test_digital_write(self):
        for i in range(1, 5):
            for j in range(2):
                self.assertTrue(cc.digitalWrite(i,j))
                self.assertEqual(cc.digitalRead(i), j)

    def test_non_existing_input(self):
        with self.assertLogs(level="WARNING") as cm:
                self.assertFalse(cc.digitalRead(9))
                self.assertFalse(cc.analogRead(3))
        self.assertEqual(
            cm.output,
            [
                "WARNING:CC100IO.CC100IO:Digital input does not exist",
                "WARNING:CC100IO.CC100IO:Analog input does not exist"
            ]
        )
              
    def test_digital_read(self):
        for i in range(1,9):
            cc.digitalRead(i)

    def test_analog_write(self):
        for i in range(1,3):
            for j in range(0,10001,1000):
                self.assertTrue(cc.analogWrite(i,j))
        
    def test_analog_read(self):
        for i in range(1,2):
            cc.analogRead(i)
        
    def test_temp_read(self):
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

if __name__ == '__main__':
    unittest.main()
