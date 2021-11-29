from os import rename, getcwd, listdir, path

current_folder = getcwd()
for folder_name in listdir(current_folder):
    if path.isfile(folder_name):
        continue

    number = 1
    for file_name in listdir(folder_name):
        rename(
                f'{current_folder}\\{folder_name}\\{file_name}',
                f'{current_folder}\\{folder_name}-{number}{file_name[-4:]}')
        number +=1
