"""
10) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები
"""


pin_code = 1234
attempts = 3
granted = False

while attempts > 0 and not granted:
    pin_input = int(input("Enter the PIN code: "))
    if pin_input == pin_code:
        granted = True
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect, you have", attempts, "attempts left. Try again.")

if granted:
    print("Access Granted")
else:
    print("Access Denied")