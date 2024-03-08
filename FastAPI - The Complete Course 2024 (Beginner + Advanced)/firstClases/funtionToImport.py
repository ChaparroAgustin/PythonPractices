def calculateHomaework(assigmentArg):
    sumGrades = 0
    for homework in assigmentArg.values():
        sumGrades += homework
    finalGrades = round(sumGrades / len(assigmentArg),2)
    print(finalGrades)