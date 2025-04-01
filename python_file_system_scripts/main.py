import os
import getpass

import change_directory
import find_directory
import find_files
import git_commands
import list_file_perms
import list_files
import list_subdirectories
import make_directory
import make_file
import mod_files
import query_name
import remove_directories

def main():
    """
    Main function to interact with the pyfiletools suite.
    """
    name = input('What is your name?: ')
    query_name.return_name(name)

    while True:
        print("\nChoose a tool to run:")
        print("1. Change Directory (cd)")
        print("2. Find Directory (searchd)")
        print("3. Find Files (searchf)")
        print("4. Git Commands (git)")
        print("5. List File Permissions (ls -a)")
        print("6. List Files (ls)")
        print("7. List Subdirectories (lsdir)")
        print("8. Make Directory (mkdir)")
        print("9. Make File (mkfile)")
        print("10. Modify Files (move, copy, delete)")
        print("11. Remove Directory (rmdir)")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            target_dir = input("Enter the directory to change to: ")
            change_directory.change_directory(target_dir)
        elif choice == "2":
            check_directory = input("Enter a directory to search for: ")
            root_directory = os.path.join("/Users", getpass.getuser())
            find_directory.find_directory(check_directory, root_directory)
        elif choice == "3":
            check_file = input("Enter a file to search for: ")
            root_directory = os.path.join("/Users", getpass.getuser())
            find_files.find_files(check_file, root_directory)
        elif choice == "4":
            git_commands.display_menu()
            git_choice = input("Enter your git command choice: ")
            if git_choice == '1':
                git_commands.init_repository()
            elif git_choice == '2':
                repo_url = input('Enter the git repository URL: ')
                git_commands.clone_repository(repo_url)
            elif git_choice == '3':
                git_commands.get_status()
            elif git_choice == '4':
                file_name = input('Enter the file name to add: ')
                git_commands.add_file(file_name)
            elif git_choice == '5':
                commit_message = input('Enter the commit message: ')
                git_commands.commit_changes(commit_message)
            elif git_choice == '6':
                git_commands.pull_changes()
            elif git_choice == '7':
                git_commands.push_changes()
            else:
                print('Invalid git command choice.')
        elif choice == "5":
            list_files.list_files_in_directory(os.getcwd())
            files = os.listdir(os.getcwd())
            files = [file for file in files if os.path.isfile(os.path.join(os.getcwd(), file))]
            for file in files:
                list_file_perms.list_file_permissions(file)
        elif choice == "6":
            list_files.list_files_in_directory(os.getcwd())
        elif choice == "7":
            list_subdirectories.list_subdirectories()
        elif choice == "8":
            dir_name = input("Enter the directory name to create: ")
            make_directory.make_directory(dir_name)
        elif choice == "9":
            file_name = input("Enter the file name to create: ")
            make_file.create_file(file_name)
        elif choice == "10":
            action = input("Enter 'move', 'copy', or 'delete': ")
            if action.lower() == 'move':
                mod_files.move_file(os.getcwd())
            elif action.lower() == 'copy':
                mod_files.copy_file(os.getcwd())
            elif action.lower() == 'delete':
                mod_files.delete_file(os.getcwd())
            else:
                print("Invalid action.")
        elif choice == "11":
            dir_name = input("Enter the directory name to remove: ")
            remove_directories.remove_directory(dir_name)
        elif choice == "12":
            print("Exiting pyfiletools.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()
