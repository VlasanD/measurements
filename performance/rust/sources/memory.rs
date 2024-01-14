use std::fs::OpenOptions;
use std::time::Instant;
use std::io::Write;

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

fn main() {
    let mut array_static: [i32; 100000] = [0; 100000];

    // Măsurarea timpului pentru alocarea de memorie dinamică
    let start_dynamic = Instant::now();
    let mut vec_dynamic = vec![0; 100000];
    let end_dynamic = Instant::now();
    let duration_dynamic = (end_dynamic - start_dynamic).as_micros();
    println!(
        "Timpul pentru alocarea de memorie dinamica: {} microsecunde",
        duration_dynamic
    );

    // Accesul la memorie
    let start_access_static = Instant::now();
    for i in 0..100000 {
        array_static[i] = i as i32; // Acces la memorie statică
    }
    let end_access_static = Instant::now();
    let duration_access_static = (end_access_static - start_access_static).as_micros();
    println!(
        "Timpul pentru accesul la memorie statica: {} microsecunde",
        duration_access_static
    );

    let start_access_dynamic = Instant::now();
    for i in 0..100000 {
        vec_dynamic[i] = i as i32; // Acces la memorie dinamică
    }
    let end_access_dynamic = Instant::now();
    let duration_access_dynamic = (end_access_dynamic - start_access_dynamic).as_micros();
    println!(
        "Timpul pentru accesul la memorie dinamica: {} microsecunde",
        duration_access_dynamic
    );

    // Write durations to a file
    write_number_to_file("DynamicAlloc_log.rs.txt", duration_dynamic as f64);
    write_number_to_file("StaticAccess_log.rs.txt", duration_access_static as f64);
    write_number_to_file("DynamicAccess_log.rs.txt", duration_access_dynamic as f64);
}
