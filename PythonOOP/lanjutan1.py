#jumlah huruf pd kata
a="okebos"
print(len(a))

#array satu tipe
b=[10,9,8,7]
print(b[0])
print(b[1])

#array beda tipe
c=["siap",10]
print(c[0])
print(c[1])

#array kosong diisi
d=[]
d.append(100)
d.append("seratus")
print(d[0],d[1])

#menyisipkan data pd array 
e=[0,1,2,3,4]
e.insert(e[0],100) #menjadi didepan index nya
print(e) 

#menghapus
f=[0,1,2,3]
del(f[2])
print(f)

#string sebagai list
g="sayaoke"
print(g[0])

#panjang list
h=["aku","kamu"]
print(len(h))

#list dalam list
mhs=[[67021,"andi"],[67022,"roy"],[67023,"budi"]]
print(len(mhs)) #banyyak data
print(mhs[0]) #data keseluruhan
print(mhs[0][1]) #data terperinci

#membalikan urutan
i=[3,2,1]
i.reverse()
print(i)

#mengurutkan ascending
j=[3,1,2,4]
j.sort()
print(j)

#mengurutkan descending
j=[3,1,2,4]
j.sort()
j.reverse()
print(j)

#menyalin
k=[10,20]
l=k
k.append(7)
print(k)
print(l) 
#agar data variabel baru salinan awal
m=list(k)
k.append(30)
print(k)
print(m)

#dictionary-key & value (tipe data key dan value bebas termasuk list)
dosen={1001:"boy", 1002:"indra"} #key 1001 dan 1002 #value boy dan indra
print(dosen[1001])
print(dosen.keys()) #melihat key yang ada 
print(dosen.values()) #melihat value yang ada

#update data
dosen.update({1003:"ike"})
print(dosen)

#menghapus data 
del dosen[1002]
print(dosen)
type(4.0) #mengetahui tipe data

