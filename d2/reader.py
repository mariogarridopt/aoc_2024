def read_file(file_path):
    """
    Reads a file and returns its lines as a list.
    :param file_path: Path to the text file
    :return: List of lines from the file
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Strip newline characters and return the lines
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
