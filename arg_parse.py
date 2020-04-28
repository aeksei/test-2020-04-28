import sys
import argparse



def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--file_list', default=[], nargs='+', type=argparse.FileType)
    parser.add_argument('--print_all', action='store_const', const=True, default=False)

    return parser


if __name__ == "__main__":
    parser = create_parser()  # создаем парсер
    namespace = parser.parse_args()  # парсим аргументы
    # namespace = parser.parse_args(sys.argv[1:])  # парсим аргументы

    print(namespace)  # в переменной namespace будут находиться ваши расперсеные аргументы





