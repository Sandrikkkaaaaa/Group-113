"""
2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)
"""


#საწყისი წიგნების ფასი:
The_lord_of_the_rings=50
harry_potter=55
diary_of_the_wimpy_kid=30
the_holy_bible=25
Natsarkekia=20

#ფასდაკლება
percent_price_1=The_lord_of_the_rings%20
percent_price_2=harry_potter%25
percent_price_3=diary_of_the_wimpy_kid%15
percent_price_4=the_holy_bible%7.5
percent_price_5=Natsarkekia%5

#საწყისი წიგნის ფასი - ფასდაკლება
new_price_1=The_lord_of_the_rings-percent_price_1
new_price_2=harry_potter-percent_price_2
new_price_3=diary_of_the_wimpy_kid-percent_price_3
new_price_4=the_holy_bible-percent_price_4
new_price_5=Natsarkekia-percent_price_5

#შედეგი
print(new_price_1,new_price_2,new_price_3,new_price_4,new_price_5 )