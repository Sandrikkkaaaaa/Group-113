"""
4) შექმენით 30 მაგალითი შედარების ოპერაციებზე (>, <, >=, <=, ==, !=), გამოიყენეთ სხვადასხვა ტიპის მნიშვნელობები (რიცხვები, სტრინგები, ცვლადები). თითოეულ მაგალითში კომენტარით მიუწერეთ, რას აბრუნებს (True ან False) და რატომ მაგალითად, თუ ობიექტები განსხვავებული ტიპისაა, ახსენით როგორ იქნა შედარებული. ეცადეთ, რომ მაგალითები არ გამეორდეს და მოიცავდეს სხვადასხვა სიტუაციებს (მათ შორის ცვლადების გამოყენებასაც)
"""


# მეტია
print(10 > 5)     # True
print(2 > 8)      # False
print(5.5 > 5.0)  # True
print(-1 > -5)    # True
print(3 > 3)      # False

# ნაკლებია
print(3 < 8)      # True
print(10 < 5)     # False
print(2.1 < 2.5)  # True
print(-10 < -5)   # True
print(7 < 7)      # False

# მეტია ან ტოლია
print(5 >= 5)     # True
print(10 >= 12)   # False
print(4.5 >= 4.0) # True
print(0 >= -1)    # True
print(2 >= 3)     # False

# ნაკლებია ან ტოლია
print(4 <= 4)     # True
print(9 <= 6)     # False
print(1.5 <= 2.0) # True
print(-3 <= -3)   # True
print(8 <= 5)     # False

# ტოლია 
print(5 == 5)     # True
print(4 == 9)     # False
print(3.0 == 3)   # True
print("apple" == "apple") # True
print("cat" == "dog")     # False

# არ არის ტოლი
print(5 != 5)     # False
print(10 != 3)    # True
print("python" != "java") # True
print(2.5 != 2.5) # False
print(100 != 99)  # True