from . import tools

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