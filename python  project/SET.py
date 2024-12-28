#TYPE berpunsi untuk mencari tipe data
data = {}
print(type(data))

siswa_id ={112,354,576,245,547,647}
print('siswa Id:',siswa_id)

siswa_id.add(112)#add berpunsi untuk menambahkan
print(siswa_id)
siswa_id.discard(112)#discard berpungsi untuk membuang
print(siswa_id)

for i in siswa_id:
    print(i)
print(list(enumerate(siswa_id)))#PUNSI LIST mengakses indeks
print(max(siswa_id))#fungsi MAX untuk mencari nilai paling besar
print(min(siswa_id))#pungsi MIN untuk mencari nilai paling kecil
print(sum(siswa_id))#pungsi SUM untuk menjumlahkan
print((sorted(siswa_id)))#pungsi sorted untuk mengurutkan dari yang terkecil ke yang terbesar

#firs set
A = {1,3,5,2}
#second set
B = {0,2,4,7,3}
unionAB = A.union(B) #A|B
print(unionAB)






