import cc100io

state = False
for output in range(1,5):
    cc100io.digitalWrite(output, state)
