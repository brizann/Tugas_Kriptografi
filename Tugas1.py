def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        # Hanya enkripsi huruf A-Z (huruf besar/kecil dipertahankan)
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += encrypted_char
        else:
            # Spasi, angka, dan tanda baca dipertahankan
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    # Dekripsi Caesar adalah enkripsi dengan nilai shift negatif
    return caesar_encrypt(ciphertext, -shift)

def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    key_idx = 0
    
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Hitung nilai geser berdasarkan huruf pada keyword saat ini
            shift = ord(keyword[key_idx % len(keyword)]) - ord('A')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += encrypted_char
            
            # Index keyword hanya maju kalau karakter adalah huruf (spasi diabaikan)
            key_idx += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    key_idx = 0
    
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[key_idx % len(keyword)]) - ord('A')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += decrypted_char
            key_idx += 1
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    while True:
        print("\n" + "="*45)
        print(" PROGRAM KRIPTOGRAFI KLASIK BY Brizan Cihuy")
        print("="*45)
        print("1. Caesar Cipher (Enkripsi)")
        print("2. Caesar Cipher (Dekripsi)")
        print("3. Vigenère Cipher (Enkripsi)")
        print("4. Vigenère Cipher (Dekripsi)")
        print("5. Keluar")
        
        pilihan = input("\nPilih menu (1-5): ")
        
        if pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
            
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid, silakan pilih 1-5.")
            continue
            
        text = input("Masukkan teks pesan: ")
        
        if pilihan in ['1', '2']:
            try:
                shift = int(input("Masukkan nilai shift key (angka): "))
                if pilihan == '1':
                    hasil = caesar_encrypt(text, shift)
                    print(f"\n[+] Hasil Enkripsi : {hasil}")
                else:
                    hasil = caesar_decrypt(text, shift)
                    print(f"\n[-] Hasil Dekripsi : {hasil}")
            except ValueError:
                print("\n[!] Error: Shift key harus berupa angka!")
                
        elif pilihan in ['3', '4']:
            keyword = input("Masukkan kata kunci (huruf): ")
            # Hapus spasi dari keyword kalau user iseng masukin spasi
            keyword = keyword.replace(" ", "")
            
            if not keyword.isalpha():
                print("\n[!] Error: Kata kunci harus berisi huruf saja!")
                continue
                
            if pilihan == '3':
                hasil = vigenere_encrypt(text, keyword)
                print(f"\n[+] Hasil Enkripsi : {hasil}")
            else:
                hasil = vigenere_decrypt(text, keyword)
                print(f"\n[-] Hasil Dekripsi : {hasil}")
