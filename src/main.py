from utils import *


def main():
    data = data_sorted(data_filter(get_data()))
    for operation in data[:5]:
        print(format_data(operation))
        print()

if __name__ == "__main__":
    main()
