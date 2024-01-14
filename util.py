def read_numbers_from_file(file_path, n):
    """
    Read n numbers from a file and return a list.

    Parameters:
    - file_path (str): The path to the file.
    - n (int): The number of values to read from the file.

    Returns:
    - list: A list containing n numbers read from the file.
    """
    numbers = []

    try:
        with open(file_path, 'r') as file:
            # Use list comprehension to read n numbers from the file
            numbers = [float(file.readline().strip()) for _ in range(n)]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print(f"Error:Unable to convert a value to a number from {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return numbers
