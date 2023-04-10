from utils import *


def main():
    data = srted(filtr(get_data()))
    for operation in data[:5]:
        print(format_data(operation))
        print()

if __name__ == "__main__":
    main()
