import random

def encrypt(text, alphabet, substitution):
    """Функция шифрования"""
    encrypted_text = ""

    for char in text:
        if char in alphabet:
            encrypted_text += substitution[alphabet.index(char)]
        else:
            encrypted_text += char  # Символы вне алфавита остаются неизменными

    return encrypted_text

def decrypt(encrypted_text, alphabet, substitution):
    """Функция дешифрования"""
    decrypted_text = ""

    for char in encrypted_text:
        if char in substitution:
            decrypted_text += alphabet[substitution.index(char)]
        else:
            decrypted_text += char  # Символы вне алфавита остаются неизменными

    return decrypted_text

if __name__ == "__main__":
    # Исходный алфавит и подстановка
    alphabet = [' '] + [chr(i) for i in range(1040, 1072)] + ['b']  # Русские буквы + пробел + символ 'b'
    substitution = alphabet[:]
    random.shuffle(substitution)

    # Текст для шифрования
    input_text = " АЯУЛЫМ "
    print(f"Исходный текст: {input_text}")

    # Шифрование
    encrypted_text = encrypt(input_text, alphabet, substitution)
    print(f"Зашифрованный текст: {encrypted_text}")

    # Дешифрование
    decrypted_text = decrypt(encrypted_text, alphabet, substitution)
    print(f"Расшифрованный текст: {decrypted_text}")
