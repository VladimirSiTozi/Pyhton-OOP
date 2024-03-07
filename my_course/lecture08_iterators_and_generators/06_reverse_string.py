def reverse_text(txt):
    for char in txt[::-1]:
        yield char


for char in reverse_text("step"):
    print(char, end='')