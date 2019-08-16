import sys
import os
import pyfiglet
import random
#
#
l = ['a', 'b', 'c']
d = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
u = ['A', 'B', 'C']
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
text = "Dicti Gen"
cprint(pyfiglet.figlet_format(text, font ="colossal") ,"green")
print('by aqswdefr746 and Kli')
print(' ')
#
#

str1 =input('Введите какие цифры будут использоваться:')
str2 =input('Введите какие маленькие буквы будут использоваться:')
str3 =input('Введите какие заглавные буквы будут использоваться:')
str4 =input('Введите какие спецсимволы будут использоваться (Если не нужно, оставьте поле пустым):')
str5 = str1 + str2 + str3 + str4
k =input('Введите длинну паролей:')
k =int(k)
store =os.getcwd()
if not os.path.exists(store):
    os.makedirs(store)
f = open('dict.txt', 'a')
for i in range(0, 99):
    ls = list(str5)
    random.shuffle(ls)
    passw = ''.join([random.choice(ls) for x in range(k)])
    print(passw)
    f.write(passw+'\n')

#by aqswdefr746 and a little bit by Kli