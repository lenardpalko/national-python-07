# user_input = input('Give me a number:')
#
# try:
#     #user_number = int(user_input)
#     #print(another_var)
#     print([][6])
# except ValueError as num_exceptie:
#     print('Value error', num_exceptie)
# except NameError as e:
#     print('Name error', e)
# except IndexError as e:
#     print("Index exception")
# finally:
#     print('THIS CODE WILL RUN ANYWAY')
#
# print("Next line of code")

# user_input = None
# while user_input == None or type(user_input) is not int:
#     user_input = input("Give me a number")
#
#     try:
#         user_input = int(user_input)
#     except ValueError as e:
#         print('Input is not an int!! Try again...')

# l = [1, 2, 3]
# def f():
#     l = ['a', 'f']
#     print(l)
#     lf = [1, 2, 3]
#     global glf
#     glf = ['x', 'c']
#
# print(l)
# f()
# print(glf)
# print(lf)

# print = 'doar un string'
# print('print')
#
# print = __builtins__.print
# print('test')

# import module as my_module
# from module import func, variabila
#
# if __name__ == '__main__':
#     print(variabila)
#     func()
#
#     print('This is the main module.')

# from my_package.my_module import vars1 as variabila1
# from my_package.my_other_module import *
#
# if __name__ == '__main__':
#     print(variabila1)
#     print(var2)
#     print('This is the main module.')

# my_lambda = lambda x, y: x + y
# def my_lambda(x, y):
#     return x + y

# def a(x):
#     return x + x
#
# def b(x):
#     return x * x
#
# print(id(a))
# print(id(b))
# print(id(lambda x: x+x))
# print(id(lambda x: x*x))

my_dict_list = [
    {
        'nume': 'Lenny',
        'varsta': 34
    },
    {
        'nume': 'Simona Halep',
        'varsta': 30
    }
]


def get_key(my_dict):
    return my_dict.get('varsta')


my_dict_list.sort(key=get_key)

my_dict_list.sort(key=lambda d: d.get('varsta'))
print(my_dict_list)
sorted(my_dict_list, key=lambda d: d.get('varsta'))
