# import os


def main() -> None:
    """
    main
    """
    print("do some work.")
    print(add(1, 2))
    show()


def add(n1: int, n2: int) -> int:
    """
    n1 plus n2
    """
    return n1 + n2


def show() -> None:
    print("hello")


if __name__ == "__main__":
    main()
