Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
key = 3;

def cipher_encrypt(plain_text):

    cipher_text='';
    plain_text = plain_text.upper();

    for c in plain_text:

        index = Alphabet.find(c);
        index = (index + key) % len(Alphabet);
        cipher_text = cipher_text + Alphabet[index];
    return cipher_text;

def cipher_decrypt(cipher_text):

    plain_text = '';
    for c in cipher_text:

        index = Alphabet.find(c);
        index = (index - key) % len(Alphabet);
        plain_text = plain_text + Alphabet[index];
    return plain_text;


plain_text = 'how are you'
cipher_text = cipher_encrypt(plain_text);
print(cipher_text);
plain_text = cipher_decrypt(cipher_text);
print(plain_text);
