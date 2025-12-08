
import datetime
import time
name=input("Enter your name: ")
times=datetime.datetime.now().hour
if 5<=times<=12:
   print("Good morning",name,".")
elif 12<=times<=15:
   print("Good noon",name,".")
elif 15<=times<=18:
   print("Good evening",name,".")
else:
   print("Good night",name,".")

   
print("Hello,Wellcome to your personal chat bot.")
print("You  can me ask simple question, and type bye for exit bot.")

replays={"hello":"Hi,i am your personal chat bot.\nHow can i help you.",
        "how are you":"I am very fine.you?",
        "motivate me":"Keep learning and keep Exploring",
        "happy":"great to hear that"}
def get_replay(user_question):
    user_question=user_question.lower().strip()
    for key in replays:
        if key in user_question:
            return replays[key]
    return "I am not abel to tell that.I am learning.Sorry"
while True:



 question=input("Enter your question here: ").lower().strip()
 replay=get_replay(question)

 print("Bot responce:",replay)
 if "bye" in question:
    break

