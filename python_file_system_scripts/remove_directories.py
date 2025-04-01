import os

# Function to remove a directory
def remove_directory(directory_path):
    """
    Remove a directory at the specified path.

    :param directory_path: The path of the directory to be removed.
    :type directory_path: str
    :raises OSError: If the directory cannot be removed.
    """
    try:
        os.rmdir(directory_path)
        print(f"Directory '{directory_path}' deleted successfully.")
        print('====================')
    except OSError as e:
        print(f"Failed to delete directory: {e}")
        print('====================')

# Function to list all subdirectories in the current working directory
def list_subdirectories():
    """
    Lists all subdirectories directly under the current working directory.

    :return: A list of subdirectory names.
    :rtype: list of str
    """
    try:
        subdirectories = [d for d in os.listdir('.') if os.path.isdir(d)]
        return subdirectories
    except OSError as e:
        print(f"Failed to list subdirectories: {e}")
        return [] # Return empty list in case of error

# Example usage (demonstration)
if __name__ == "__main__":
    # Create a test directory (if it doesn't exist)
    test_dir = "test_directory"
    if not os.path.exists(test_dir):
        try:
            os.mkdir(test_dir)
            print(f"Created directory '{test_dir}' for testing.")
        except OSError as e:
            print(f"Failed to create test directory: {e}")
            test_dir = None #Avoid errors if test directory was not created.

    # List subdirectories
    print("Subdirectories in the current directory:")
    subdirs = list_subdirectories()
    if subdirs:
        for subdir in subdirs:
            print(subdir)
    else:
        print("No subdirectories found.")

    # Remove the test directory (if it was created)
    if test_dir:
        remove_directory(test_dir)
