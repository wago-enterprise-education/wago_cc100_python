import cc100io

while True:
    temp_in = cc100io.tempRead("PT1")
    print(f"Temperatur 1: {temp_in}")
    cc100io.delay(1000)
