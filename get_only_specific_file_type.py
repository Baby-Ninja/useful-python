import sys
import os 

directory = '/dirpath'
test = os.listdir(directory)

for name in test:
    if item.endswith('.jpg'):
        os.remove(os.path.join(directory, item))