import os
import shutil


# Creates a folder that is named after the extension of the file
def create_folder(path: str, extension: str) -> str:
    folder_name: str = extension[1:]  # gets everything past the dot (.)
    folder_path: str = os.path.join(path, folder_name)  # joins the path to the folder

    if not os.path.exists(folder_path):  # checking if the folder does not already exist
        os.makedirs(folder_path)  # if the folder does not exist, this will automatically create one

    return folder_path


# Sorting files based on a given path
def sort_files(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path):
        # os.walk slowly walks through every dir and file in that path
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)  # creating the file path
            extension: str = os.path.splitext(filename)[1]  # creating the extension

            if extension:  # if there is an extension
                target_folder: str = create_folder(source_path, extension)  # creating target folder
                target_path: str = os.path.join(target_folder, filename)
                # creating target path -> finding filename in the target folder
                shutil.move(file_path, target_path)  # moving the files in the folder


# removing empty folders
def remove_empty_folder(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        # topdown -> the process starts with root directory and making the way up to subfolders. Topdown False reverses the process
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):  # if it doesn't contain anything it will remove it
                os.rmdir(folder_path)  # rmdir = remove directory


def main():
    user_input: str = input('Please provide a file path to sort: ')

    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folder(user_input)
        print('Files sorted successfully!')
    else:
        print('Invalid path, please provide a valid file path.')


if __name__ == '__main__':
    main()

# create a prompt or even to create a tk app to allow the user to select the folder using a button
