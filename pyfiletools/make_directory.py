import os

# Function to create a directory
def make_directory(directory_path):
    """
    Create a new directory at the specified path.

    :param directory_path: The path where the directory should be created.
    """
    try:
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully in {os.getcwd()}.")
        print('====================')
    except OSError as e:
        print(f"Failed to create directory: {e}")
        print('====================')
