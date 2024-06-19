def ubah_format_nomor(nomor):
    if nomor.startswith('0'):
        return '+62' + nomor[1:]
    return nomor

def proses_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            nomor_nomer = line.strip().split(', ')
            nomor_nomer_baru = [ubah_format_nomor(nomor) for nomor in nomor_nomer]
            file.write(', '.join(nomor_nomer_baru) + '\n')

# Nama file input dan output
input_file = 'nomor_target_2.txt'
output_file = 'nomor_target_2_hasil.txt'

# Memproses file
proses_file(input_file, output_file)

print(f"Nomor telepon dalam {input_file} telah diubah formatnya dan disimpan dalam {output_file}.")
