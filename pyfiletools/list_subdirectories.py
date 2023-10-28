import os

# Function to list all subdirectories in the current working directory
def list_subdirectories():
    """
    List all subdirectories in the current working directory.
    """
    try:
        current_dir = os.getcwd()
        subdirectories = [d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d))]
        
        if not subdirectories:
            print("No subdirectories in the current working directory.")
            print('====================')
        elif subdirectories:
            print("Subdirectories in the current working directory:")
            for subdirectory in subdirectories:
                print(subdirectory)
            print('====================')
    except OSError as e:
        print(f'Error: {e}')
        print('====================')