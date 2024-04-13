def file_merger(files: list, new_file: str) -> None:
    with open(new_file, 'w', newline='') as newfile:
        for f in files:
            with open(f, 'r', newline='') as file:
                for row in file:
                    newfile.write(row)


file_merger(['zamowienia_polska.csv', 'zamowienia_niemcy.csv'], 'zamowienia_merged.csv')
