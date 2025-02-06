# # Tapşırıq:
# # Bir tələbənin imtahan nəticələri verilmişdir. Aşağıdakı dictionary-də fənlər və onların qiymətləri saxlanılır.

# # Riyaziyyat  85, Fizika 78, Kimya 90, İngilis dili  88, Tarix 76

fenler = ["Riyaziyyat", "Fizika", "Kimya", "Ingilis dili", "Tarix"]
ballar = [85, 78, 90, 88, 76]

imtahan_neticeleri = {}

for i in range(len(fenler)):
    imtahan_neticeleri[fenler[i]] = ballar[i]

print(imtahan_neticeleri)