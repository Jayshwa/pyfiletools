import os

# Function to change the current working directory
def change_directory(target_dir):
    """
    Change the current working directory to the specified directory.

    :param target_dir: The path of the directory to change to.
    :type target_dir: str
    :raises OSError: If the directory change fails.
    """
    try:
        if target_dir == '..':
            # Handle changing to the parent directory
            parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
            try:
                os.chdir(parent_directory)
                print(f'Changed working directory to: {os.getcwd()}')
                print('====================')
            except OSError as e:
                print(f'Error: {e}')
                print('====================')
        else:
            # Handle changing to a specified subdirectory or absolute path
            try:
                os.chdir(target_dir)
                print(f'Changed working directory to: {os.getcwd()}')
                print('====================')
            except OSError as e:
                print(f'Error: {e}')
                print('====================')
    except OSError as e:
        # Catch any errors that might happen when getting the parent directory
        print(f'Error: {e}')
        print('====================')

# Example usage (demonstration)
if __name__ == "__main__":
    # Create a test directory and subdirectory
    test_dir = "test_dir"
    test_subdir = os.path.join(test_dir, "subdir")

    if not os.path.exists(test_subdir):
        try:
            os.makedirs(test_subdir)
            print(f"Created directories '{test_subdir}' for testing.")
        except OSError as e:
            print(f"Failed to create test directories: {e}")
            test_dir = None #Avoid errors if test directory was not created.

    if test_dir:
        # Change to the test subdirectory
        change_directory(test_subdir)

        # Change back to the parent directory (test_dir)
        change_directory('..')

        # Change back to the parent of test_dir
        change_directory('..')

        # Clean up the test directories
        try:
            os.chdir(os.path.dirname(os.path.abspath(test_dir))) #change directory to test_dir parent.
            os.rmdir(test_subdir)
            os.rmdir(test_dir)
            print("Test directories cleaned up.")
        except OSError as e:
            print(f"Failed to clean up test directories: {e}")
