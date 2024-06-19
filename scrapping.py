from bs4 import BeautifulSoup

# Fungsi untuk membaca konten dari file HTML
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Fungsi untuk mendapatkan teks dari elemen berdasarkan kelas
def get_text_by_class(html_content, class_name):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(class_=class_name)
    return [element.get_text() for element in elements]

# Fungsi untuk memproses nomor telepon
def process_phone_numbers(numbers):
    processed_numbers = []
    for number in numbers:
        if number.startswith('('):
            continue  # Skip numbers that start with '('
        if number.startswith('08'):
            number = '+628' + number[2:]
        processed_numbers.append(number)
    return processed_numbers

# Fungsi untuk menyimpan nomor telepon ke file dengan pemisahan per 5 data
def save_numbers_to_file(numbers, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for i, number in enumerate(numbers):
            if i > 0 and i % 5 == 0:
                file.write(',\n')
            elif i > 0:
                file.write(',')
            file.write(number)

# Path ke file HTML
file_path = 'scrapping.html'


# Nama kelas yang ingin dicari
class_name = 'UsdlK'

# Membaca konten file HTML
html_content = read_html_file(file_path)

# Mendapatkan teks dari elemen dengan kelas tertentu
texts = get_text_by_class(html_content, class_name)

# Memproses nomor telepon
processed_numbers = process_phone_numbers(texts)
processed_numbers = list(set(processed_numbers))

# Menyimpan hasil ke file .txt
output_file_path = '../Promosi/nomor_telephon/bandung.txt'
save_numbers_to_file(processed_numbers, output_file_path)

print(f"Processed phone numbers have been saved to {output_file_path}")
