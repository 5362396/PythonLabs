def split_types(input_list: list) -> dict:
    types_dict = dict()
    for i in input_list:
        if type(i).__name__ not in types_dict.keys():
            types_dict[type(i).__name__] = [i]
        else:
            types_dict[type(i).__name__].append(i)
    return types_dict


mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
print(split_types(mieszana))
