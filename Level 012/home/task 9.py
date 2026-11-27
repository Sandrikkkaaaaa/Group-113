"""
9) მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ
"""

num = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

numinbetween1 = (num + 1)
numinbetween2 = (num2 - 1)

for i in range(numinbetween1, numinbetween2 + 1):
    print(i)