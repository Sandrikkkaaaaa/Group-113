"""
11) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო
"""

total = 0
count = 0

n = int(input("Enter a number: "))
while n != -1:
    total += n
    count += 1
    n = int(input("Enter a number: "))

if count > 0:
    print("Average:", total / count)
else:
    print("No numbers were entered")