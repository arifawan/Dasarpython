#operator
print(10+5)
print(10*5)
print(float (10)/3)
print((5+2)*2)

#pembulatan berjalan benar di console
a=15.5
int (a) #pembulatan ke bawah
print (a)
b=17.5
round (b)  #pembulatan ke atas
print(b)

#string
print("test petik dua")
print('test petik satu')

#menulis kutip (')
print('don\'t') #atau 
print("don't")

#string banyak
print("""
Cara mulai coding :
    1. niat yangg bener
    2. tekat yang kuat
    3. memulai """)

#penjumlahan & perkalian
c='aku'
d='love'
e='kamu'
print(c+' '+d+' '+e)

print('-'*5)

#mengubah jadi string
f=5
g=5
h=f+g
#i=str(f)+"+"+str(g)+"="+str(h) #atau
i="%i + %i = %s" % (f,g,h) #memudahkan debuging
print(i)

#String jadi integer
j="10"
int(j)
print(j)

#string jadi float
k="8.9"
float(k)
print(k)