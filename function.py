# def test():
#     pass

def test():
    print("this is function")
test()
test()+"annadn" #gives error  here print is NoneType


def test():
    return "this is return"
print(test()+"  anand")


def test():
    return 1,2,"anand",[1,2,3]
print(test()) #(1, 2, 'anand', [1, 2, 3])


l1 = ["anand", "kishor", "gupta"]
for i in l1:
    if (i == "gupta"):
        break
    print(i)
else:
    print("else code ")


print(list(range(5)))