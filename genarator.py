"""
Создать список, в котором каждый элемент – кортеж из двух чисел.
Отсортировать данный список по убыванию вторых элементов кортежей.
"""
# from operator import getitem
a = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
#
# list_word = ["ABC", 'abcasd', 'qwe', 'qwerty', 'QWERTY']
# # print(sorted(list_word, key=lambda word: len(word)))
# # print(sorted(list_word, key=len, reverse=True))
#
# print(sorted(list_word, key=lambda word: word.lower()))
# print(sorted(list_word, key=str.lower))

#
# print(list(map(lambda item: (item[0]+1, item[1]+1),
#                a)))



# gen_exp = (word.upper() for word in s.split(" "))
#
# for word in gen_exp:
#     print(word)
#
#
# def gen_word(s, sep=' '):
#     for word in s.split(sep):
#         yield word
#
#
# def random_(seed, m=33, a=100, c=32):
#     if seed > m:
#         raise ValueError("seed > m")
#     x0 = seed
#     while True:
#         x1 = (a * x0 + c) % m
#         yield x1
#         x0 = x1
#
#
def ar_prog(start_num, step=1):
    start = start_num
    while True:
        input_ = yield start
        if input_ is None:
            start += step
        else:
            start = input_


# def count(fn):
#     fn.count = 0
#
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         fn.__dict__['count'] += 1
#         print(f"Функция {fn} вызывалась {fn.__dict__['count']} раз")
#         return result
#     return wrapper


# @count
# def my_func():
#     print("word")
#
# @count
# def my_func1():
#     print("hello")

# def cache(fn):
#     def wrapper(*args, **kwargs):
#         if args in fn.__dict__:
#             print("Взято из кеша")
#             return fn.__dict__[args]
#         else:
#             print("Вычисленно")
#             result = fn(*args, **kwargs)
#             fn.__dict__[args] = result
#             return result
#     return wrapper

def cache(fn):
    def wrapper(*args, **kwargs):
        if args not in fn.__dict__:
            fn.__dict__[args] = fn(*args, **kwargs)
        return fn.__dict__[args]
    return wrapper


def my_func():
    print(1)

my_func = cache(my_func)
print(my_func)


def cache(max_len=10):
    def cache_decorator(fn):
        def wrapper(*args, **kwargs):
            if args not in wrapper.__dict__:
                # if len(wrapper.__dict__) == 10:
                #     print(fn.__dict__)
                #     wrapper.__dict__ = dict(wrapper.__dict__.items()[1:])
                wrapper.__dict__[args] = fn(*args, **kwargs)
            return wrapper.__dict__[args]
        return wrapper
    return cache_decorator


@cache()
def pow_(a, n):
    return a ** n


if __name__ == "__main__":
    print(pow_)
    for i in range(20):
       pow_(10, i)
       print(pow_.__dict__)
