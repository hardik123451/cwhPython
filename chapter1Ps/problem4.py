import os

def print_directory_contents(directory_path):
    try:
        # Get a list of entries in the directory
        entries = os.listdir(directory_path)
        
        # Print each entry
        for entry in entries:
            print(entry)
    
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Permission denied: unable to access {directory_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the directory you want to list
directory_path = '.'

# Call the function
print_directory_contents(directory_path)
