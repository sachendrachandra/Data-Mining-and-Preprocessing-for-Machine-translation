import os, shutil

dict_extensions = {
    'python_extensions' : ('.py')
}


folderpath = input('enter folder path : ')
files = []
folder_name='pythonFiles'
folder_path = os.path.join(folderpath, folder_name)
os.mkdir(folder_path)
def file_finder(folder_path, file_extensions):
    for file in os.listdir(folder_path):
        try:

            if not os.path.isfile(os.path.join(folder_path, file)):
                file_finder(os.path.join(folder_path,file),file_extensions)
            for extension in file_extensions:
                if file.endswith(extension):
                    files.append(os.path.join(folder_path,file))
        except:
            pass
    return files

for extension_type, extension_tuple in dict_extensions.items():
    # folder_name = extension_type.split('_')[0] + 'Files'
    # folder_path = os.path.join(folderpath, folder_name)
    # os.mkdir(folder_path)
    for item in file_finder(folderpath, extension_tuple):
        # # item_path = os.path.join(folderpath,item)
        # item_path = os.path.dirname(os.path.abspath(item))
        base = os.path.basename(item)
        item_new_path = os.path.join(folder_path,base)
        try:
            shutil.copy(item,item_new_path)
        except:
            pass
        print(item)