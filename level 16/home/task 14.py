"""
14) while ციკლის საშვალებით მომხმარებელს შეეკითხეთ რიცხვი ყოველ ჯერზე, თუ რიცხვი კენტია გააგრძელეთ ციკლი (გამოიყენეთ continue), თუ რიცხვი ლუწია დაბეჭდეთ "even number detected" და თუ რიცხვი 0-ის ტოლია შეწყვიტეთ ციკლი (გამოიყენეთ break)
"""

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    if num % 2 != 0:
        continue

    print("even number detected")