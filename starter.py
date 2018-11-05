from compare import scorecompare

a = [1,2,9,6,5,6,7]
b = [2,3,4,5,6,7,8]

numOfHoles = 7

breaker = scorecompare(a, b, numOfHoles)

print('The winner is leading by ', breaker)