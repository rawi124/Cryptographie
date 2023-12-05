from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random.random import randrange
from Cryptodome.Util.number import inverse
import math

def get_e(phi_n):
    e = randrange(1, phi_n)
    while math.gcd(e, phi_n) != 1:
        e = randrange(1, phi_n)
    return e

def get_d(e, phi_n):
    return inverse(e, phi_n)
    
p = 4171849679533027504677776769862406473833407270227837441302815640277772901915313574263597828843

q = 5214812099416284380847220962328008092291759087784796801628519550347216127394141967829497285857

phi = (p-1)*(q-1)
e = get_e(phi)
d = get_d(e, phi)
print("e = ", e, " d = ", d)

#####################################################################
m = 5937088902777210702170118407838964396657014799511276368944229378900088074875217916968940725692083815174641415318313344353051645660075302117695865627738383

e = 479361040626881526661674029149900921690118916599896390474807785

n = 56177910464447372116540787212157022925561780591947080397946900361791461189219050978971399163252355006600035587459810424268371802754505194529014822074867579478853703804841362668599547866365103107744281040913063025333521282285105969845502608576507554360234694173363874933284518754573398661697290850260431476581

print("crypto = ", pow(m, e, n))
#####################################################################
c = 15085077818610232319096882572506406797007092461378884964143420704005072478075568111404783743557200545038982306288820567706495399713130248485751166422604691284718931040035040231030717756191


e = 510120241562372757078541216275919249838095303399514653805396983


p = 4171849679533027504677776769862406473833407270227837441302815640277772901915313574263597828111

q = 5214812099416284380847220962328008092291759087784796801628519550347216127394141967829497283919

d = inverse(e, (p-1)*(q-1))
print("clair = ", pow(c, d, p*q))


##############################RSA cryptodome########################
#*************************************************************************************************
#Generates a new RSA key pair here, used scrypt to thwart dictionary attacks
secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")  #PBKDF2WithHMAC-SHA1AndDES-EDE3-CBC

file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

"""
print(key.publickey().export_key())
print()
print(key.export_key())
"""

#*************************************************************************************************
#Read the private RSA key and print the public one
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)
#print("\n",key.publickey().export_key())


#*************************************************************************************************
#Generates an RSA key
key = RSA.generate(2048)

f = open("private.der", "wb") #private key
f.write(key.export_key()) #key.export_key('DER')
f.close()

f = open("receiver.der", "wb") #public key
f.write(key.publickey().export_key())
f.close()

#cle publique e, n cle privee n,d m = c exp d mod n et c = m exp e mod n 
#*************************************************************************************************
#CHIFFREMENT use public key
message = b'You can attack now!'
key = RSA.importKey(open('receiver.der').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print("Crypto: ",ciphertext)

#DECHIFFREMENT use private key
key = RSA.importKey(open('private.der').read())
cipher = PKCS1_OAEP.new(key)
message = cipher.decrypt(ciphertext)
print("\nClair: ",message)
