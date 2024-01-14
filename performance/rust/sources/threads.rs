use std::io::Write;
use std::fs::OpenOptions;
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::{Instant};
use affinity::*;

fn write_number_to_file(filename: &str, number: f64) {
    let mut log_file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(filename);

    match log_file {
        Ok(ref mut file) => {
            if let Err(err) = writeln!(file, "{}", number) {
                eprintln!("Error writing to file: {}", err);
            }
        }
        Err(err) => eprintln!("Error opening file: {}", err),
    }
}

fn thread_function(shared_variable: Arc<Mutex<i32>>) {
    for _ in 0..10_000_000 {
        // Increment the shared variable inside the critical region
        {
            let mut shared_variable = shared_variable.lock().unwrap();
            *shared_variable += 1;
        }
    }
}

fn main() {
    // Measure time for creating a thread

    let shared_variable = Arc::new(Mutex::new(0));

    let start_create_time = Instant::now();

    let handle = {
        let shared_variable = Arc::clone(&shared_variable);
        thread::spawn(move || {
            thread_function(shared_variable);
        })
    };

    let end_create_time = Instant::now();
    let create_time_duration = end_create_time.duration_since(start_create_time);

    println!(
        "Time for creating the thread: {} microseconds",
        create_time_duration.as_micros()
    );

    write_number_to_file("ThreadCreation_log.rs.txt", create_time_duration.as_micros() as f64);

    // for i in 0..100_000 {
    // Measure time for a context switch
    let start_context_switch_time = Instant::now();

    {
        let mut shared_variable = shared_variable.lock().unwrap();
        *shared_variable += 1;
    }

    let end_context_switch_time = Instant::now();

    let context_switch_duration = end_context_switch_time.duration_since(start_context_switch_time);

    println!(
        "Time for context switch: {} microseconds",
        context_switch_duration.as_micros()
    );

    write_number_to_file("ContextSwitch_log.rs.txt", context_switch_duration.as_micros() as f64);

    // }

    // Measure time for thread migration
    let cores: Vec<usize> = (2..get_core_num()).step_by(2).collect();
    let cores2: Vec<usize> = (1..get_core_num()).step_by(2).collect();

    let _ = set_thread_affinity(&cores);

    let start_thread_migration_time = Instant::now();

    let _ = set_thread_affinity(&cores2);

    let end_thread_migration_time = Instant::now();
    let thread_migration_duration = end_thread_migration_time.duration_since(start_thread_migration_time);

    println!(
        "Time for thread migration: {} microseconds",
        thread_migration_duration.as_micros()
    );

    write_number_to_file("ThreadMigration_log.rs.txt", thread_migration_duration.as_micros() as f64);

    handle.join().unwrap();

}
