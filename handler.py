import os
import sys
import hashlib


####################### Asker ###########################
if len(sys.argv) < 2:
    print('Directory is not specified')
    sys.exit(1)
else:
    my_dict = {}
    replicas_list = []
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


####################### Dictionary creater ###########################
    for root, dirs, files, in os.walk(my_path, topdown=False):
        for name in files:
            if name.endswith(format):
                file_size = os.path.getsize(os.path.join(root, name))
                file_path = os.path.join(root, name)
                with open(file_path, 'rb') as f:
                    md5 = hashlib.md5(f.read()).hexdigest()
                my_dict.setdefault(file_size, {})
                my_dict[file_size].setdefault(md5, {})
                if my_dict[file_size][md5] == {}:
                    my_dict[file_size][md5] = []
                my_dict[file_size][md5].append(file_path)


####################### Printer ###########################
    for i in sorted(my_dict.keys(), reverse=sorting):
        print('\n' + str(i) + ' bytes')
        for key, value in my_dict[i].items():
            for element in value:
                print(element)


####################### Checker ###########################
    while True:
        replica_check = input('\nCheck for duplicates?\n')
        if replica_check.lower() == 'yes' or replica_check.lower() == 'no':
            break
        else:
            print('Wrong option')
    if replica_check.lower() == 'yes':
        for key, value in sorted(my_dict.items(), reverse=sorting):
            flag = True
            for hash, hash_list in value.items():
                if len(hash_list) > 1:
                    if flag:
                        print('\n' + str(key) + ' bytes\nHash: ' + hash)
                        flag = False
                    else:
                        print('Hash: ' + hash)
                    for i in sorted(hash_list):
                        replicas_list.append(i)
                        print(f'{len(replicas_list)}. {i}')
    else:
        sys.exit()


####################### Deleter ###########################
    while True:
        delete_check = input('\nDelete files?\n')
        if delete_check.lower() == 'yes' or delete_check.lower() == 'no':
            break
        else:
            print('Wrong option')
    if delete_check.lower() == 'yes':
        while True:
            file_numbers = input('Enter file numbers to delete:\n')
            delete_list = file_numbers.split()
            flag = True
            if len(file_numbers) == 0:
                flag = False
            for element in delete_list:
                if not element.isdigit():
                    flag = False
            if flag:
                break
            else:
                print('Wrong format')
        summa = 0
        for i in range(1, len(replicas_list) + 1):
            if str(i) in delete_list:
                summa += os.path.getsize(replicas_list[i - 1])
                os.remove(replicas_list[i - 1])
        print(f'Total freed up space: {summa} bytes')
    else:
        sys.exit()
