#OOP PYTHON

class Hero: #merupakan template
    pass


hero1 = Hero() #object /instance
hero2 = Hero()

hero1.name = "miya"
hero1.kuat = 100

hero2.nama = "balmon"
hero2.kuat = 200

print(hero1)
print(hero1.__dict__)
print(hero1.name)

#constractor

class manusia:

    def __init__(self,x):
        print("hallo",x)

hero3 = manusia(10)

class hewan:  #hewan adalah class
    #class variabel
    jumlah = 0
    def __init__(self, inputname, power): #self adalah object, inputname dan power adalah atribut
        #instance variabel 
        self.nama = inputname
        self.kuat = power
        hewan.jumlah += 1
        print("menambah hewan : " + inputname)


hewan1 = hewan("bocah", 1000)
print(hewan.jumlah)
hewan2 = hewan("bolot", 2000)
print(hewan.jumlah)

#print(hewan1.nama) #menampilkan yg ada di variabel nama
#print(hewan1.__dict__) #menaampilkan semua data pd object
#print(hewan.__dict__) #menampilkan keseluruhan data pd class

print("hello world")

