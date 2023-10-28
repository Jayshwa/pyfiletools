
import os
import shutil

import os
import shutil

# Function to move a file from the source directory to a target directory
def move_file(source_dir):
    # List of files to move
    files_to_move = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    if not files_to_move:
        print(f'No files to move in {source_dir}')
        print('====================')
        return

    # Print available files for moving
    print('Files available for moving:')
    for i, file in enumerate(files_to_move, 1):
        print(f"{i}. {file}")

    # Ask the user to choose a file to move
    try:
        choice = int(input("Enter the number of the file you wish to move: "))
        if 1 <= choice <= len(files_to_move):
            # Get the chosen file to move
            target_file = files_to_move[choice - 1]

            # Get the target directory from the user
            target_directory = input(f'Enter the filepath of the directory you wish to move to: ')

            # Check if the target_directory is a valid directory
            if os.path.isdir(target_directory):
                # Check if the target file already exists in the target directory
                target_file_path = os.path.join(target_directory, target_file)
                if not os.path.exists(target_file_path):
                    # Construct the full path of the source file
                    source_file_path = os.path.join(source_dir, target_file)
                    try:
                        # Move the file to the target directory
                        shutil.move(source_file_path, target_file_path)
                        print(f"File '{target_file}' moved successfully to {target_directory}.")
                    except OSError as e:
                        print(e)
                        print('====================')
                else:
                    print(f"File '{target_file}' already exists in the target directory.")
            else:
                print(f'Not a directory: {target_directory}')
        else:
            print("Invalid choice. Please choose a valid file number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    print('====================')


# Function to copy a file from the source directory to a target directory
def copy_file(source_dir):
    # List of files to copy
    files_to_copy = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    if not files_to_copy:
        print(f'No files to copy in {source_dir}')
        print('====================')
        return

    # Print available files for copying
    print('Files available for copying:')
    for i, file in enumerate(files_to_copy, 1):
        print(f"{i}. {file}")

    # Ask the user to choose a file to copy
    try:
        choice = int(input("Enter the number of the file you wish to copy: "))
        if 1 <= choice <= len(files_to_copy):
            # Get the chosen file to copy
            target_file = files_to_copy[choice - 1]

            # Get the target directory from the user
            target_directory = input(f'Enter the filepath of the directory you wish to copy to: ')

            # Check if the target_directory is a valid directory
            if os.path.isdir(target_directory):
                # Check if the target file already exists in the target directory
                target_file_path = os.path.join(target_directory, target_file)
                if not os.path.exists(target_file_path):
                    # Construct the full path of the source file
                    source_file_path = os.path.join(source_dir, target_file)
                    try:
                        # Copy the file to the target directory
                        shutil.copy(source_file_path, target_file_path)
                        print(f"File '{target_file}' copied successfully to {target_directory}.")
                    except OSError as e:
                        print(e)
                        print('====================')
                else:
                    print(f"File '{target_file}' already exists in the target directory.")
            else:
                print(f'Not a directory: {target_directory}')
        else:
            print("Invalid choice. Please choose a valid file number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    print('====================')


# Function to delete a file from a directory
def delete_file(source_dir):
    # List of files in the source directory
    files_to_delete = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    if files_to_delete:
        # List available files to delete
        print('Files available for deletion:')
        for i, file in enumerate(files_to_delete, 1):
            print(f"{i}. {file}")

        # Ask the user to choose which file to delete
        try:
            choice = int(input("Enter the number of the file you wish to delete: "))
            if 1 <= choice <= len(files_to_delete):
                # Construct the full path of the chosen file
                file_to_delete = os.path.join(source_dir, files_to_delete[choice - 1])

                # Confirm with the user before deleting
                confirmation = input(f"Are you sure you want to delete '{files_to_delete[choice - 1]}'? (yes/no): ")
                if confirmation.lower() == "yes":
                    os.remove(file_to_delete)
                    print(f"File '{files_to_delete[choice - 1]}' has been deleted.")
                else:
                    print(f"File '{files_to_delete[choice - 1]}' was not deleted.")
            else:
                print("Invalid choice. Please choose a valid file number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("No files to delete in the directory.")