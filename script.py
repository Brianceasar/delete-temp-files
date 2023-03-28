import os

# Get the system temporary directory
temp_dir = os.path.join(os.environ.get('TMP'), '')

# Define a variable to keep track of the total size of deleted files
total_size = 0

# Iterate through the files in the directory
for root, dirs, files in os.walk(temp_dir):
    for file in files:
        # Check if the file is a temporary file
        if file.startswith('tmp'):
            # Construct the absolute path of the file
            abs_path = os.path.join(root, file)
            try:
                # Get the size of the file
                size = os.path.getsize(abs_path)
                # Attempt to delete the file
                os.remove(abs_path)
                total_size += size
                print(f"Deleted file: {abs_path}")
            except OSError as e:
                print(f"Error deleting file: {abs_path} - {e}")
            except Exception as e:
                print(f"Error deleting file: {abs_path} - {e}")

# Convert the total size to megabytes
total_size_mb = total_size / (1024 * 1024)

if total_size_mb > 0:
    print(f"Total size freed: {total_size_mb:.2f} MB")
    print("Temporary files deleted successfully!")
else:
    print("No temporary files found.")
