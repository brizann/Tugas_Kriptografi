import sys

def modulo_operation():
    print("\n=== 01 Operasi Modulo ===")
    try:
        a = int(input("Masukkan angka pertama (a): "))
        b = int(input("Masukkan angka kedua pembagi (b): "))
        print(f"Hasil: {a} mod {b} = {a % b}")
    except ValueError:
        print("Input harus berupa angka!")
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan angka nol!")

def letter_to_number(char):
    char = char.upper()
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    return -1

def number_to_letter(num):
    if 0 <= num <= 25:
        return chr(num + ord('A'))
    return '?'

def interactive_letter_number():
    print("\n=== 02 Huruf <-> Angka (A=0...Z=25) ===")
    print("1. Ubah Huruf ke Angka")
    print("2. Ubah Angka ke Huruf")
    pilihan = input("Pilih (1/2): ")
    
    if pilihan == '1':
        char = input("Masukkan satu huruf: ")
        if len(char) == 1 and char.isalpha():
            print(f"Huruf '{char.upper()}' -> Angka: {letter_to_number(char)}")
        else:
            print("Input tidak valid. Masukkan hanya 1 karakter huruf.")
    elif pilihan == '2':
        try:
            num = int(input("Masukkan angka (0-25): "))
            if 0 <= num <= 25:
                print(f"Angka {num} -> Huruf: '{number_to_letter(num)}'")
            else:
                print("Angka harus berada di antara 0 dan 25.")
        except ValueError:
            print("Input harus berupa angka!")
    else:
        print("Pilihan tidak valid.")

def interactive_caesar():
    print("\n=== 03 Caesar Cipher dengan Modulo ===")
    print("1. Enkripsi (Maju)")
    print("2. Dekripsi (Mundur)")
    mode = input("Pilih mode (1/2): ")
    
    if mode in ['1', '2']:
        text = input("Masukkan teks: ")
        try:
            shift = int(input("Masukkan nilai pergeseran (shift): "))
            if mode == '2':
                shift = -shift # Dekripsi berarti digeser ke arah sebaliknya
                
            result = ""
            for char in text.upper():
                if 'A' <= char <= 'Z':
                    num = letter_to_number(char)
                    shifted = (num + shift) % 26
                    result += number_to_letter(shifted)
                else:
                    result += char
            print(f"\nHasil: {result}")
        except ValueError:
            print("Nilai shift harus berupa angka bulat!")
    else:
        print("Pilihan tidak valid.")

def interactive_xor():
    print("\n=== 04 XOR sederhana pada data biner ===")
    data1 = input("Masukkan data biner ke-1 (contoh: 1010): ")
    data2 = input("Masukkan data biner ke-2 (contoh: 1100): ")
    
    # Validasi input hanya 0 dan 1
    if not (all(c in '01' for c in data1) and all(c in '01' for c in data2)):
        print("Error: Input hanya boleh mengandung 0 dan 1!")
        return
        
    # Menyamakan panjang agar sejajar (padding kiri dengan 0)
    max_len = max(len(data1), len(data2))
    d1 = data1.zfill(max_len)
    d2 = data2.zfill(max_len)
    
    result = ""
    for b1, b2 in zip(d1, d2):
        if b1 == b2:
            result += "0"
        else:
            result += "1"
            
    print(f"\nData 1   : {d1}")
    print(f"Data 2   : {d2}")
    print(f"Hasil XOR: {result}")

def main():
    while True:
        print("\n" + "="*40)
        print("   MENU KRIPTOGRAFI DASAR INTERAKTIF")
        print("="*40)
        print("1. Operasi Modulo")
        print("2. Konversi Huruf <-> Angka")
        print("3. Caesar Cipher")
        print("4. XOR Data Biner")
        print("5. Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            modulo_operation()
        elif pilihan == '2':
            interactive_letter_number()
        elif pilihan == '3':
            interactive_caesar()
        elif pilihan == '4':
            interactive_xor()
        elif pilihan == '5':
            print("Terima kasih, selamat bereksperimen! 👋")
            sys.exit(0)
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
