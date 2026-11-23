"""
13) მომხმარებელს შემოატანინეთ რიცხვი. თუ რიცხვი დადებითია, შეამოწმეთ შიგნით მეორე if-ით არის თუ არა ლუწი, თუ ლუწია დაბეჭდეთ "Positive and even", თუ არა "Positive and odd". ხოლო თუ რიცხვი უარყოფითია, შეამოწმეთ მეორე if-ით არის თუ არა 10-ზე ნაკლები, თუ ნაკლებია დაბეჭდეთ "Negative and small", სხვა შემთხვევაში "Negative and large"
"""

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    if num < 10:
        print("Negative and small")
    else:
        print("Negative and large")