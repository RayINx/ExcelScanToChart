import pandas as pd

#Read first line in excel

doubleDown = pd.read_excel('DOTA2DoubleDown.xlsx')

print(doubleDown)

#Need a way to see the delta of MMR lost/gained
#Need to see top hero played
#Most gmaes played in a day, MMR gained lost that day

#Filter out Win games and Lost games
winGames = doubleDown[doubleDown['Win/Lose'] == 'Win']
lostGames = doubleDown[doubleDown['Win/Lose'] == 'Lost']


