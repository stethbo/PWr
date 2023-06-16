import os
import zipfile

def pack_bin_files(folder_path, zip_file_name):
    # Create a new zip file
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Iterate over all the directories and files in the given folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.bin'):
                    # Get the absolute path of the .bin file
                    file_path = os.path.join(root, file)
                    # Add the .bin file to the zip file
                    zipf.write(file_path, arcname=file)

    print(f'All .bin files in "{folder_path}" are packed into "{zip_file_name}".')

# Specify the folder path containing the subdirectories
folder_path = '/path/to/folder'

# Specify the name of the zip file to be created
zip_file_name = 'packed_bin_files.zip'

# Call the function to pack the .bin files
pack_bin_files(folder_path, zip_file_name)
