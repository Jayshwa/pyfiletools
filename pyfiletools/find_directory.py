import os

# Function to find directories within the specified root directory
def find_directory(check_directory, root_directory):
    """
    Find directories with a specified name within the specified root directory.

    :param check_directory: The name of the directory to search for.
    :param root_directory: The root directory to start the search from.
    :return: A list of full paths to matching directories, or an empty list if none are found.
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
    else:
        print(f'No directories matching {check_directory} were found in {root_directory}')
        print('====================')
