# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries
#  starting from 1 second, but stops after 5 retries.

import time

## Using For Loop
wait_time = 1 
for i in range(1,6):
    print(f"Trying to Reconnect {i} out of 5 : Expected Time {wait_time} Second/Seconds")
    time.sleep(wait_time)
    wait_time *= 2


#### Using While Loop
wait_time = 1
i = 1
while i < 6:
    print(f"Trying to Reconnect {i} out of 5 : Expected Time {wait_time} Second/Seconds")
    time.sleep(wait_time)
    wait_time *= 2
    i += 1