//#include <iostream>
//#include <chrono>
//#include <fstream>
//
//using namespace std;
//
//void WriteNumberToFile(const string &filename, const double number) {
//    ofstream logFile(filename, ios::app);
//    if (!logFile.is_open()) {
//        cerr << "Error opening file: " << filename << endl;
//        return;
//    }
//
//    logFile << number << endl;
//
//    if (logFile.fail()) {
//        cerr << "Error writing to file: " << filename << endl;
//    }
//    logFile.close();
//}
//
//int main() {
//
//    int arrayStatic[100000];
//
//    // Măsurarea timpului pentru alocarea de memorie dinamică
//    auto startDynamic = std::chrono::high_resolution_clock::now();
//    int *arrayDynamic = new int[100000];
//    auto endDynamic = std::chrono::high_resolution_clock::now();
//    std::cout << "Timpul pentru alocarea de memorie dinamica: "
//              << std::chrono::duration_cast<std::chrono::microseconds>(endDynamic - startDynamic).count()
//              << " microsecunde" << std::endl;
//
//    // Accesul la memorie
//    auto startAccessStatic = std::chrono::high_resolution_clock::now();
//    for (int i = 0; i < 100000; ++i) {
//        arrayStatic[i] = i; // Acces la memorie statică
//    }
//    auto endAccessStatic = std::chrono::high_resolution_clock::now();
//    std::cout << "Timpul pentru accesul la memorie statica: "
//              << std::chrono::duration_cast<std::chrono::microseconds>(endAccessStatic - startAccessStatic).count()
//
//              << " microsecunde" << std::endl;
//
//    auto startAccessDynamic = std::chrono::high_resolution_clock::now();
//    for (int i = 0; i < 100000; ++i) {
//        arrayDynamic[i] = i; // Acces la memorie dinamică
//    }
//    auto endAccessDynamic = std::chrono::high_resolution_clock::now();
//    std::cout << "Timpul pentru accesul la memorie dinamica: "
//              << std::chrono::duration_cast<std::chrono::microseconds>(endAccessDynamic - startAccessDynamic).count()
//
//              << " microsecunde" << std::endl;
//
//    delete[] arrayDynamic;
//
//    WriteNumberToFile("DynamicAlloc_log.cpp.txt",
//                      chrono::duration_cast<chrono::microseconds>(endDynamic - startDynamic).count());
//    WriteNumberToFile("StaticAccess_log.cpp.txt",
//                      chrono::duration_cast<chrono::microseconds>(endAccessStatic - startAccessStatic).count()
//    );
//    WriteNumberToFile("DynamicAccess_log.cpp.txt",
//                      chrono::duration_cast<chrono::microseconds>(endAccessDynamic - startAccessDynamic).count()
//    );
//
//    return 0;
//}
