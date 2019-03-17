from Crypto.Cipher import AES
import base64

pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

#########################################
# Should really choose key randomly, but 
# md5 gives me a value that has the right
# length. What should I use...?
#
# Monkeys rule!
#
# Todo: Look it up. No time today!
#
#########################################
key = ''


mode = AES.MODE_ECB
encryptor = AES.new(key, mode)
text = ''
ciphertext = encryptor.encrypt(pad(text))

###################
# debug
###################
print base64.b64encode(ciphertext)

