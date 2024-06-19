# Daftar nomor telepon
def baca_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File tidak ditemukan."
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
numbers = baca_file('../Promosi/nomor_telephon/bandung.txt')

# Mengubah daftar nomor telepon menjadi sebuah list
number_list = [number.strip() for number in numbers.split(",")]

# Menggunakan set untuk mengecek keunikan
unique_numbers = set()
duplicates = set()

for number in number_list:
    if number in unique_numbers:
        duplicates.add(number)
    else:
        unique_numbers.add(number)

# Menampilkan hasil
if len(duplicates) > 0:
    print("Ada nomor duplikat:")
    for number in duplicates:
        print(number)
else:
    print("Semua nomor unik.")