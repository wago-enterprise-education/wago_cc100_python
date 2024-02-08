import CC100IO

while True:
    for input in range(1,9):
        input_value = CC100IO.digitalRead(input)
        print(f"Input_{input}: {input_value}")
    print("\n")
    CC100IO.delay(500)