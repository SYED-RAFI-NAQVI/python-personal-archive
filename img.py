import os

path = "/Users/syedrafinaqvi/Desktop/tact1"

files = os.listdir(path)

for i in files:
    # print(type(i))
    # print(i)
    b = i.split(".")
    # print(b[1])

    if b[1] == "txt":
        continue
    print(i)


