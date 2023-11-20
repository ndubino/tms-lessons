# 1
def hello_world():
    print('Hello world')


hello_world()


# 2
def hello_world():
    return 'Hello world'


print(hello_world())


#3
def hello():
    name = input()
    print(f'Hello {name}')

hello()


#4
def hello():
    name = input()
    return (f'Hello {name}')

print(hello())
