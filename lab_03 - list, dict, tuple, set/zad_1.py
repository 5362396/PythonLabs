original_list = list(range(1, 11))
new_list = list()

if __name__ == '__main__':
    print(original_list, 'ID listy:', id(original_list))
    print(new_list, 'ID listy:', id(new_list))

for i in range(len(original_list) // 2):
    new_list.append(original_list.pop(5))

if __name__ == '__main__':
    print(original_list, 'ID listy:', id(original_list))
    print(new_list, 'ID listy:', id(new_list))
