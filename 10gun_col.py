from collections import Counter

data = ["ziya","ziya","ahmet","mehmet","ahmet","cihan","ihsan","mehmet"]
data = ["ziya","ziya","ahmet","mehmet","ahmet","cihan","ihsan","mehmet","ilter"]

data = Counter(data)
print(data.most_common(2))

z = Counter(a=1,b=5,ihsan=9)
print(list(z.elements()))
data3 = Counter("Mustafa")
print(data3.most_common(1))
print(list(z))