from util import read_numbers_from_file

NO_TESTS = 500

dynamic_alloc = {
    'C++': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\DynamicAlloc_log.cpp.txt",
                                  NO_TESTS),
    'Rust': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\DynamicAlloc_log.rs.txt",
                                   NO_TESTS),
    'Python': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\Alloc_log.py.txt", NO_TESTS)
}

static_access = {
    'C++': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\StaticAccess_log.cpp.txt",
                                  NO_TESTS),
    'Rust': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\StaticAccess_log.rs.txt",
                                   NO_TESTS),
    'Python': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\Access_log.py.txt",
                                     NO_TESTS)
}

dynamic_access = {
    'C++': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\DynamicAlloc_log.cpp.txt",
                                  NO_TESTS),
    'Rust': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\DynamicAccess_log.rs.txt",
                                   NO_TESTS),
    'Python': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\Access_log.py.txt",
                                     NO_TESTS)
}

threads = {
    'C++': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ThreadCreation_log.cpp.txt",
                                  NO_TESTS),
    'Rust': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ThreadCreation_log.rs.txt",
                                   NO_TESTS),
    'Python': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ThreadCreation_log.py.txt",
                                     NO_TESTS)
}

context = {
    'C++': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ContextSwitch_log.cpp.txt",
                                  NO_TESTS),
    'Rust': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ContextSwitch_log.rs.txt",
                                   NO_TESTS),
    'Python': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ContextSwitch_log.py.txt",
                                     NO_TESTS)
}

migration = {
    'C++': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ThreadMigration_log.cpp.txt",
                                  NO_TESTS),
    'Rust': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ThreadMigration_log.rs.txt",
                                   NO_TESTS),
    'Python': read_numbers_from_file(r"C:\Users\Darius\Desktop\Measurements\gui\performance\ThreadMigration_log.py.txt",
                                     NO_TESTS)
}
