import re
x = """
aofojaslkfjaslkjfjaslkfjasf312q 1234
QWEWQEQWE
safasfasfasfasfasf
*051asflasfkjaksljfaskfasfasf
asfklashfkas*/*qwqw*
şlvü=84rizelim@katibim.org!!!j53406*mgeğqro
"""

print(re.search("\D\d\d\d\D",x).group(0))
print(re.search("\W(\w+@[\w\.]+)\W",x).group(1))
