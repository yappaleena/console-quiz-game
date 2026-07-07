quiz={"q1":"Ants move in a line because of their sense of -------",
      "ans1": "smell",
      "q2":"poisonous teeth of the snakes are called as---------",
      "ans2":"fangs",
      "q3":"The saltiest water body in the world is ---- sea",
      "ans3":"dead",
      "q4":"planet thats known as red planet----------",
      "ans4": "mars",
      "q5":"the largest sea animal is----------------",
      "ans5":"blue whale",
      "q6":"largest organ in human body is-----------",
      "ans6": "skin",
      "q7":"animals that eat only plants are known as-----------",
      "ans7":"herbivores",
      "q8":"bees collect ---------- from flowers",
      "ans8":"honey",
      "q9":"animal thats known as ship of desert--------",
      "ans9": "camel"}
while True:
    n=int(input("enter the number between 1 and 9 (to exit press 0):"))
    if n==0:
        print("quiz ended. see you again")
        break
    if n==1:
        print(quiz["q1"])
        a=input("enter the answer:")
        if a== quiz["ans1"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is",quiz["ans1"])
    elif n==2:
        print(quiz["q2"])
        a = input("enter the answer:")
        if a == quiz["ans2"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is", quiz["ans2"])
    elif n==3:
        print(quiz["q3"])
        a = input("enter the answer:")
        if a == quiz["ans3"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is", quiz["ans3"])
    elif n==4:
        print(quiz["q4"])
        a = input("enter the answer:")
        if a == quiz["ans4"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is", quiz["ans4"])
    elif n==5:
        print(quiz["q5"])
        a = input("enter the answer:")
        if a == quiz["ans5"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is", quiz["ans5"])
    elif n==6:
        print(quiz["q6"])
        a=input("enter the answer:")
        if a==quiz["ans6"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is",quiz["ans6"])
    elif n==7:
        print(quiz["q7"])
        a=input("enter the answer:")
        if a==quiz["ans7"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is",quiz["ans7"])
    elif n==8:
        print(quiz["q8"])
        a=input("enter the answer:")
        if a==quiz["ans8"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is",quiz["ans8"])
    elif n==9:

        print(quiz["q9"])
        a=input("enter the answer:")
        if a==quiz["ans9"]:
            print("correct answer")
        else:
            print("wrong! the correct answer is",quiz["ans9"])
    else:
        print("invalid option, please enter the number between 1 and 9")