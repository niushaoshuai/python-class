class test:
# 在调用eat方法时会将eat()函数本身作为第一个参数传给eat方法，eat方法的第二个参数接收实例传过来的真实的参数
    def eat(self,food):
        print(self,"im eating",food)


p=test()
#p.eat("123","xjiao")

p.eat("xjiao")

func1=p.eat
func1("aaa")