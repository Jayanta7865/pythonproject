questions=[
    ["What is the capital of India?","west Bengal","kolkata","Mumbai","New Delhi", 4],
    [" Which planet is known as the Red Planet?"," Venus","Mars","Jupiter","Earth",2],
    ["Which country is famous for the Eiffel Tower?","India","Astralia","Germany","France",4],
    ["What is the chemical symbol for gold?","Au","Ag","co2","Al", 1],
    ["What is the tallest mountain in the world?","K2","Kangchenjunga ","Mount Everest","Lotus", 3],
    ["Who painted the Mona Lisa?","Vincent van Gogh"," Leonardo da Vinci ","Jayanta","Mahadeb",2],
    ["Where was India first national Museum opened?","Mumbai","Delhi","Kolkata","Bengaluru", 1],
    [" In 2019, Which popular singer was awarded the Bharat Ratna award?","Arijit Shing","Bhupen Hazarika","Lata ji","Asha Bhosle",2],
    [" The green planet in the solar system is?","Mars","Venas","Uranus","Earth",3],
    ["The father of Indian missile technology is _________________?","Dr Homi Bhabha","Dr Chidambaram","Dr U.R. Rao","Dr A.P.J. Abdul Kalam", 4],
    ["The largest public sector undertaking in the country is?","Airways","Roadways","railways","all correct",3],
    ["In 2017, Who was appointed as the new Brand Ambassador for Swachh Bharat Mission?","Shilpa Shetty","Karina Kapoor","Anushka Sharma","Kangana Ranaut",1],
    ["Which is the largest island?","Green Land","New Guinea","Andaman Nicobar","Hawaii",1],
    [" What is the official currency of Japan?","won","dollar","yuan","yen",4],
    ["Which river is the second longest in the world?","Amazon","Yangtze","Nile","Mississippi",2],
   ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
print(f"\n\n WELLCOME TO KBC")

for i in range(0, len(questions)):
  
    question = questions[i]
    print(f"\nThe question of Rs.{levels[i]}:\n\n{question[0]} ")
    print(f"a. {question[1]}")   
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    reply=int(input(f"\nLock your answer (1-4)or press 0 to Quit: "))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply == question[-1]):
        print(f"\n correct answer, you won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
       
    else:
        print(f"\n worng answer..\n")
        print(f"dont worry")
        break

print(f"\nYour Prize Ammount is Rs.{money}\n")
print("\nTHANK YOU FOR PLAYING KBC")

    

