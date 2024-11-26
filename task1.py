def strict(func):
    def wrapper(*args):
        allowed_types = {int, float, str, bool}
        annotations = func.__annotations__
        for annot in annotations.values():
            if annot not in allowed_types:
                raise TypeError(f'Аннотация с этим типом данных - {annot} не допускается')
            
        for annotation_key, arg in zip(annotations.keys(), args):
            if not isinstance(arg, annotations[annotation_key]):
                raise TypeError
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: float):
    return a + b


if __name__ == '__main__':
    print(sum_two(3, 3.14))