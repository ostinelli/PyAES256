# AES-256 cryptographic library for Python EXAMPLE USE

import aes256

# set clear text
text = "My testing clear text"

# define a 32-bytes string
key = "aserghjerg4w5ygb8JHBr8ySuhrergiE"

# encrypt
encrypted = aes256.encrypt(text, key)

# decrypt
decrypted = aes256.decrypt(encrypted, key)

# display
print "CLEAR TEXT: %s" % text
print "DECRYPTED TEXT: %s" % decrypted
