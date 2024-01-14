import time

def write_number_to_file(filename, number):
    try:
        with open(filename, 'a') as file:
            file.write(str(number) + '\n')
    except IOError as e:
        print(f"Error opening/writing to file {filename}: {e}")

# Measure time for memory allocation
start_dynamic = time.time()
array_dynamic = [0] * 100000
end_dynamic = time.time()
memory_allocation_duration = int((end_dynamic - start_dynamic) * 1e6)

# Measure time for memory access
start_access_static = time.time()
for i in range(100000):
    array_dynamic[i] = i
end_access_static = time.time()
memory_access_duration = int((end_access_static - start_access_static) * 1e6)

# Write durations to a file
write_number_to_file("Alloc_log.py.txt", memory_allocation_duration)
write_number_to_file("Access_log.py.txt", memory_access_duration)
print(f"Memory allocation duration: {memory_allocation_duration}")
print(f"Memory access duration: {memory_access_duration}")
