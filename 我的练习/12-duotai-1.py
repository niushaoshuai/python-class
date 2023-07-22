class Document:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        # 如果子类调用show方法时，必须重写
        raise  NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        print("the pdf content...")
    pass

class Word(Document):
    def show(self):
        print("the word content...")
    pass

p1 = Pdf("联系方式.pdf")
w1 = Word("联系方式.doc")
p1.show()
w1.show()