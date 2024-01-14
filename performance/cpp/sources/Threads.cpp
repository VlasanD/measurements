#include <iostream>
#include <windows.h>
#include <chrono>
#include <mutex>
#include <fstream>

using namespace std;
using namespace chrono;


// Shared variable
int sharedVariable = 0;

// Mutex for protecting the critical section
mutex mtx;

DWORD WINAPI ThreadFunction(LPVOID lpParam) {
    auto startThreadTime = high_resolution_clock::now();

    for (int i = 0; i < 10000000; i++) {
        // Increment the shared variable inside the critical region
        {
            lock_guard<mutex> lock(mtx);
            sharedVariable++;
        }
    }
    return 0;
}

void WriteNumberToFile(const string& filename, const double number) {
    ofstream logFile(filename, ios::app);
    if (!logFile.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        return;
    }

    logFile << number << endl;

    if (logFile.fail()) {
        cerr << "Error writing to file: " << filename << endl;
    }
    logFile.close();
}

int main() {
    // Măsoară timpul pentru crearea unui thread
    auto startCreateTime = high_resolution_clock::now();

    HANDLE hThread1 = CreateThread(nullptr, 0, ThreadFunction, nullptr, 0, nullptr);
    HANDLE hThread2 = CreateThread(nullptr, 0, ThreadFunction, (LPVOID)1, 0, nullptr);

    auto endCreateTime = high_resolution_clock::now();
    auto createTimeDuration = duration_cast<microseconds>(endCreateTime - startCreateTime).count();

    cout << "Timpul pentru crearea thread-ului: " << createTimeDuration / 2 << " microsecunde" << endl;

    // Măsoară timpul pentru un context switch
    auto startContextSwitchTime = high_resolution_clock::now();

    {
        lock_guard<mutex> lock(mtx);
        Sleep(0);
    }

    auto endContextSwitchTime = high_resolution_clock::now();
    auto contextSwitchDuration = duration_cast<microseconds>(endContextSwitchTime - startContextSwitchTime).count();

    cout << "Timpul pentru context switch: " << contextSwitchDuration << " microsecunde" << endl;

    // Măsoară timpul pentru migrația unui thread
    auto startThreadMigrationTime = high_resolution_clock::now();

    DWORD_PTR currentAffinityMask = 0;
    DWORD_PTR systemAffinityMask = 0;

    if (GetProcessAffinityMask(GetCurrentProcess(), &currentAffinityMask, &systemAffinityMask)) {
        if ((currentAffinityMask & (1 << 1)) != 0) {
            SetThreadAffinityMask(hThread1, 1 << 0); // Migrează pe al doilea core
        }
        else{
            SetThreadAffinityMask(hThread1, 1 << 1); // Migrează pe al doilea core
        }
    }

    auto endThreadMigrationTime = high_resolution_clock::now();
    auto threadMigrationDuration = duration_cast<microseconds>(endThreadMigrationTime - startThreadMigrationTime).count();

    cout << "Timpul pentru migrația thread-ului: " << threadMigrationDuration << " microsecunde" << endl;

    WaitForSingleObject(hThread2, INFINITE);
    WaitForSingleObject(hThread1, INFINITE);

    CloseHandle(hThread1);
    CloseHandle(hThread2);

    WriteNumberToFile("ThreadCreation_log.cpp.txt", createTimeDuration / 2);
    WriteNumberToFile("ContextSwitch_log.cpp.txt", contextSwitchDuration);
    WriteNumberToFile("ThreadMigration_log.cpp.txt", threadMigrationDuration);

    return 0;
}
