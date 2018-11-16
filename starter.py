from compare import scorecompare
from dbplayers import get_player_names
from dbplayers import get_single_player_name
import sys

a = [1,2,9,6,7,6,9,5]
b = [2,3,4,5,6,7,8,4]
leader = ''

if(len(a) != len(b)):
    sys.exit("Score mismatch")

numOfHoles = len(a)

breaker = scorecompare(a, b, numOfHoles)

playernames = get_player_names()

print('Here be things', playernames[1][2])

if(breaker > 0):
    leader = 2
elif(breaker < 0):
    leader = 1
else:
    print('The score is tied')
    sys.exit()
    
winner = get_single_player_name(leader)

print(winner[0][0] + ' is leading by ' + str(abs(breaker)))
