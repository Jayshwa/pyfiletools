import os

def list_file_permissions(file_path):
    """
    Lists the permissions of a file in a human-readable format.

    :param file_path: The path of the file to list permissions for.
    :type file_path: str
    :raises OSError: If the file does not exist or cannot be accessed.
    """
    try:
        # Get the file's permission mode as an integer
        mode = os.stat(file_path).st_mode

        # Convert the integer mode to a human-readable format (octal)
        permission_string = format(mode, 'o')[-3:]

        # Map numeric permission values to their corresponding letters
        permissions = {
            '0': '---',
            '1': '--x',
            '2': '-w-',
            '3': '-wx',
            '4': 'r--',
            '5': 'r-x',
            '6': 'rw-',
            '7': 'rwx'
        }

        # Convert numeric permission values to letters
        permission_str = ''.join(permissions[digit] for digit in permission_string)

        print(f"File: {file_path}")
        print(f"Permissions: {permission_str}")
        print('====================')
    except OSError as e:
        print(f"Error: {e}")
        print('====================')

# Example usage (demonstration)
if __name__ == "__main__":
    # Create a test file
    test_file = "test_permissions.txt"
    try:
        with open(test_file, "w") as f:
            f.write("Test content")
        print(f"Created test file '{test_file}' for testing.")
    except OSError as e:
        print(f"Failed to create test file: {e}")
        test_file = None

    if test_file:
        # List the permissions of the test file
        list_file_permissions(test_file)

        # Change the permissions of the test file (e.g., make it executable)
        try:
            os.chmod(test_file, 0o755)  # Set permissions to rwxr-xr-x
            print(f"Changed permissions of '{test_file}' to 755.")
            list_file_permissions(test_file) #Print the new permissions.
        except OSError as e:
            print(f"Failed to change permissions: {e}")

        # Clean up the test file
        try:
            os.remove(test_file)
            print(f"Test file '{test_file}' cleaned up.")
        except OSError as e:
            print(f"Failed to clean up test file: {e}")
