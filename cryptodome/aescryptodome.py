import binascii
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad

def tohex(n):
	if n < 16:
		return '0'+hex(n)[-1] 
	else:
		return hex(n)[2:]

def affiche(L):
	print(list(map(tohex,L[0])))
	print(list(map(tohex,L[1])))
	print(list(map(tohex,L[2])))
	print(list(map(tohex,L[3])))
	print()
	

def convert_to_state(message):
	state = [0]*4
	for i in range(4):
		state[i] = [message[0:4][i],message[4:8][i],message[8:12][i],message[12:16][i]]
	return state


#Chiffrement ECB simple K fixé
#PARTIE_1
clair = b"Un message clair"
cle =   b"Ceci est une cle"

aesecb = AES.new(cle, AES.MODE_ECB)
cipher = aesecb.encrypt(clair)

ciphertext = convert_to_state(cipher)
print("PARTIE_1")
affiche(ciphertext)

#PARTIE_2
#Chiffrement CBC, longueur message multiple de 16
# IV fix'e donn'e sous forme d'une chaine hexa
clair = b"J'adore vraiment la cryptographie,bien plus que le developpement"
IV = "1234567890abcdef1234567890abcdef"

IV = binascii.unhexlify(IV)

aescbc = AES.new(cle, AES.MODE_CBC, iv=IV)
cipher = aescbc.encrypt(clair)
print("PARTIE_2")
for i in range(0, len(cipher), 16):
	bloc = cipher[i:i+16]
	ciphertext = convert_to_state(bloc)
	affiche(ciphertext)
	






#PARTIE_3
#chiffrement CBC, longueur du texte quelconque
# IV fix'e donn'e d'une chaine hexa
clair = b"voici un texte dont la longueur n'a aucune raison d'etre un multiple de 16 et qui necessite donc du padding."
IV = "1234567890abcdef1234567890abcdef"
print("PARTIE_3")

IV = binascii.unhexlify(IV)
aescbc = AES.new(cle, AES.MODE_CBC, iv=IV)
cipher = aescbc.encrypt(pad(clair, AES.block_size))


#VERIFICATION
aescbc = AES.new(cle, AES.MODE_CBC, iv=IV)
clairtext = unpad(aescbc.decrypt(cipher), AES.block_size)

print(clair == clairtext)





#PARTIE_4
#chiffrement CBC, longueur du texte quelconque
# IV g'en'er'e par la fonction encrypt
# Alice envoie IV concat'en'e avec le crypto
clair = b"voici un texte dont la longueur n'a aucune raison d'etre un multiple de 16 et qui necessite donc du padding."

print("\nPARTIE_4")
aescbc = AES.new(cle, AES.MODE_CBC)
cipher = aescbc.encrypt(pad(clair, AES.block_size))

ciphertext = aescbc.iv + cipher

aescbc = AES.new(cle, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
clairtext = unpad(aescbc.decrypt(ciphertext[AES.block_size:]), AES.block_size)
print(clairtext)




#chiffrement CBC, longueur du texte quelconque
# IV g'en'er'e par la fonction encrypt
# Alice envoie IV chiffr'e en mode ECB concat'en'e avec le crypto
clair = b"voici un texte dont la longueur n'a aucune raison d'etre un multiple de 16 et qui necessite donc du padding."

print("\nPARTIE_5")
IV = "1234567890abcdef1234567890abcdef"
IV = binascii.unhexlify(IV)
aesebc = AES.new(cle, AES.MODE_ECB)

IVcipher = aesebc.encrypt(IV)
aescbc = AES.new(cle, AES.MODE_CBC, iv=IVcipher)
cipher = aescbc.encrypt(pad(clair, AES.block_size))

ciphertext = IVcipher + cipher


aescbc = AES.new(cle, AES.MODE_CBC, iv=ciphertext[:AES.block_size])
clairtext = unpad(aescbc.decrypt(ciphertext[AES.block_size:]), AES.block_size)
print(clairtext)

