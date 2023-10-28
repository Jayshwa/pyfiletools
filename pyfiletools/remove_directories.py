import os 

# Function to remove a directory
def remove_directory(directory_path):
    """
    Remove a directory at the specified path.

    :param directory_path: The path of the directory to be removed.
    """
    try:
        os.rmdir(directory_path)
        print(f"Directory '{directory_path}' deleted successfully.")
        print('====================')
    except OSError as e:
        print(f"Failed to delete directory: {e}")
        print('====================')

# Function to list all subdirectories in the current working directory