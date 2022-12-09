#Lügendetektor...

import statistics

list = [12, 24, 36, 48, 60]
print("List : " + str(list))

st_dev = statistics.pstdev(list)
print("Standard deviation of the given list: " + str(st_dev))

def std():
  