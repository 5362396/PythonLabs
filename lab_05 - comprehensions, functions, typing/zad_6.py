def sort_str(*texts: str) -> list[str]:
    return sorted(texts)


print(sort_str())
print(sort_str('w tym', 'przypadku', 'nie trzeba', 'robić', 'oddzielnego', 'case`a', 'dla braku', 'argumentów'))
