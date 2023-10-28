import os

# Function to change the current working directory
def change_directory(target_dir):
    """
    Change the current working directory to the specified directory.

    :param target_dir: The path of the directory to change to.
    """
    try:
        parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        if target_dir == '..':
            try:
                os.chdir(parent_directory)
                print(f'Changed working directory to: {os.getcwd()}')
                print('====================')
            except OSError as e:
                print(f'Error: {e}')
                print('====================')
        else:
            try:
                os.chdir(target_dir)
                print(f'Changed working directory to: {os.getcwd()}')
                print('====================')
            except OSError as e:
                print(f'Error: {e}')
                print('====================')
    except OSError as e:
        print(f'Error: {e}')
        print('====================')