import os

# Function to find files within the specified root directory
def find_files(check_files, root_directory):
    """
    Find files with a specified name within the specified root directory.

    :param check_files: The name of the file to search for.
    :type check_files: str
    :param root_directory: The root directory to start the search from.
    :type root_directory: str
    :return: A list of full paths to matching files, or an empty list if none are found.
    :rtype: list of str
    """
    print(f'Searching for files named "{check_files}" in: {root_directory}')
    check_files = check_files.lower()
    matching_files = []

    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.lower() == check_files:
                matching_files.append(os.path.join(root, file))

    if matching_files:
        for matching_file in matching_files:
            print(matching_file)
        print('====================')
        return matching_files
    else:
        print(f'No files matching {check_files} were found in {root_directory}')
        print('====================')
        return []

# Example usage (demonstration)
if __name__ == "__main__":
    # Create test files
    test_root = "test_root"
    test_file1 = os.path.join(test_root, "testfile.txt")
    test_file2 = os.path.join(test_root, "subdir", "TestFile.txt") # Test case insensitivity

    if not os.path.exists(os.path.dirname(test_file2)):
        try:
            os.makedirs(os.path.dirname(test_file2))
        except OSError as e:
            print(f"Failed to create test directories: {e}")
            test_root=None

    if test_root:
        try:
            with open(test_file1, "w") as f1:
                f1.write("Test content")
            with open(test_file2, "w") as f2:
                f2.write("Test content")
            print(f"Created files '{test_file1}' and '{test_file2}' for testing.")
        except OSError as e:
            print(f"Failed to create test files: {e}")

        # Search for the test file
        found_files = find_files("testfile.txt", test_root)
        print(f"Found files: {found_files}")

        # Search for the test file with different case
        found_files2 = find_files("TestFile.txt", test_root)
        print(f"Found files: {found_files2}")

        # Search for a non-existent file
        found_files3 = find_files("nonexistent.txt", test_root)
        print(f"Found files: {found_files3}")

        # Cleanup test files and directories
        try:
            os.chdir(os.path.dirname(os.path.abspath(test_root)))
            os.system(f'rm -rf {test_root}')
            print("Test files and directories cleaned up.")
        except OSError as e:
            print(f"Failed to clean up test files and directories: {e}")
