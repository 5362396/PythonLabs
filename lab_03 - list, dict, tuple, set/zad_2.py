import zad_1

zad_1.original_list.extend(zad_1.new_list)
zad_1.original_list.insert(0, 0)
print(zad_1.original_list)

list_copy = zad_1.original_list.copy()
list_copy.sort(reverse=True)
print(list_copy)
