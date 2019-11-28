class manusia:
    jumlah_man = 0

    def __init__(self, inputname, inputumur, inputasal):
        self.name = inputname
        self.umur = inputumur
        self.asal = inputasal
        manusia.jumlah_man +=1
    
    #void function method tanpa return tanpa argumen
    def siapa(self):
        print("aku adalah " + self.name)
    
    #method dgn argummen tanpa return
    def tambahumur(self, up):
        self.umur+=up
    
    #method dgn return
    def getumur(self):
        return self.umur


man1 = manusia("awan", 20, "kebumen")
man2 = manusia("arif", 21, "kecepit")

print(man1.siapa())
man1.tambahumur(5)
print(man1.getumur())

