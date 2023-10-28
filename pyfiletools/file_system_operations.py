import os
import query_name, find_directory, find_files, make_directory, list_file_perms as lfp, change_directory, list_subdirectories, remove_directories, mod_files, make_file, list_files, git_commands
import getpass

# Function to navigate directories
def navigate_directories(base_dir=None):
    """
    Navigate directories based on user input and perform search or modify actions.

    :param base_dir: The base directory to start searching from (default is the current working directory).
    """
    if base_dir is None:
        base_dir = os.getcwd()

    while True:
        print('Enter an action:')
        for command in commands:
            print(command)
        action_plan = input(f"")
        print('====================')

        # Search for a directory in the user's home directory
        if action_plan.lower() == 'searchd':
            # Get the currently logged-in username
            current_user = getpass.getuser()

            # Create the path to the user's directory
            user_path = os.path.join("/Users", current_user)

            check_directory = input('Enter a directory to search for: ')
            directory_path = find_directory.find_directory(check_directory, user_path)

            if directory_path:
                print(f'{check_directory} was found at path: {directory_path}')

        if action_plan.lower() == 'searchf':
            # Get the currently logged-in username
            current_user = getpass.getuser()

            # Create the path to the user's directory
            user_path = os.path.join("/Users", current_user)

            check_file = input('Enter a file to search for: ')
            directory_path = find_files.find_files(check_file, user_path)

            if directory_path:
                print(f'{check_directory} was found at path: {directory_path}')

        # Handle modify actions (create or remove directories)
        elif action_plan.lower() in ['modify', 'mod']:
            action = input(f"Enter an action {commands}")
            action_parts = action.split(' ')

            # Check for the proper format for modify actions
            if len(action_parts) == 2:
                if action_parts[0].lower() == 'mkdir':
                    make_directory.make_directory(action_parts[1])
                    print(f'Directory "{action_parts[1]}" created successfully.')
                    print('====================')
                elif action_parts[0].lower() == 'rmdir':
                    remove_directories.remove_directory(action_parts[1])
                    print(f'Directory "{action_parts[1]}" deleted successfully.')
                    print('====================')
            elif action_parts[0].lower().startswith('mfile'):
                mod_files.move_file(os.getcwd())
            elif action_parts[0].lower().startswith('cfile'):
                mod_files.copy_file(os.getcwd())
            elif action_parts[0].lower().startswith('dfile'):
                mod_files.delete_file(os.getcwd())
            elif action_parts[0].lower().startswith('git'):
                print(f'Commands are not ready to be used.')
            
            elif action_parts[0].lower() in ['mkfile', 'touch']:
                new_file_name = input("Enter the name of the file with a valid extension (e.g., .txt, .py, .csv): ")
                make_file.create_file(new_file_name)
                print('====================')

            else:
                print(f"Invalid input. Please use {commands}: ")
                print('====================')

        # List subdirectories in the current directory
        elif action_plan.lower() in ['listdir', 'lsd', 'lsdir']:
            list_subdirectories.list_subdirectories()

        elif action_plan.lower() in ['list', 'ls']:
            list_files.list_files_in_directory(os.getcwd())

        # List all files in the current directory with their permissions
        elif action_plan.lower() == 'ls -a':
            files = os.listdir(os.getcwd())
            files = [file for file in files if os.path.isfile(os.path.join(os.getcwd(), file))]
            for file in files:
                lfp.list_file_permissions(file)
            

        # Change the current working directory based on the provided directory path
        elif action_plan.lower().startswith('cd'):
            cd_location = action_plan.split(' ')
            if len(cd_location) >= 2:
                target_dir = cd_location[1]
                change_directory.change_directory(target_dir)
            else:
                print('Directory to navigate to not specified.')
                print('====================')

        # Check if the user input is to quit or exit the program
        elif action_plan.lower() in ['quit', 'exit']:
            # If 'quit' or 'exit' is entered, terminate the program
            quit()


        # Display the current working directory
        elif action_plan.lower() == 'cwd':
            try:
                print(f'Current working directory: {os.getcwd()}')
                print('====================')
            except OSError as e:
                print(f'Error: {e}')
                print('====================')

        else:
            print(f"Invalid input. Please enter {(i for i in commands)}")
            print('====================')

if __name__ == "__main__":

    commands = ["Navigation: 'searchd', 'searchf' , 'cd [file]', 'ls', 'ls-a', 'lsdir', 'listdir', 'lsd', 'cwd' ", "Modify: 'Mod', 'Modify'// 'mkdir', 'mkfile', 'mfile'", "Quit // 'quit', 'exit'", "Git Commands: 'git'"]
    # Get the user's name and then navigate directories
    query_name.return_name(input('What is your name?: '))
    navigate_directories()
