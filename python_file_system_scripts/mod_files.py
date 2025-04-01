import os
import shutil

# Function to move a file from the source directory to a target directory
def move_file(source_dir):
    """
    Moves a file from the source directory to a target directory.

    :param source_dir: The source directory containing the file to move.
    :type source_dir: str
    :raises FileNotFoundError: If the source directory does not exist.
    :raises ValueError: If the user input is invalid.
    :raises OSError: If an error occurs during the move operation.
    """
    try:
        files_to_move = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

        if not files_to_move:
            print(f'No files to move in {source_dir}')
            print('====================')
            return

        print('Files available for moving:')
        for i, file in enumerate(files_to_move, 1):
            print(f"{i}. {file}")

        try:
            choice = int(input("Enter the number of the file you wish to move: "))
            if 1 <= choice <= len(files_to_move):
                target_file = files_to_move[choice - 1]
                target_directory = input(f'Enter the filepath of the directory you wish to move to: ')

                if os.path.isdir(target_directory):
                    target_file_path = os.path.join(target_directory, target_file)
                    source_file_path = os.path.join(source_dir, target_file)
                    if not os.path.exists(target_file_path):
                        shutil.move(source_file_path, target_file_path)
                        print(f"File '{target_file}' moved successfully to {target_directory}.")
                    else:
                        print(f"File '{target_file}' already exists in the target directory.")
                else:
                    print(f'Not a directory: {target_directory}')
            else:
                print("Invalid choice. Please choose a valid file number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        print('====================')
    except FileNotFoundError:
        print(f"Source directory '{source_dir}' not found.")
        print('====================')
    except OSError as e:
        print(f"Error during move operation: {e}")
        print('====================')

# Function to copy a file from the source directory to a target directory
def copy_file(source_dir):
    """
    Copies a file from the source directory to a target directory.

    :param source_dir: The source directory containing the file to copy.
    :type source_dir: str
    :raises FileNotFoundError: If the source directory does not exist.
    :raises ValueError: If the user input is invalid.
    :raises OSError: If an error occurs during the copy operation.
    """
    try:
        files_to_copy = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

        if not files_to_copy:
            print(f'No files to copy in {source_dir}')
            print('====================')
            return

        print('Files available for copying:')
        for i, file in enumerate(files_to_copy, 1):
            print(f"{i}. {file}")

        try:
            choice = int(input("Enter the number of the file you wish to copy: "))
            if 1 <= choice <= len(files_to_copy):
                target_file = files_to_copy[choice - 1]
                target_directory = input(f'Enter the filepath of the directory you wish to copy to: ')

                if os.path.isdir(target_directory):
                    target_file_path = os.path.join(target_directory, target_file)
                    source_file_path = os.path.join(source_dir, target_file)
                    if not os.path.exists(target_file_path):
                        shutil.copy(source_file_path, target_file_path)
                        print(f"File '{target_file}' copied successfully to {target_directory}.")
                    else:
                        print(f"File '{target_file}' already exists in the target directory.")
                else:
                    print(f'Not a directory: {target_directory}')
            else:
                print("Invalid choice. Please choose a valid file number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        print('====================')
    except FileNotFoundError:
        print(f"Source directory '{source_dir}' not found.")
        print('====================')
    except OSError as e:
        print(f"Error during copy operation: {e}")
        print('====================')


# Function to delete a file from a directory
def delete_file(source_dir):
    """
    Deletes a file from the specified directory.

    :param source_dir: The source directory containing the file to delete.
    :type source_dir: str
    :raises FileNotFoundError: If the source directory does not exist.
    :raises ValueError: If the user input is invalid.
    :raises OSError: If an error occurs during the delete operation.
    """
    try:
        files_to_delete = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

        if files_to_delete:
            print('Files available for deletion:')
            for i, file in enumerate(files_to_delete, 1):
                print(f"{i}. {file}")

            try:
                choice = int(input("Enter the number of the file you wish to delete: "))
                if 1 <= choice <= len(files_to_delete):
                    file_to_delete = os.path.join(source_dir, files_to_delete[choice - 1])
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
        print('====================')
    except FileNotFoundError:
        print(f"Source directory '{source_dir}' not found.")
        print('====================')
    except OSError as e:
        print(f"Error during delete operation: {e}")
        print('====================')
