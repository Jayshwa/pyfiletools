import os
import getpass

def return_name(name):
    """
    Greets the user and displays the current working directory,
    after confirming the entered name matches the logged-in username.

    :param name: The name entered by the user.
    :type name: str
    """
    if name != getpass.getuser():
        print(f'Incorrect username entered')
        return_name(input('What is your name?: '))
    else:
        print(f'Hello {name}')
        print(f'You are currently working in: {os.getcwd()}')
        print('====================')

# Example usage (demonstration)
if __name__ == "__main__":
    return_name(input('What is your name?: '))
