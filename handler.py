import os
import sys

try:
    my_path = sys.argv[1]
    for root, dirs, files in os.walk(my_path, topdown=False):
        for name in files:
            print(os.path.join(my_path, root, name))
except IndexError:
    print('Directory is not specified')
