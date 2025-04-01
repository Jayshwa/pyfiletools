import os

# Function to list all subdirectories in the current working directory
def list_subdirectories():
    """
    List all subdirectories in the current working directory.

    :return: A list of subdirectory names.
    :rtype: list of str
    :raises OSError: If an error occurs while listing subdirectories.
    """
    try:
        current_dir = os.getcwd()
        subdirectories = [d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d))]

        if not subdirectories:
            print("No subdirectories in the current working directory.")
            print('====================')
            return []
        else:
            print("Subdirectories in the current working directory:")
            for subdirectory in subdirectories:
                print(subdirectory)
            print('====================')
            return subdirectories
    except OSError as e:
        print(f'Error: {e}')
        print('====================')
        return []

# Example usage (demonstration)
if __name__ == "__main__":
    # Create test subdirectories
    test_dirs = ["subdir1", "subdir2", "subdir3"]
    for dir_name in test_dirs:
        if not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
                print(f"Created subdirectory '{dir_name}' for testing.")
            except OSError as e:
                print(f"Failed to create subdirectory '{dir_name}': {e}")
                test_dirs = [] #prevent errors if subdirs were not created.

    # List subdirectories
    found_subdirs = list_subdirectories()
    print(f"Found subdirectories: {found_subdirs}")

    # Clean up test subdirectories
    if test_dirs:
        for dir_name in test_dirs:
            try:
                os.rmdir(dir_name)
                print(f"Removed subdirectory '{dir_name}'.")
            except OSError as e:
                print(f"Failed to remove subdirectory '{dir_name}': {e}")
