def reverse_shift(text, key):
    # Dekripsi dengan mengurangi nilai ASCII setiap karakter dengan key
    return "".join(chr((ord(c) - key) % 256) for c in text)

# Daftar string terenkripsi
obfuscated_texts = ["O`OD", "bv?Cm", "?Cm", "ev>m", "?mB{"]
# Daftar kunci yang digunakan dalam C++ untuk rotasi
keys = [4, 1, 7, 2, 5]

# Dekripsi string berdasarkan kunci
decoded = [reverse_shift(text, key) for text, key in zip(obfuscated_texts, keys)]

# Gabungkan hasil dekripsi untuk membentuk flag
flag = "".join(decoded)

# Menampilkan flag dalam format ARA6{}
print(f"ARA6{{{flag}}}")
