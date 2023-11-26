from Cryptodome.Hash import SHAKE128
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode


print("***************************** MODE CBC ****************************\n")
K = 23735572912396822947448854887371177533556817454199328740290936514978928422648571598726918832566357785110928613965466311127895906957098549984592019275697986789578336153697648585363213040767212132272276282916881121661684773948926589923941382890369368944863959960813599345724948446127851792805845934439925016475

K_shake = SHAKE128.new()
K_bytes = int.to_bytes(K, byteorder="big", length=128) 

K_shake.update(K_bytes)
cle = K_shake.read(16)
print("cle",cle)

#CHIFFREMENT
clair = b"vraiment tu es une tete a claque mais je tadore jespere que tu vas bien t'installer a toulouse madame capgemini"

aesecb = AES.new(cle, AES.MODE_ECB)
aescbc = AES.new(cle, AES.MODE_CBC)

IVcipher = aesecb.encrypt(aescbc.iv)
cipher = aescbc.encrypt(pad(clair, AES.block_size))

ciphertext = IVcipher + cipher
cipher = b64encode(ciphertext).decode('utf-8')
print("\ncipher = ",cipher)

#DECHIFFREMENT
ciphertext = 'h1af648jKULTpDmzvRZYbjXF/28B76JZc9IGycruU1mscRlwLcE5OTbg+3Zn+IYDS9a7phMy9PLD4ifU+N5GcvpzlrfbrVazCy3wf2kNHKgWabJSVkmWVsLWcO0Ikza0oOf7jjHiNbQ4b3YWr4MtOH1fUaEYYJ/gEuCrj4j/D383B4Bt5whZKvXTxcwpw/i4'

cipher = b64decode(ciphertext)
aesecb = AES.new(cle, AES.MODE_ECB)
IV = aesecb.decrypt(cipher[:AES.block_size])

aescbc = AES.new(cle, AES.MODE_CBC, iv=IV)
clairtext = unpad(aescbc.decrypt(cipher[AES.block_size:]), AES.block_size)
print("\nclair = ",clairtext)




