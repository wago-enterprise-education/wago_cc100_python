import CC100IO

state = True
while True:
    for output in range(1,5):
        CC100IO.digitalWrite(output, state)
        CC100IO.delay(100)
    state = not state