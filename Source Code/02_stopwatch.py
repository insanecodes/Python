import time

print("press Enter to start the stopwatch")
print("and press ctrl + c to stop the the stopwatch")

while True:
    try:
        input()
        start_time = time.time()
        print("stopwatch started")
    
    except KeyboardInterrupt:
        print("stopwatch stopped...")
        end_time = time.time()
        print("the total time:",round(end_time -start_time,2),"second")
        break
