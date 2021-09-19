import os
import sys

if len(sys.argv) < 2:
    print('Directory is not specified')
    sys.exit(1)
else:
    my_dict = {}
    my_path = sys.argv[1]
    format = input('Enter file format:\n')
    print('Size sorting options:\n1. Descending\n2. Ascending')
    while True:
        sorting = int(input('Enter a sorting option:\n'))
        if sorting == 1:
            sorting = True
            break
        elif sorting == 2:
            sorting = False
            break
        else:
            print('Wrong option')

    for root, dirs, files, in os.walk(my_path, topdown=False):
        for name in files:
            if name.endswith(format):
                file_size = os.path.getsize(os.path.join(root, name))
                file_path = os.path.join(root, name)
                try:
                    my_dict[file_size].append(file_path)
                except KeyError:
                    my_dict[file_size] = [file_path]

for key in sorted(my_dict.keys(), reverse=sorting):
    if len(my_dict[key]) > 1:
        print('\n' + str(key) + ' bytes')
        for item in my_dict[key]:
            print(item)
