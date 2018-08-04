def metod1():
    data = []
    for i in range(0,1000):
        data.append(i)
    return data

def metod2():
    data = []
    for i in range(0,2):
        data.append(i)
        yield i
        yield data


for i in metod2():
    print(i)
