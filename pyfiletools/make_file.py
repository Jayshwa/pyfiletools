import os

def create_file(file_name):
    valid_extensions = [".txt", ".docx", ".doc", ".md", ".odt", ".rtf", ".pdf", ".pptx", ".ppt",".py", ".js", ".html", ".css", ".cpp", ".java",]  # Add more valid extensions as needed
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

