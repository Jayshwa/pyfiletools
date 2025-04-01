import os

# Function to find directories within the specified root directory
def find_directory(check_directory, root_directory):
    """
    Find directories with a specified name within the specified root directory.

    :param check_directory: The name of the directory to search for.
    :type check_directory: str
    :param root_directory: The root directory to start the search from.
    :type root_directory: str
    :return: A list of full paths to matching directories, or an empty list if none are found.
    :rtype: list of str
    """
    print(f'Searching for directories named "{check_directory}" in: {root_directory}')
    check_directory = check_directory.lower()
    matching_directories = []

    for root, dirs, files in os.walk(root_directory):
        for directory in dirs:
            if directory.lower() == check_directory:
                matching_directories.append(os.path.join(root, directory))

    if matching_directories:
        for matching_directory in matching_directories:
            print(matching_directory)
        print('====================')
        return matching_directories
    else:
        print(f'No directories matching {check_directory} were found in {root_directory}')
        print('====================')
        return []

# Example usage (demonstration)
if __name__ == "__main__":
    # Create test directories
    test_root = "test_root"
    test_dir1 = os.path.join(test_root, "testdir")
    test_dir2 = os.path.join(test_root, "subdir", "TestDir") # Test case insensitivity

    if not os.path.exists(test_dir2):
        try:
            os.makedirs(test_dir2)
            print(f"Created directories '{test_dir2}' for testing.")
        except OSError as e:
            print(f"Failed to create test directories: {e}")
            test_root = None #Avoid errors if test directory was not created.

    if test_root:
        # Search for the test directory
        found_dirs = find_directory("testdir", test_root)
        print(f"Found directories: {found_dirs}")

        # Search for the test directory with different case
        found_dirs2 = find_directory("TestDir", test_root)
        print(f"Found directories: {found_dirs2}")

        # Search for a non-existent directory
        found_dirs3 = find_directory("nonexistent", test_root)
        print(f"Found directories: {found_dirs3}")
        try:
            os.chdir(os.path.dirname(os.path.abspath(test_root)))
            os.system(f'rm -rf {test_root}') # Delete the test directory and all contents.
            print("Test directories cleaned up.")
        except OSError as e:
            print(f"Failed to clean up test directories: {e}")
