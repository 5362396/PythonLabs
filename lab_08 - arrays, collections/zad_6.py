from collections import Counter, deque


def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())


print(create_kolo_fortuny(1, 2, 3, 1.23, 'koło', 'fortuny'))
