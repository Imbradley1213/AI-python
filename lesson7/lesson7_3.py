import random
import pyinputplus as pyip
def play_game():
    min=1
    max=100
    count=0
    target=random.randint(1,100)
    print('-------猜數字遊戲-------\n')
    while True:
        count+=1
        keyin=pyip.inputInt(f'猜數字範圍{min}~{max}',min=min,max=max)
        if keyin==target:
            print(f'恭喜中獎~是{keyin}')
            print(f'已猜了{count}次')
            break
        elif keyin>target:
            print('再小點')
            max=keyin
        elif keyin<target:
            print('再大點')
            min=keyin
        print(f'已猜了{count}次')
while True:
    min=1
    max=100
    count=0
    target=random.randint(1,100)
    print('-------猜數字遊戲-------\n')
    while True:
        play_game()
        is_play=pyip.inputYesNo('繼續嗎?(yes,no)')
        if is_play=='no':
            break
print('應用程式結束')
