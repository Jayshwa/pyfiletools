import os

def list_files_in_directory(directory):
    """
    List all files in the specified directory.

    :param directory: The directory to list files from.
    :return: A list of file names in the directory.
    """

    try:
        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        if files:
            print(f'Here are the files found in: {directory}')
            for file in files:
                print(file)
            print('====================')    
        else:
            print(f'There are no files inside {directory}')
            print('====================') 
    except OSError as e:
        print(f"Error: {e}")
        print('====================')
