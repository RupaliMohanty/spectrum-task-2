def first_func(a,b):
    def second_func():
        var = a + b
        return var
    var2 = second_func()
    var3 = var2 + 5
    return var3

add = first_func(5,5)
print(add)