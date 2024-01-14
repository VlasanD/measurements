import threading
import time
import psutil

# Shared variable
shared_variable = 0

# Lock for protecting the critical section
lock = threading.Lock()

def write_number_to_file(filename, number):
    try:
        with open(filename, 'a') as file:
            file.write(str(number) + '\n')
    except IOError as e:
        print(f"Error opening/writing to file {filename}: {e}")

def thread_function(thread_id):
    global shared_variable
    for _ in range(10000000):
        # Increment the shared variable inside the critical region
        with lock:
            shared_variable += 1

def get_context_switch_time():
    # Get the number of context switches before the sleep
    start_ctx_switches = psutil.cpu_stats().ctx_switches

    # Sleep for a short duration
    time.sleep(0.1)

    # Get the number of context switches after the sleep
    end_ctx_switches = psutil.cpu_stats().ctx_switches

    # Calculate the context switch time
    ctx_switch_time = (end_ctx_switches - start_ctx_switches) / 0.1

    return ctx_switch_time

if __name__ == "__main__":
    # Measure the time for creating threads
    start_create_time = time.time()

    thread1 = threading.Thread(target=thread_function, args=(1,))
    thread2 = threading.Thread(target=thread_function, args=(2,))

    thread1.start()
    thread2.start()

    end_create_time = time.time()
    create_time_duration = ((end_create_time - start_create_time) / 2) * 1000000
    print(f"Time for creating threads: {create_time_duration} microseconds")

    # Measure the time for a context switch
    context_switch_time_microsec = get_context_switch_time()

    print(f"Time for context switch: {context_switch_time_microsec} microseconds")

    # Measure the time for thread migration
    start_thread_migration_time = time.time()

    pid = psutil.Process().pid

    new_affinity = [0] if psutil.Process(pid).cpu_affinity() == [1] else [1]
    psutil.Process(pid).cpu_affinity(new_affinity)

    end_thread_migration_time = time.time()
    thread_migration_duration = (end_thread_migration_time - start_thread_migration_time) * 1000000
    print(f"Time for thread migration: {thread_migration_duration} microseconds")

    thread1.join()
    thread2.join()

    # Write durations to a file
    write_number_to_file("ThreadCreation_log.py.txt", create_time_duration)
    write_number_to_file("ContextSwitch_log.py.txt", context_switch_time_microsec)
    write_number_to_file("ThreadMigration_log.py.txt", thread_migration_duration)
