from time import *
import random as r



def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1

    return error



def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput)/ time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input("Ready To Start : (Yes/No)")
        if ck == "yes":
            test = ["An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations."]
            ["Agent framework and applications built upon Qwen>=2.0, featuring Function Calling, Code Interpreter, RAG, and Chrome extension."]

            test1 = r.choice(test)
            print("     ---- TYPING SPEED ----")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter :")
            time_2 = time()

            print('Speed : ', speed_time(time_1, time_2, testinput), "w/sec")
            print("Error : ", mistake(test1, testinput))

        elif ck == 'no':
            print("Thank You")
            break

        else:
            print("Wrong Input. Try Again !")


