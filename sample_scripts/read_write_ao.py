import cc100io

voltage_out = 0     # voltage in mV

while voltage_out < 10000:
    cc100io.analogWrite(1, voltage_out)
    voltage_in_1 = cc100io.analogRead(1)
    print(f"Analogeingang 1: {voltage_in_1}mV")
    voltage_out += 500
    cc100io.delay(1000)
