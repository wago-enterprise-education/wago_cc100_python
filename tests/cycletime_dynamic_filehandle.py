from lib import CC100IO
import time

# Sample script for writing digital Outputs

state = True
while True:
    start_time = time.time()
    
    for output in range(1, 5):
        CC100IO.digitalWrite(output, state)
    state = not state
    for output in range(4, 0, -1):
        CC100IO.digitalWrite(output, state)
    state = not state
    
    end_time = time.time()
    cycle_time = end_time - start_time
    print(f"Cycle time: {cycle_time * 1000:.2f} milliseconds")