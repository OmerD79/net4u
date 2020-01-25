import random
from time import sleep

def manual_lotto(NoOfPlays):
    lottoform = []
    while len(lottoform) < NoOfPlays:
        Entry = []
        while len(Entry) < 6:
            num = int(input('Enter num between 1 - 37: '))
            while num < 1 or num > 37 or num in Entry:
                print('Only numbers between 1-37 and number cannot be repeated.\n')
                num = int(input('Enter num between 1 - 37: '))
                continue
            Entry.append(num)
            continue
        print('Six numbers were entered. Continue to next line')
        lottoform.append(Entry)
        continue
    print('Your chosen numbers are:\n')
    print(lottoform)
    return lottoform

def auto_lotto(NoOfPlays):
    lottoform = []
    while len(lottoform) < NoOfPlays:
        Entry = []
        while len(Entry) < 6:
            num = random.randint(1,37)
            while num in Entry:
                num = random.randint(1,37)
                continue
            Entry.append(num)
            continue
        print('Six numbers were entered. Continue to next line')
        lottoform.append(Entry)
        continue
    print('Your chosen numbers are:\n')
    print(lottoform)
    return lottoform

def checkwin(win,lottoform):
    winlist = []
    lottoformIndex = 0
    while len(winlist) < len(lottoform):
        countwin = 0
        for i in range(0, 6):
            if win[i] in lottoform[lottoformIndex]:
                countwin += 1
            continue
        winlist.append(countwin)
        lottoformIndex += 1
        continue

    # print(winlist)

    sumWins = []
    winlistIndex = 0
    while len(sumWins) < len(winlist):
        sumwin = 0
        if winlist[winlistIndex] == 1 or winlist[winlistIndex] == 2:
            SumWin = 0
        elif winlist[winlistIndex] == 3:
            SumWin = 10
        elif winlist[winlistIndex] == 4:
            SumWin = 250
        elif winlist[winlistIndex] == 5:
            SumWin = 5000
        elif winlist[winlistIndex] == 6:
            SumWin = 1000000
        sumWins.append(sumwin)
        winlistIndex += 1
        continue
    # print(sumWins)

    TotalWin = 0
    for i in sumWins:
        TotalWin = TotalWin + i

    print('You won ' + str(TotalWin) + ' Shekels')


###Main Dev

sum = int(input('Enter the sum of money that you want to play: '))
NoOfPlays = int(sum / 3)
print('The number of plays is ' + str(NoOfPlays))

method_of_lotto = input('please enter the method that you want to fill the lotto. Enter 1 for automatic / 2 for manual: ')
if method_of_lotto == '1':
    lottoform = auto_lotto(NoOfPlays)
elif method_of_lotto == '2':
    lottoform = manual_lotto(NoOfPlays)

print('Running lotto draw..')
sleep(3)
win = []
while len(win) <6:
    ball = random.randint(1, 37)
    if ball not in win:
        win.append(ball)
    else:
        continue

print('Winning numbers are:')
print(win)

ischeckwin = input('Do you wish to check your win? y/n')
if ischeckwin == 'y':
    checkwin(win,lottoform)
elif ischeckwin == 'n':
    Print('Thank you. Please try again next time.')

