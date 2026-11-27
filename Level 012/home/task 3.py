"""
3) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები
"""

temperature = 35
is_raining = False
age = 14
score = 85
cloudy = True


can_go_to_the_beach = temperature > 30 and not is_raining 
is_teenager = age >= 13
is_adult = age >= 21 
can_go_to_the_club = age >= 18 
the_movie_is_a_hit = score > 80

print(can_go_to_the_beach)  # True
print(is_teenager)  # True
print(is_adult)  # False
print(can_go_to_the_club)  # False
print(the_movie_is_a_hit)  # True