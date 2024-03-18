import CC100IO

voltage_out = 0     # voltage in mV

while voltage_out < 10000:
    CC100IO.analogWrite(1, voltage_out)
    voltage_in_1 = CC100IO.analogRead(1)
    print(f"Analogeingang 1: {voltage_in_1}mV")
    voltage_out += 500
    CC100IO.delay(1000)