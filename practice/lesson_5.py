def hello_world():
    print('Hello World')


hello_world()


# 2

def hello_world():
    return 'Hello World'


print(hello_world())


# 3
def hello(name):
    print('Hello {}'.format(name))


hello('Nikita')


# 4
def hello(name):
    return f'Hello {name}'


x = hello('Nikita')
print(x)
