liste1 = [ "string", 1 , 1.7,{"x":"z"},["a",[[[]]]]]

liste1.append("deneme")
print(liste1)
liste1.pop(0)
print(liste1)
liste1.remove(1.7)
print(liste1)
print(liste1.count("1"))
print(liste1.index(1))

liste2 = [4,6,2,1,46,11]
liste2.sort(reverse=True)
print(liste2)
liste2.sort()
print(liste2)
liste2.insert(1,99)
print(liste2)
liste2.extend([9,8,66,4,3,2])
print(liste2)
print(liste2[9])
kopyalist = liste2.copy()
print(kopyalist)


print(liste2[3:])
print(liste2[:3])
print(liste2[1:3])
print(liste2[-1])