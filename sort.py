import os

BOOK_1 = "1.txt"
BOOK_2 = "2.txt"
BOOK_3 = "3.txt"
BOOK_4 = "4.txt"
BOOK_DIR = "sorted"
ROOT_PATH = os.getcwd()
FUUL_PATH_1 = os.path.join(ROOT_PATH, BOOK_DIR, BOOK_1)
FUUL_PATH_2 = os.path.join(ROOT_PATH, BOOK_DIR, BOOK_2)
FUUL_PATH_3 = os.path.join(ROOT_PATH, BOOK_DIR, BOOK_3)
FUUL_PATH_4 = os.path.join(ROOT_PATH, BOOK_DIR, BOOK_4)

len_list =[]
len_dict ={}

with open (FUUL_PATH_1, encoding = 'utf-8') as book_1:
    b_1 = len(book_1.readlines())
    len_list.append(b_1)

with open (FUUL_PATH_2, encoding='utf-8') as book_2:
    b_2 = len(book_2.readlines())
    len_list.append(b_2)

with open (FUUL_PATH_3, encoding='utf-8') as book_3:
    b_3 = len(book_3.readlines())
    len_list.append(b_3)

len_dict[FUUL_PATH_1] = (b_1, '1.txt')
len_dict[FUUL_PATH_2] = (b_2, '2.txt')
len_dict[FUUL_PATH_3] = (b_3, '3.txt')
len_list.sort()
# print(len_list)
# print(len_dict)

with open (FUUL_PATH_4, "a") as book_4:
    for n in len_list:
        for k, v in len_dict.items():
            if v[0] == n:
                book_4.write(f'{v[1]}\n')
                book_4.write(f'{v[0]}\n')
                with open(k, encoding='utf-8') as book_1:
                    book = book_1.read()
                    book_4.write(f'{book} \n')










