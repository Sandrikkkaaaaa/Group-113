"""
შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა
"""

correct_pin = "1234"

attempts = 0

user_pin = input("Enter Pin:  ")
attempts += 1  

while user_pin != correct_pin:
    print("Wrong, Try Again: ")
    user_pin = input("Enter Pin:  ")
    attempts += 1  

print("Success!")
print("You needed", (attempts), "attempts")