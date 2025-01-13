#High or Low Game

import random

point=0
game_over=False

#Generate the random number
def random_number():
    return random.randint(0,8) # i know the lenth of the list

def is_correct(A,B):
    if A<B:
        return "B"
    else:
        return "A"




logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""



#Game Data
game_data=[
    
{ 'name':'Vijay',
   'age':50,
   'number_of_movies':65,
    'Industry':'Kollywood'
},
{ 'name':'Aamir Khan',
   'age':59,
   'number_of_movies':52,
    'Industry':'Bollywood'
},
{ 'name':'Rajinikanth',
   'age':73,
   'number_of_movies':160,
    'Industry':'Kollywood'
 },
 { 'name':'Kamal Haasan',
   'age':69,
   'number_of_movies':230,
    'Industry':'Kollywood'
},
    { 'name':'Mahesh Babu',
   'age':49,
   'number_of_movies':36,
    'Industry':'Tollywood'
},
{ 'name':'Akshay Kumar',
   'age':57,
   'number_of_movies':150,
    'Industry':'Bollywood'
},
{ 'name':'Prabhas',
   'age':44,
   'number_of_movies':23,
    'Industry':'Tollywood'
},
    { 'name':'Allu Arjun',
   'age':41,
   'number_of_movies':20,
    'Industry':'Tollywood'
},
{ 'name':'Yash',
   'age':38,
   'number_of_movies':20,
    'Industry':'Sandalywood'
}
]
print(logo)
choice=random_number()
while not game_over:
    print(f"Compare A: {game_data[choice]['name']}, age {game_data[choice]['age']},from {game_data[choice]['Industry']}.")
    print(vs)
    against=random_number()
    print(f"Aganist B: {game_data[against]['name']}, age {game_data[against]['age']},from {game_data[against]['Industry']}.")
    user_choice=input("Who has acted more movies? Type 'A' or 'B'")
    
    if is_correct(game_data[choice]['number_of_movies'],game_data[against]['number_of_movies'])==user_choice.upper():
        choice=against
        point+=1
        print(f"You're Right! Current Score: {point}")
         
    else:
        print(f"You're Wrong! Final Score: {point}")
        game_over=True
    
    
