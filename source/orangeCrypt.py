
def ENCRYPT(text,x):
    encrypted_word = ""
    for char in text:
        char = ord(char)
        char += x
        char = chr(char)
        encrypted_word += char
    return encrypted_word

def DECRYPT(text,x):
    decrypted_word = ""
    for char in text:
        char = ord(char)
        char -= x
        char = chr(char)
        decrypted_word += char
    return decrypted_word
    