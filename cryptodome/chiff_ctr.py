from Cryptodome.Hash import SHAKE128
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode


print("***************************** MODE CTR ****************************\n")
K = 23735572912396822947448854887371177533556817454199328740290936514978928422648571598726918832566357785110928613965466311127895906957098549984592019275697986789578336153697648585363213040767212132272276282916881121661684773948926589923941382890369368944863959960813599345724948446127851792805845934439925016475

K_shake = SHAKE128.new()
K_bytes = int.to_bytes(K, byteorder="big", length=128) 

K_shake.update(K_bytes)
cle = K_shake.read(16)
print("cle",cle)



#CHIFFREMENT
clair = b"vraiment tu es une tete a claque mais je tadore jespere que tu vas bien t'installer a toulouse madame capgemini"

aesecb = AES.new(cle, AES.MODE_ECB)
aesctr = AES.new(cle, AES.MODE_CTR)

nonceCipher = aesecb.encrypt(pad(aesctr.nonce, AES.block_size))
cipher = aesctr.encrypt(pad(clair, AES.block_size))

ciphertext = nonceCipher + cipher
cipher = b64encode(ciphertext).decode('utf-8')
print("\ncipher = ",cipher)


#DECHIFFREMENT
ciphertext = '6DPb7ZffxzNLmCDnPsFH8QRjSXfLSvJaHYZBcobvfzB0kFiiIx4tkF9DPd/e9sATJwvUMYT3QQl4hriSuE2IXvoAwqPL6X0hubM2of4z3OTnRA7wY4VXRyYwOH4n3Wb7EQExa9ZQhf3qS1ExtEqylCetP93qoLyfzrAdg7Ebhgzzd4uxRXpDqJsn0FwRpJnl'

cipher = b64decode(ciphertext)
aesecb = AES.new(cle, AES.MODE_ECB)
nonceC = unpad(aesecb.decrypt(cipher[:AES.block_size]), AES.block_size)

aesctr = AES.new(cle, AES.MODE_CTR, nonce=nonceC)
clairtext = unpad(aesctr.decrypt(cipher[AES.block_size:]), AES.block_size)
print("\nclair = ",clairtext)




