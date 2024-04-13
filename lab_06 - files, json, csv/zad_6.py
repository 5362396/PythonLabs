def reverse_words(sentence: str) -> str:
    sentence_reversed = ''
    for word in sentence.split(' '):
        sentence_reversed += word[::-1] + ' '
    return sentence_reversed


example = 'Ala ma kota'
print(reverse_words(example))
