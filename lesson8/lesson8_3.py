class Myclass:
    @classmethod
    def status(cls,BMI:float)->str:
        '''
        #param BMI:這是要傳出的值
        #return:傳出BMI的值
        '''
        if BMI<18.5:
            return('過輕')
        elif BMI<24:
            return('正常')
        elif BMI<27:
            return('過重')
        elif BMI<30:
            return('輕度肥胖')
        elif BMI<35:
            return('中度肥胖')
        else:
            return('重度肥胖') 

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
        print(f'你的體重為:{Myclass.status(BMI)}')
    stuff = input("請問還要繼續('q':離開,enter:繼續)嗎?:")
    if stuff=='q':
        break
print('應用程式結束')