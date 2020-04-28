import sys
import argparse

# print(sys.argv)
# if len(sys.argv) < 2:
#     print("Аргументов нет")
# elif len(sys.argv) > 3:
#     print("Аргументов много")
# else:
#     print(f"Hello {sys.argv[1]}. Count: {sys.argv[2]}")


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

    # if namespace.file_list:
    #     for file in namespace.file_list:
    #         for line in file:
    #             print(line, end="")
    # else:
    #     print("Файлов нет")




