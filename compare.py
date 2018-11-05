def scorecompare(scoresA, scoresB, numOfHoles):
    whatever = 0
    for x in range(0,7):   
        if(scoresA[x] > scoresB[x]):
            whatever = whatever + 1
        elif(scoresA[x] < scoresB[x]):
            whatever = whatever - 1
        
    return whatever