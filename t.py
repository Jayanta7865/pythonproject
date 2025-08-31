import random

questions = [
    ["Who invented C language?", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup", "Guido van Rossum", "a"],
    ["Python is developed by?", "Guido van Rossum", "Bjarne", "Ken", "Dennis", "a"],
    ["Java is developed by?", "James Gosling", "Dennis", "Guido", "Bjarne", "a"],
    ["C++ is developed by?", "Ken", "Dennis", "Guido", "Bjarne", "d"],
    ["Which is used for AI?", "Java", "C", "Python", "HTML", "c"]
]

levels = [1000, 2000, 5000, 10000, 50000]
money = 0
lifeline_used = False

print("🎉 Welcome to KBC (Kaun Banega Crorepati)!\n")

for i in range(len(questions)):
    question = questions[i]
    print(f"🎯 Question for Rs. {levels[i]}:\n")
    print(f"{i+1}.{question[0]}")
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    while True:
        reply = input("\n👉 Choose your answer (a/b/c/d) or type 'lifeline': ").strip().lower()

        if reply == "lifeline":
            if lifeline_used:
                print("❌ Lifeline already used.")
            else:
                lifeline_used = True
                correct_option = question[-1]
                options = ['a', 'b', 'c', 'd']
                options.remove(correct_option)
                removed = random.sample(options, 2)
                print("\n🧠 50:50 Lifeline Activated! Remaining options:")

                for opt in ['a', 'b', 'c', 'd']:
                    if opt not in removed:
                        idx = ord(opt) - ord('a') + 1
                        print(f"{opt}. {question[idx]}")
        elif reply in ['a', 'b', 'c', 'd']:
            break
        else:
            print("❌ Invalid input. Try again.")

    if reply == question[-1]:
        print(f"✅ Correct! You won Rs. {levels[i]}\n")
        money = levels[i]
    else:
        print("❌ Wrong answer! Game Over.")
        break

print(f"\n🏆 You take home Rs. {money}")
print("🙏 Thank you for playing KBC!\n")
