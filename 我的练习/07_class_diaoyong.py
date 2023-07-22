class RelationShip:
    def __init__(self,couple):
        self.couple = couple
    
    def make_couple(self,obj1,obj2):
        print("%s 和 %s 交往了"%(obj1.name,obj2.name))
        self.couple=[obj1,obj2]

    def break_couple(self,obj):
        if self.couple:
            print("%s 和 %s 分手了"%(self.couple[0].name,self.couple[1].name))
            self.couple.clear()
        else:
            print("%s 分手个蛋"%(obj.name))

    def get_partner(self,obj):
        if self.couple:
            for i in self.couple:
                if i != obj:
                    print("%s your friend is %s"%(obj.name,i.name))
        else:
            print("%s you are single dog"%obj.name)

class Person:
    def __init__(self,name,age,sex,relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation


R1=RelationShip([])
# print(help(RelationShip))
p1=Person("jimi",23,"male",R1)
p2=Person("lily",23,"female",R1)
p3=Person("lily1",23,"female",R1)
R1.make_couple(p1,p2)
p1.relation.break_couple(p1)
p3.relation.break_couple(p3)
R1.get_partner(p2)

    
