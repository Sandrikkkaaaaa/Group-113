"""
2) გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი
"""

# მეტია
print(10 > 5)    # True
print(3 > 8)     # False
print(5.5 > 5.4) # True
print(7 > 7)     # False
print(-2 > -5)   # True

# მეტია ან ტოლია
print(10 >= 10)  # True
print(15 >= 20)  # False
print(4.5 >= 4.5)# True
print(3 >= 5)    # False
print(0 >= -1)   # True

# ნაკლებია
print(4 < 9)     # True
print(12 < 7)    # False
print(3.14 < 3.15) # True
print(6 < 6)     # False
print(-10 < -2)  # True

# ნაკლებია ან ტოლია
print(5 <= 5)    # True
print(8 <= 3)    # False
print(2.5 <= 2.5)# True
print(10 <= 4)   # False
print(-3 <= 0)   # True

# ტოლია
print(7 == 7)    # True
print(4 == 9)    # False
print(3.0 == 3)  # True
print("apple" == "banana") # False
print("hello" == "hello")  # True

# არ არის ტოლი
print(5 != 5)    # False
print(10 != 3)   # True
print(4.1 != 4.2)# True
print("python" != "python") # False
print("code" != "bug")      # True