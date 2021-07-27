class MyClass:
    def __format__(self, format_spec, x=None) -> str:
        return f"Did you know{x}: {format_spec=!r}"


def main():
    x = 5
    print(f'{MyClass():%x}')


if __name__ == '__main__':
    main()
