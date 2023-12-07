import time

my_dict = {}
COUNT = 10000000

n = COUNT
start_time = time.time()


for i in range(n):
    my_dict["key-" + str(i)] = i * 3

elapsed_time = time.time() - start_time

print(f"set from dict: {elapsed_time:.6f} seconds")

n = COUNT

total = 0
start_time_get = time.time()
for i in range(n):
    total += my_dict["key-" + str(i)]

elapsed_time_get = time.time() - start_time_get

print(f"get from dict: {elapsed_time_get:.6f} seconds")
