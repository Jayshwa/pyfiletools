import os

def create_file(file_name):
    """
    Creates a new file with the specified name and a valid extension.

    :param file_name: The name of the file to create, including the extension.
    :type file_name: str
    :raises OSError: If the file cannot be created.
    """
    valid_extensions = [".txt", ".docx", ".doc", ".md", ".odt", ".rtf", ".pdf", ".pptx", ".ppt", ".py", ".js", ".html", ".css", ".cpp", ".java"]  # Add more valid extensions as needed
    extension = os.path.splitext(file_name)[1]

    if extension not in valid_extensions:
        print(f"Invalid file extension. Supported extensions: {', '.join(valid_extensions)}")
        return

    default_content = ""

    try:
        with open(file_name, 'w') as file:
            file.write(default_content)
        print(f"New file '{file_name}' created successfully.")
        print('====================')
    except OSError as e:
        print(f"Error: {e}")
        print('====================')

# Example usage (demonstration)
if __name__ == "__main__":
    # Create a valid file
    create_file("example.txt")

    # Create another valid file
    create_file("script.py")

    # Attempt to create a file with an invalid extension
    create_file("invalid.xyz")

    # Attempt to create a file in a non-existent directory (should fail)
    create_file("nonexistent_dir/test.txt")

    # Clean up created files, if possible.
    try:
        os.remove("example.txt")
        os.remove("script.py")
        print("Test files cleaned up.")
    except OSError as e:
        print(f"Failed to clean test files: {e}")
