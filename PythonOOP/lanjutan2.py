#Kondisi if
#n= raw_input("Lanjut y(ya)/t(tidak) : ") #kemungkinan berjalan hanya di linux
#if n in ["y","Y"]:
 #   print("ya")
#else:
#    print("tidak")

#perulangan for
for nomor in [1,2,3]:
    print(nomor)
print(".......")

#perullangan while
i=0
while i < 3 :
    i=i+1
    print(i)
print("..........")

import random
a = 0
while a <= 0.5:
    a= random.random()
    print(a)
    break #keluar perulangan
print("selesai")

#fungsi
def garis():
    print("-"*30)
garis()
print("Setiap pesan diawali garis ")
garis()
print("Juga diakhiri garis")
garis()

#dengan masukan 

def garis(kar,jum):
    print(kar*jum)
print("HEADER")
garis(".",40)
