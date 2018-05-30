from random import randint

a = [i for i in range(10)]

print(a)

for i in a:
    print(i)

for x in iter(a):
    print("ITER:{}".format(x))




# for _ in iter(a):
#     print(_)