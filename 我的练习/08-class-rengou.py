#!/usr/bin/env python

class Person:
    role = 'person'

    def __init__(self,name,sex,attack_value):
        self.name = name
        self.sex = sex
        self.attack_value = attack_value
        self.life_value = 100
        self.weapon = Weapon()
    
    def attack(self,dog):
        dog.life_value -= self.attack_value
        print("人%s打狗，狗掉血%s,狗还剩%s血"%(self.name,self.attack_value,dog.life_value))

class Weapon:
    role = 'weapon'

    def use_gun(self,obj):
        self.name = "AK47"
        self.attack_value=50
        obj.life_value -= self.attack_value
        self.print_log(obj)
    def use_dog_beat(self,obj):
        self.name = "打狗棒"
        self.attack_value=30
        obj.life_value -= self.attack_value
        self.print_log(obj)
    def print_log(self,obj):
        # obj.life_value-=self.attack_value
        print("人使用%s打狗，狗掉血%s,狗还剩%s的血量"%(self.name,self.attack_value,obj.life_value))

class Dog:
    role = "dog"

    def __init__(self,name,breed,attack_value):
        self.name = name
        self.breed = breed
        self.attack_value = attack_value
        self.life_value = 100

    def beat(self,person):
        person.life_value -= self.attack_value
        print("狗%s咬人，人掉血%s,人还剩%s血"%(self.name,self.attack_value,person.life_value))

p1 = Person("owen","Male",50)
d1 = Dog("gjj","藏獒",45)

p1.attack(d1)
d1.beat(p1)

# p1.weapon.use_gun(d1)
p1.weapon.use_dog_beat(d1)