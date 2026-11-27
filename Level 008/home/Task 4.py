"""
4) დაწერეთ პითონის კოდი რომელიც მომხმარებელს input-ის საშვალებით შეეკითხება და ცვლადში შეინახავს შემდეგ ინფორმაციას:
"""


name=str(input("Enter Your Name: "))
Surnane=str(input("Enter Your Surname: "))
age=int(input("Enter Your Age: "))
location=str(input("Enter Your Location: "))
Occupation=str(input("Enter Your Occupation: "))
Hobby=str(input("Enter Your Hobby: "))

"""
ამ ცვლადების საშვალებით კი გამოიტანს ერთ წინადადებას რომელშიც ყველა მიღებული ინფორმაცია იქნება გამოყენებული. 

მაგალითად:

Enter your name: Alex  
Enter your surname: Johnson  
Enter your age: 25  
Enter your location: New York  
Enter your occupation: Engineer  
Enter your hobby: Playing guitar  

Alex Johnson is 25 years old, lives in New York, works as an Engineer, and enjoys Playing guitar.
"""

print(name + " " + Surnane + " " + "is " + str(age) + " " + "Years old, " + "Lives in " + location + ", " + "works as a " + Occupation + " " +"and enjoys " + Hobby + ".")