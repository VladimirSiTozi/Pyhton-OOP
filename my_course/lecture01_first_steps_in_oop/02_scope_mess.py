x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x  # added

        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # added

        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
