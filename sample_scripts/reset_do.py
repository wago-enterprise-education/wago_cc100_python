import CC100IO

state = False
for output in range(1,5):
    CC100IO.digitalWrite(output, state)