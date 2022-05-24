import itertools


def dots(text: str):
    if len(text) < 1:
        return []
    for i in itertools.product(['', '.'], repeat=len(text) - 1):
        result = text[0]
        for k, v in zip(i, text[1:]):
            result += k + v
        yield result


if __name__ == "__main__":
    print(list(dots('')))
