message ="Ceci est un message de 111 caracteres (888 bits) a signer avec le RSA sans prendre en compte le formattage OAEP"
signature = 0x4f11175df7c0508c2d38eaad65ce537eea7b73deda23d9c432be5d716dde9161c307134737fc73548d69ade7ab7d98ddbdf0d422f0d8ec217b87ec9f3c1fe4f77388df1892612c9f711cabe4f7a6 
n = 21755412185774780362325532940389114975420134102099227574249231900688529811900507862596096103954962020367271336407573427087654824977661206378805646778893998689425716957148629735888664015091

e = 244639737139442129145538993636009925449005706539865025922916045
import hashlib


def verif_sig(m,s,e,n):
    h = hashlib.sha256()
    h.update(bytes(m.encode('utf-8')))
    h = int(h.hexdigest(),16)
    res = pow(s, e, n)
    if res == h :
        print("True")
    else :
        print("False")
verif_sig(message, signature, e, n)
