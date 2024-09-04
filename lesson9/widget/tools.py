def get_status_message(bmi: float) -> str:
    '''
    #param bmi:這是要傳入bmi傳
    #return:傳出bmi的狀態
    '''

    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常範圍"
    elif bmi < 27:
        return "過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"

class MyClass():
    @classmethod
    def get_status_message(cls,bmi: float) -> str:
        '''
        #param bmi:這是要傳入bmi傳
        #return:傳出bmi的狀態
        '''

        if bmi < 18.5:
            return "體重過輕"
        elif bmi < 24:
            return "正常範圍"
        elif bmi < 27:
            return "過重"
        elif bmi < 30:
            return "輕度肥胖"
        elif bmi < 35:
            return "中度肥胖"
        else:
            return "重度肥胖" 
        
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