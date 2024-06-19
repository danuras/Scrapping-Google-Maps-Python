def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def reformat_phone_numbers(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Memisahkan nomor-nomor berdasarkan koma
    phone_numbers = data.split(',')
    # Menghapus spasi putih di sekitar nomor
    #phone_numbers = [number.strip() for number in phone_numbers]

    phone_numbers_2 = list(set(phone_numbers))
    phone_numbers_2.remove('')
    print(len(phone_numbers_2))
    chunked_data = chunk_list(phone_numbers_2, 100)
    for j in range (0, len(chunked_data)):
        # Menyimpan nomor dengan format baru
        with open(output_file_path+f'{j}.txt', 'w', encoding='utf-8') as file:
            for i, number in enumerate(chunked_data[j]):
                if i > 0 and i % 5 == 0:
                    file.write('\n')
                file.write(number)
                file.write(',')

# Contoh penggunaan
input_file_path = '../Promosi/nomor_telephon/surabaya.txt'
output_file_path = '../Promosi/nomor_telephon/surabaya/surabaya-'
reformat_phone_numbers(input_file_path, output_file_path)
