import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# List files and directories in the current path
contents = os.listdir('.')
print(f"Contents of current directory: {contents}")

# Check if a path exists
file_exists = os.path.exists("my_file.txt")
print(f"Does 'my_file.txt' exist? {file_exists}")