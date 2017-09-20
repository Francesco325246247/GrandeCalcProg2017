def calcMyScore():
    totalScore = 0

    for score in range(9):

        if score == 1:
            addScore = input("Add your Module 1 score")
            Module1 = (int(addScore) * 2) / 100
            totalScore = totalScore + Module1
        elif score == 2:
            addScore = input("Add your Module 2 score")
            Module2 = (int(addScore) * 2) / 100
            totalScore = totalScore + Module2
        elif score == 3:
            addScore = input("Add your Module 3 score")
            Module3 = (int(addScore) * 4) / 100
            totalScore = totalScore + Module3
        elif score == 4:
            addScore = input("Add your Module 4 score")
            Module4 = (int(addScore) * 4) / 100
            totalScore = totalScore + Module4
        elif score == 5:
            addScore = input("Add your Module 5 score")
            Module5 = (int(addScore) * 8)/100
            totalScore = totalScore + Module5
        elif score == 6:
            addScore = input("Add your Module 6 score")
            Module6 = (int(addScore) * 8) / 100
            totalScore = totalScore + Module6
        elif score == 7:
            addScore = input("Add your Module 7 score")
            Module7 = (int(addScore) * 12) / 100
            totalScore = totalScore + Module7
        elif score == 8:
            addScore = input("Add your Exam score")
            Module8 = (int(addScore) * 60) / 100
            totalScore = totalScore + Module8

    print(int(totalScore/10))


calcMyScore()
