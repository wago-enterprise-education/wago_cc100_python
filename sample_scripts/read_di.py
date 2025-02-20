import cc100io

while True:
    for input in range(1,9):
        input_value = cc100io.digitalRead(input)
        print(f"Input_{input}: {input_value}")
    print("\n")
    cc100io.delay(500)
