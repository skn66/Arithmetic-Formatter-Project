# to encrypt and decrypt the message 
text = "mrttaqrhknsw ih puggrur"
custom_key = 'happycoding'

def code(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else: 
            key_char = key[key_index % len(key)]
            key_index += 1


            offset = alphabet.index(key_char.lower())
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return code(message, key, 1)

def decrypt(message, key):
    return code(message, key, -1)

print(f'\nEncrypt text : {text}')
print(f'Key :{custom_key}')

decryption = decrypt(text,custom_key)
print(f'Decrypt text:{decryption}\n')

