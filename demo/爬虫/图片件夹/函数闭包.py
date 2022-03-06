def f1(num1):
    print(num1)
    def f2(num2):
        result = num1 + num2
        print(result)
    return f2
a = f1(1)
a(2)