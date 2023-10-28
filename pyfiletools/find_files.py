import os

# Function to find files within the specified root directory
def find_files(check_files, root_directory):
    """
    Find files with a specified name within the specified root directory.

    :param check_files: The name of the file to search for.
    :param root_directory: The root directory to start the search from.
    :return: A list of full paths to matching files, or an empty list if none are found.
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
    else:
        print(f'No files matching {check_files} were found in {root_directory}')
        print('====================')
