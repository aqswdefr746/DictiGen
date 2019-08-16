import sys
import os
import pyfiglet
import random
#
#

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
text = "Dicti Gen"
cprint(pyfiglet.figlet_format(text, font ="colossal") ,"green")
print('by aqswdefr746 and Kli')
print(' ')
enlang = 'EN/'
ukrlang = 'UKR'
rulang = 'RU/'
ru1 = 'Введите какие цифры будут использоваться:'
en1 = 'Enter digits that programm will use:'
ukr1 = 'Введіть які цифри будуть використовуватись:'
ru2 = 'Введите какие маленькие буквы будут использоваться:'
en2 = 'Enter letters that programm will use:'
ukr2 = 'Введіть які маленькі літери будуть використовуватись:'
ru3 = 'Введите какие заглавные будут использоваться:'
en3 = 'Enter capital letters that programm will use:'
ukr3 = 'Введіть які великі літери будуть використовуватись:'
ru4 = 'Введите какие спецсиволы будут использоваться (оставьте поле пустым если не нужны):'
en4 = 'Enter special symbols that programm will use (leave the field empty if not needed):'
ukr4 = 'Введіть які спеціальні символи будуть використовуватись (залиште пустим якщо не потрібно)'
rupass = 'Введите длину генерируемых паролей:'
enpass = 'Enter password generation length:'
ukrpass = 'Введіть довжину генерируємих паролів:'
ruamount = 'Введите количество паролей:'
enamount = 'Amount of passwords to generate:'
ukramount = 'Введіть кількість паролів:'
while True:
    print('Please choose Your language')
    print(str(rulang+enlang+ukrlang))
    lch = str(input())
    print(lch)
    if lch == 'RU'  or lch == 'ru':
        str1text = ru1
        str2text = ru2
        str3text = ru3
        str4text = ru4
        lpass = rupass
        lamount = ruamount
        print('Язык изменён на русский')
        break
    elif lch == 'EN' or lch =='en':
        str1text = en1
        str2text = en2
        str3text = en3
        str4text = en4
        lpass = enpass
        lamount = enamount
        print('Language set to Еnglish')
        break
    elif lch == 'UKR' or lch == 'ukr':
        str1text = ukr1
        str2text = ukr2
        str3text = ukr3
        str4text = ukr4
        lpass = ukrpass
        lamont = ukramount
        print('Мова змінена на українську')
        break
    else:
        print('Wrong input.')
str1 =input(str1text)
str2 =input(str2text)
str3 =input(str3text)
str4 =input(str4text)
str5 = str1 + str2 + str3 + str4
k =input(lpass)
k =int(k)
l =input(lamount)
l =int(l)
#
#
str1 =input('Введите какие цифры будут использоваться:')
str2 =input('Введите какие маленькие буквы будут использоваться:')
str3 =input('Введите какие заглавные буквы будут использоваться:')
str4 =input('Введите какие спецсимволы будут использоваться (Если не нужно, оставьте поле пустым):')
str5 = str1 + str2 + str3 + str4
k =input('Введите длинну паролей:')
k =int(k)
l =input('Введите количество паролей:')
l =int(l)
store =os.getcwd()
if not os.path.exists(store):
    os.makedirs(store)
f = open('dict.txt', 'a')
for i in range(0, l):
    ls = list(str5)
    random.shuffle(ls)
    passw = ''.join([random.choice(ls) for x in range(k)])
    print(passw)
    f.write(passw+'\n')

#by aqswdefr746 and a little bit by Kli