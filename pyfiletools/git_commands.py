import subprocess

def run_git_command(command):
    """
    Executes a Git command using subprocess and returns the output.

    :param command: The Git command to execute as a string.
    :type command: str
    :return: The output of the Git command as a string.
    :rtype: str
    :raises subprocess.CalledProcessError: If the Git command returns a non-zero exit code.
    """
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8").strip()

def init_repository():
    """
    Initializes a new Git repository in the current directory.
    """
    print(run_git_command("git init"))

def clone_repository(repository_url):
    """
    Clones a remote Git repository to your local machine.
    Example: clone_repository("https://github.com/your-username/your-repo.git")

    :param repository_url: The URL of the remote Git repository.
    :type repository_url: str
    """
    print(run_git_command(f"git clone {repository_url}"))

def get_status():
    """
    Displays the status of your working directory.
    """
    print(run_git_command("git status"))

def add_file(filename):
    """
    Stages changes for the next commit.
    Example: add_file("file.txt")

    :param filename: The name of the file to add to the staging area.
    :type filename: str
    """
    print(run_git_command(f"git add {filename}"))

def commit_changes(message):
    """
    Commits your staged changes to the repository with a descriptive message.
    Example: commit_changes("Initial commit")

    :param message: The commit message.
    :type message: str
    """
    print(run_git_command(f'git commit -m "{message}"'))

def pull_changes():
    """
    Fetches changes from a remote repository and merges them into your current branch.
    """
    print(run_git_command("git pull"))

def push_changes():
    """
    Pushes your local commits to a remote repository.
    """
    print(run_git_command("git push"))

def display_menu():
    """
    Displays the menu of available Git commands.
    """
    print("Available Git Commands:")
    print("1. Initialize a Git Repository")
    print("2. Clone a Remote Repository")
    print("3. Check Repository Status")
    print("4. Add File to Staging Area")
    print("5. Commit Changes")
    print("6. Pull Changes from Remote")
    print("7. Push Changes to Remote")
    print("0. Exit")

def display_command_description(command_number):
    """
    Displays the docstring of the selected Git command.

    :param command_number: The number corresponding to the Git command.
    :type command_number: str
    """
    commands = {
        "1": init_repository,
        "2": clone_repository,
        "3": get_status,
        "4": add_file,
        "5": commit_changes,
        "6": pull_changes,
        "7": push_changes,
    }
    command = commands.get(command_number)
    if command:
        print(command.__doc__)
    else:
        print("Invalid command number.")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            display_command_description(choice)
            input("Press Enter to continue...")
        else:
            print("Invalid choice. Please select a valid option.")
