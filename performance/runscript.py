import subprocess
import sys

import benchmarks

memory_cpp_path = "cpp/AllocAndAccessCPP.exe"
threads_cpp_path = "cpp/ThreadsCPP.exe"
memory_rust_path = "rust/Rust.exe"
threads_rust_path = "rust/Threads.exe"
memory_python_path = "python/AllocationAndAccess.py"
threads_python_path = "python/Threads.py"
python_path = sys.executable


# Loop to run the executable multiple times
for i in range(benchmarks.NO_TESTS):
    # # C++
    # subprocess.run([memory_cpp_path], check=True)
    # subprocess.run([threads_cpp_path], check=True)
    # # Python
    subprocess.run([python_path, memory_python_path], check=True)
    # subprocess.run([python_path, threads_python_path], check=True)
    # # Rust
    # subprocess.run([threads_rust_path], check=True)
    # subprocess.run([memory_rust_path], check=True)


print("Execution completed!")
