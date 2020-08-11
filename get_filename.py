import os 
import os.path 

dir_path ='../dataset'
for path, subdirs, files in os.walk(dir_path):
    for name in files:
        path_name =os.path.join(path, name)
        with open('file_name.csv', 'w') as f:
            f.write('{}'.format(path_name))

