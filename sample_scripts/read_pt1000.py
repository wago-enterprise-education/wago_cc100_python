import CC100IO

while True:
    temp_in = CC100IO.tempRead("PT1")
    print(f"Temperatur 1: {temp_in}")
    CC100IO.delay(1000)