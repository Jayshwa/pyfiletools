import os

def list_files_in_directory(directory):
    """
    List all files in the specified directory.

    :param directory: The directory to list files from.
    :type directory: str
    :return: A list of file names in the directory.
    :rtype: list of str
    :raises OSError: If the directory does not exist or cannot be accessed.
    """

    try:
        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        if files:
            print(f'Here are the files found in: {directory}')
            for file in files:
                print(file)
            print('====================')
            return files
        else:
            print(f'There are no files inside {directory}')
            print('====================')
            return []
    except OSError as e:
        print(f"Error: {e}")
        print('====================')
        return []

# Example usage (demonstration)
if __name__ == "__main__":
    # Create a test directory and files
    test_dir = "test_files"
    if not os.path.exists(test_dir):
        try:
            os.makedirs(test_dir)
            print(f"Created directory '{test_dir}' for testing.")
        except OSError as e:
            print(f"Failed to create test directory: {e}")
            test_dir = None

    if test_dir:
        try:
            with open(os.path.join(test_dir, "file1.txt"), "w") as f1:
                f1.write("Test content 1")
            with open(os.path.join(test_dir, "file2.py"), "w") as f2:
                f2.write("print('Hello, world!')")
            print(f"Created test files in '{test_dir}'.")
        except OSError as e:
            print(f"Failed to create test files: {e}")

        # List files in the test directory
        found_files = list_files_in_directory(test_dir)
        print(f"Found files: {found_files}")

        # List files in a non-existent directory
        nonexistent_files = list_files_in_directory("nonexistent_dir")
        print(f"Found files in nonexistent: {nonexistent_files}")

        # Clean up the test directory and files
        try:
            os.chdir(os.path.dirname(os.path.abspath(test_dir)))
            os.system(f'rm -rf {test_dir}')
            print(f"Test directory '{test_dir}' cleaned up.")
        except OSError as e:
            print(f"Failed to clean up test directory: {e}")
