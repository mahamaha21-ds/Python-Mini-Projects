import random as rd
print("WELCOME TO QUIZ GAME")
print("READY!")
setquestions={'What is the capital of India?':'New Delhi',
           'Which planet is known as the Red Planet?':'Mars',
           'Which is the largest mammal on Earth?':' Blue Whale',
           'Who is known as the Father of the Nation in India?':'Mahatma Gandhi',
           'What is the national bird of India?':'Peacock',
           'How many colors are there in a rainbow?':'Seven',
           'Which gas do plants take in for photosynthesis?':'Carbon Dioxide'}
score=0
while True:
    question=rd.choice(list(setquestions.keys()))
    print("question:",question)
    answer=input("Your answer:",)
    if answer.lower() == setquestions[question].lower():
        score+=1
        ans=setquestions[question]
        print("CORRECT ANSWER!")
    else:
        print("WRONG ANSWER!")
        print("CORRECT ANSWER:",ans)
    if answer.lower()=="exit":
        print("EXIT")
        break

print("TotalScore:",score)
