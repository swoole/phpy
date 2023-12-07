import time


def microtime_true():
    return time.time() * 1000000


COUNT = 10000000

n = COUNT
start_time = time.time()

my_dict = {}
for i in range(n):
    my_dict["key-" + str(i)] = i * 3

elapsed_time = time.time() - start_time

print(f"set from dict: {elapsed_time:.6f} seconds")

n = COUNT
start_time = time.time()

total = 0
my_dict = {}
for i in range(n):
    my_dict["key-" + str(i)] = i * 3

start_time_get = time.time()
for i in range(n):
    total += my_dict["key-" + str(i)]

elapsed_time_get = time.time() - start_time_get

print(f"get from dict: {elapsed_time_get:.6f} seconds")
