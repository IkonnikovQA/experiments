def hello(name):
    if name == '':
        print('Hello world')
    else:
        print(f'Hello {name}')

def hello2(name):
    if name:
        print(f'Hello {name}')
    else:
        print('Hello world')

a = 1

if a:
    print('xxx')

print('Enter two numbers, each less than 10')
a = int(input('first number: '))
b = int(input('second number: '))

def divide(x, y):
    if x > 10 or y > 10:
        result = 'the number does not meet the requirements'
    elif y == 0:
        result = "don't divide by 0"
    else:
        result = x / y
    return result

def devide2(x, y):
    if x > 10 or y > 10:
        return 'the number does not meet the requirements'

    if y == 0:
        return "don't divide by 0"
    return x / y

lst = [1, 2, 3, 4, 5, 6, 7]

new_lst = []
for x in lst:
    new_lst.append(x * 2)

new_lst = [x * 2 for x in lst]

new_lst = []
for x in lst:
    if x % 2 == 0:
        new_lst.append(x)

new_lst = [x for x in lst if x % 2 == 0]

print(new_lst)

i = 0
while i < 20:
    print('hello')
    i += 1

for i in range(20):
    print(i, 'hello')

# tlp = ('one', 'two', 'three')
# var1 = tpl[0]
# var2 = tpl[1]
# var3 = tpl[2]
#
# var1, var2, var3 = tpl
# print(var2)

def print_text_with_exclamation_at_the_end(text):
    print(f'{text}!')

print_text_with_exclamation_at_the_end('hello')

my_print = print_text_with_exclamation_at_the_end

my_print('hi')