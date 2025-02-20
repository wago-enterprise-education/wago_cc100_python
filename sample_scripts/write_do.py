import cc100io

state = True
while True:
    for output in range(1,5):
        cc100io.digitalWrite(output, state)
        cc100io.delay(100)
    state = not state
