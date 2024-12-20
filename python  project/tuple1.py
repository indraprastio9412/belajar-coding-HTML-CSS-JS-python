text = "aku anak pintar karena aku pintar karena aku belajar supaya pintar dan pintar itu aku"
print(text)

partText = text.partition("aku anak pintar karena aku pintar karena aku belajar supaya pintar dan pintar itu aku")
print(partText)#fungi partition ini mengembalikan sebuah tuple yg berisi 3 elemen diantaranya bagian sebelum pemisah,pemisah itu sendiri dan bagian setelah pemisah

chars = set(text)
print(chars)

for char in chars:
    print(char ,"=", text.count(char))

# Menampilkan kata yang sama
words = text.split()#funsi split() adalah digunakan untukmemecah string menjadi daftar(list) substring berdasarkan pemisah(delimeter) yg ditentukan,fungsi iniakan mengunakan spasi putih(whitspasi)sebagai default
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    if count > 0:
        print(f"{word} = {count}")
