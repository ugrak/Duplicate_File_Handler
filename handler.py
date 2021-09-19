import os
import sys

if len(sys.argv) < 2:
    print('Directory is not specified')
    sys.exit(1)
else:
    my_path = sys.argv[1]
    for root, dirs, files, in os.walk(my_path, topdown=False):
        for name in files:
            print(os.path.join(my_path, root, name))
