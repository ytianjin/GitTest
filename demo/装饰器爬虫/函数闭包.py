def outer(func):
    def inner():
        print('11,22,33')
        res = func()
        print('77,88,99')
        return res
    return inner


def show():
    print('44,55,66')


result = outer(show)
result()