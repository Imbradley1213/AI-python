class TESTBMI():
    def __init__(self,name:str,h:float,w:float):
        self.name=name
        self.h=h
        self.w=w
    def username(self)->str:
        return f'{self.name}你好'
    def userbmi(self)->float:
        return round(self.w/((self.h*0.01)**2),ndigits=2)
    def status(self)->str:
        BMI=self.userbmi()
        if BMI<18.5:
            return "體重:過輕"
        elif BMI<24:
            return "體重:正常"
        elif BMI<27:
            return "體重:過重"
        elif BMI<30:
            return "體重:輕度肥胖"
        elif BMI<35:
            return "體重:中度肥胖"
        else:
            return "體重:重度肥胖"
from widget import TESTBMI
while True:
    try:
        name=str(input('請輸入姓名:'))
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
        n1=TESTBMI(name=name,h=h,w=w)
        print(n1.username())
        print(f'你的BMI值是{n1.userbmi()}')
        print(n1.status())
    stuff = input("請問還要繼續('q':離開,enter:繼續)嗎?:")
    if stuff=='q':
        break
print('應用程式結束')