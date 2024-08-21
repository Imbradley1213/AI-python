import tools
while True: 
    name=str(input('請輸入姓名:'))
    try:
        h=float(input('請輸入身高cm:'))
        if h<=0:
            raise Exception
        w=float(input('請輸入體重kg:'))
        if w<=0:
            raise Exception
    except Exception:
        print('格式錯誤')
        continue
    else:
        BMI=round(w/((h*0.01)**2),ndigits=2)
        print(f'{name}你好:')
        print(f'你的BMI值為:{BMI}')
        print(f'你的體重為:{tools.status(BMI)}')
    stuff = input("請問還要繼續('q':離開,enter:繼續)嗎?:")
    if stuff=='q':
        break
print('應用程式結束')