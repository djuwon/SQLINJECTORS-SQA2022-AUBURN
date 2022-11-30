def fuzz(func, *args):
    try:
        result = func(*args)
        print(f'Fuzzing for {func.__name__} passed with result {result}')
    except Exception as e:
        print(f'Fuzzing for {func.__name__} failed:')
        print(e)

def main():
    funcs = []
    args = []

    for func, args in zip(funcs, args):
        fuzz(func, *args)