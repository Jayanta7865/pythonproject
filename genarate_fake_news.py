# import random
# subject=["jayanta",
# "Virat Kohali",
# "Mahadeb",
# "A dog",
# "A bus driver"]
# action=["eats mom",
#         "launches",
#         "dance with",
#         "orders",
#         "celebrates"]
# place_or_things=["a red fort",
#                  "black sunglass",
#                  "at ganga ghat",
#                  "a plate of samosa",
#                  "inside parlament"]
# while True:
#    subjects=random.choice(subject)
#    actions=random.choice(action)
#    place_or_thing=random.choice(place_or_things)
#    headline=f"Breaking News:{subjects} {actions} {place_or_thing}"
#    print("\n"+ headline)
#    user_input=input("\n Do you want to another headline(yes/no):").strip().lower()
#    if user_input=="no":
#       break

import random
from datetime import datetime
subjects = [
    "Jayanta",
    "Virat Kohli",
    "Mahadeb",
    "A dog",
    "A bus driver",
    "A college student",
    "An angry teacher"
]

actions = [
    "eats",
    "launches",
    "dances with",
    "orders",
    "celebrates",
    "steals",
    "destroys"
]

places_or_things = [
    "a red fort",
    "black sunglasses",
    "at Ganga Ghat",
    "a plate of samosa",
    "inside Parliament",
    "a broken scooter",
    "a stolen bicycle"
]

emotions = [
    "angrily",
    "secretly",
    "happily",
    "emotionally",
    "fearlessly",
    "unexpectedly"
]



count = 1  

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    emotion = random.choice(emotions)
   

   
    time = datetime.now().strftime("%I:%M %p")

    headline = f"({time}) Breaking News: {subject} {emotion} {action} {place_or_thing}!"

    print(f"\n{count}. {headline}")
    print("***Fack NEWS — NOT REAL ***")

    
    with open("news_history.txt", "a") as file:
        file.write(headline + "\n")

    count += 1

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        print("\n All generated news saved in: news_history.txt")
        print("Program stopped.")
        break
