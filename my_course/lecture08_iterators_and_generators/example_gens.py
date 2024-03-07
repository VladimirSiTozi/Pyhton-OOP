def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is second first')
    yield n

    n += 1
    print('This is third first')
    yield n


for num in my_gen():
    print(num)