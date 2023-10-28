import os 

def list_file_permissions(file_path):
    try:
        # Get the file's permission mode as an integer
        mode = os.stat(file_path).st_mode

        # Convert the integer mode to a human-readable format
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