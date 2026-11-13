"""
1) თქვენი სახელი და გვარი დაბეჭდეთ 10-ჯერ 2 მეთოდით: ვირჯინული და ჩადური. შემდეგ კომენტარებით დაწერეთ რომელი მეთოდი ჯობია და რატომ თქვეი აზრით. 


ასევე input-ით მიიღეთ 2 რიცხვი საწყისი და საბოლოო. ამ ორ რიცხვს შორს არსებული ყველა რიცხვი დაბეჭდეთ
"""

# print("sandro qeshelashvili")
# print("sandro qeshelashvili")  
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")                  #Virgin 🤮🤮🤮
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")
# print("sandro qeshelashvili")


# for k in range(10):                             #Chad 😎😎😎
#     print("sandro")


# # CHAD method ჯობია რადგან უფრო ნაკლები კოდის წერა გიწევს და უფრო პრაქტიკულია


# start = int(input("Enter The First Number: "))
# end = int(input("Enter The Last Number: "))

# for i in range(1 + start, end):
#     print(i)

# counter = 10

# while counter > 0:
#     print(counter)
#     counter += 1

"""
2) შექმენით while ციკლი რომელიც გამოიტანს

40-იდან 20-მდე რიცხვებს
სანამ პაროლი სწორი იქნება
"""

counter = 40

while counter >= 20:
    print(counter)
    counter -= 1

password="GoaIsTheBest"
user_input=input("Enter Password:")

while user_input != password:
    user_input = input("Enter Password:")
print("Correct!")