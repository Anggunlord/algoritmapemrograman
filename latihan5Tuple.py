tuple_1 = ("faqih", "Nicko", "Ageng", "Ihsan", "Adin")
tuple_2 = (23, 42, 12, 53, 64)
tuple_3 = "Puri", "putri", "Syifa", "Lord Anggun"

print(tuple_1)
print(tuple_2)
print(tuple_3)



#Membuat Tuple Yang Bernilai Kosong
empty_tuple = ()
print("tuple kosong: ", empty_tuple)

#tuple bernilai integer
int_tuple = (4, 6, 8, 10, 12, 14)
print("Tuple bernilai Integer: ", int_tuple)
 
 #tuple dengan kombinasi tipe data
mixed_tuple = (4,"Python",9.3)
print("Tuple dengan tipe data yang berbeda: ", mixed_tuple)
 
 #Tuple bersarang
nested_tuple = ("Python", {4: 5, 6: 2, 8:2},(5,3,5,6))
print("A Tuple bersarang: ", nested_tuple)
 
print()
print()
print()

#Membuat lish

identitas = ["Lord Anggun Hidetoshi",27, "Jepang"]
prodi_1 = ["Informatika",10]
prodi_2 = ["Sistem Informasi",11]
dosen_1 = [10, "Ms. Lord Anggun Hidetoshi"]
dosen_2 = [11, "Ms. Lord Anggun Hidetoshi"]

print("cetak semua data...")
print("-----------------------------------------------------------------------")
print("Nama: %s, Usia: %d, Negara: %s"%(identitas[0],identitas[1],identitas[2]))
print("-----------------------------------------------------------------------")
print("Cetak Program Studi...")
print("-----------------------------------------------------------------------")
print("program Study 1:\nNama Prodi Pertama: %s, ID: %d\nProgram Studi kedua: %s, ID: %s"%(prodi_1[0],prodi_1[1],prodi_2[0],prodi_2[1]))
print("-----------------------------------------------------------------------")
print("Dosen Pengampu...")
print("-----------------------------------------------------------------------")
print("Dosen Informatika: %s, ID: %d"%(dosen_1[1],dosen_2[0]))
print("Dosen Sistem Informasi: %s, ID: %d"%(dosen_2[1],dosen_2[0]))
print(type(identitas),type(prodi_1),type(prodi_2),type(dosen_1),type(dosen_2))


print()
print()
print()

#forward
print("---------------------------")
print("Firmansyah")
print("---------------------------")
print(list[1])
print(list[3:])
print(list[:1])
print(list[1:3])




#backward
print("--------------------------")
print("Firmansyah")
print("--------------------------")

print(list[-1])
print(list[-3:])
print(list[:-1])
print(list[-3:-1])
