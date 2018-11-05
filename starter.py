from compare import scorecompare
import sys

a = [1,2,9,6,5,6,9,5]
b = [2,3,4,5,6,7,8,4]
leader = ''

if(len(a) != len(b)):
    sys.exit("Score mismatch")

numOfHoles = len(a)

breaker = scorecompare(a, b, numOfHoles)

if(breaker > 0):
    leader = 'Player A'
elif(breaker < 0):
    leader = 'Player B'
else:
    print('The score is tied')
    sys.exit()
    
print(leader + ' is leading by ' + str(abs(breaker)))
