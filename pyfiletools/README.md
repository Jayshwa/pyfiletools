# pyfiletools

Welcome to the pyfiletools project repository! This collection of Python scripts and tools is designed to solidify my understanding of the `os`, `shutil`, and `getpass` modules. These modules are essential for file system interaction, data manipulation, and secure user input in Python.

**Project Goals**

* **Educational:** Deepen my understanding of Python's file and directory management capabilities.
* **Practical:** Develop useful tools for system administration and automation tasks.
* **Modular:** Create reusable scripts that can be integrated into larger projects.

**Key Features**

* **`os` Module Exploration:**
    * Scripts demonstrating various `os` module functions for file and directory operations.
    * Examples include listing files, creating directories, changing directories, and retrieving file metadata.
* **`shutil` Module Utilization:**
    * Tools showcasing the `shutil` module's capabilities for high-level file operations.
    * Features include copying, moving, and deleting files and directories.
* **`getpass` Module Implementation:**
    * Examples of secure password input and user authentication using the `getpass` module.
    * Focus on handling sensitive information securely.
* **Git integration:**
    * Scripts showcasing the `subprocess` module to run git commands.

**Getting Started**

1.  **Clone the Repository:**
    ```bash
    git clone [repository URL]
    cd pyfiletools
    ```
2.  **Explore the Scripts:**
    * Each script is self-contained and documented with comprehensive comments.
    * Run the scripts directly using Python.
    * Example: `python list_files.py`
3.  **Experiment and Adapt:**
    * Feel free to modify the scripts to suit your specific needs.
    * Use the provided examples as a foundation for your own projects.

**Example Usage**

```python
#Example of using the make_directory.py script.
import make_directory
make_directory.make_directory('new_directory')
