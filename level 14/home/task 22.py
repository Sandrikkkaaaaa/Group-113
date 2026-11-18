"""
22) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს
"""


password="goabest123"
user_input=input("Enter Password:")

while user_input != password:
    user_input = input("Enter Password, Again: ")
print("Correct!")