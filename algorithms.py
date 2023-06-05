from random import seed, randint

class __crypt:
    """A way of encrypting and decrypting text in an ASCII way"""
    
    def encrypt(text, key):
        """Encrypts the text, key is used as seed and must be given"""
        seed(key)
        if not isinstance(text, str):
            raise TypeError("{} should be a type string".format(text))
        return "".join([chr(ord(something) + randint(1,randint(2,10))) for something in text])
    
    def decrypt(text, key):
        """Decrypts the text, key is used as seed and must be given and must be the same as the encryption."""
        seed(key)
        if not isinstance(text, str):
            raise TypeError("{} should be a type string".format(text))
        return "".join([chr(ord(something) - randint(1,randint(2,10))) for something in text])
    
if __name__ == '__main__':
    text = input("Put in some text to encrypt: ")
    key = input("Put in a key: ")

    print(f"Encrypted: {__crypt.encrypt(text, key)}")
