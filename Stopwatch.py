import time
import datetime
current_time=datetime.datetime.now()
print(current_time)
start_time=time.time()
print(start_time)
input("Press enter to stop the stop watch")
end_time=time.time()
elapse_time=end_time-start_time
print(elapse_time)
