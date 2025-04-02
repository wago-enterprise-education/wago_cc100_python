import time


DOUT_DATA = "/sys/kernel/dout_drv/DOUT_DATA"

def digitalWrite(output, value):
    do_file.seek(0)
    currentValue = int(do_file.read())
    
    if output == 1:
        if value:
            currentValue = currentValue | 0b0001
        else:
            currentValue = currentValue & 0b1110
    elif output == 2:
        if value:
            currentValue = currentValue | 0b0010
        else:
            currentValue = currentValue & 0b1101
    elif output == 3:
        if value:
            currentValue = currentValue | 0b0100
        else:
            currentValue = currentValue & 0b1011
    elif output == 4:
        if value:
            currentValue = currentValue | 0b1000
        else:
            currentValue = currentValue & 0b0111
    else:
        print("Output is false")

    do_file.seek(0)
    do_file.write(str(currentValue))
    return True


def start_runtime():
    global do_file
    do_file = open(DOUT_DATA, "r+")
    print("Runtime started.")


def reset_runtime():
    do_file.close()
    print("Runtime reset.")    




start_runtime()
try:
    state = True
    while True:
        start_time = time.time()
        
        for output in range(1, 5):
            digitalWrite(output, state)
        state = not state
        for output in range(4, 0, -1):
            digitalWrite(output, state)
        state = not state
        
        end_time = time.time()
        cycle_time = end_time - start_time
        print(f"Cycle time: {cycle_time * 1000:.2f} milliseconds")
    
except KeyboardInterrupt:
    print("KeyboardInterrupt detected. Exiting...")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    reset_runtime()