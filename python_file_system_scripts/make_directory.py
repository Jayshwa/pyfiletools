import os

# Function to create a directory
def make_directory(directory_path):
    """
    Create a new directory at the specified path.

    :param directory_path: The path where the directory should be created.
    :type directory_path: str
    :raises OSError: If the directory cannot be created.
    """
    try:
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully in {os.getcwd()}.")
        print('====================')
    except OSError as e:
        print(f"Failed to create directory: {e}")
        print('====================')

# Example usage (demonstration)
if __name__ == "__main__":
    # Create a test directory
    test_dir = "test_make_dir"

    # Create the directory
    make_directory(test_dir)

    # Attempt to create the same directory again (should fail)
    make_directory(test_dir)

    # Clean up the test directory
    try:
        os.rmdir(test_dir)
        print(f"Test directory '{test_dir}' cleaned up.")
    except OSError as e:
        print(f"Failed to clean up test directory: {e}")
