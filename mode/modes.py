import des_skel as des

def convert_text_bin(texte):
    """
    """
    result = list(format(c, 'b') for c in bytearray(texte, "utf-8"))
    return result

def decoupage(texte, taille):
    """
    """
    i = 0
    while i < len(binaire) :
        decoupe.append(binaire[i:taille])
        taille += taille
        i += taille
    return decoupe
    

def mode_ecb(texte, cle, taille):
    """
    """
    binaire = convert_text_bin(texte)
    decoupe = decoupage(texte, taille)
    encrypt = []
    for el in decoupe :
        enrypt.append(des.standard_des(el, cle))
    return encrypt

def mode_cbc(texte, cle, taille, iv):
    """
    """
    binaire = convert_text_bin(texte)
    decoupe = decoupage(texte, taille)
    encrypt = []
    for el in decoupe :
        tmp = el ^ iv
        iv = des.standard_des(tmp, cle)
        encrypt.append(iv)
    return encrypt

def mode_ctr(texte, cle, taille, compteur):
    """
    """
    binaire = convert_text_bin(texte)
    decoupe = decoupage(texte, taille)
    encrypt = []
    i = 0
    while i < len(decoupe) :
        tmp = des.standard_des(compteur[i], cle)
        encrypt.append(tmp ^ decoupe[i])
    return encrypt

def mode_cfb(texte, cle, taille, compteur):
    """
    """
    binaire = convert_text_bin(texte)
    decoupe = decoupage(texte, taille)
    encrypt = []
    i = 0
    while i < len(decoupe) :
        tmp = des.standard_des(compteur, cle)
        compteur = tmp ^ decoupe[i]
        encrypt.append(compteur)
    return encrypt


def mode_ofb(texte, cle, taille, compteur):
    """
    """
    binaire = convert_text_bin(texte)
    decoupe = decoupage(texte, taille)
    encrypt = []
    i = 0
    while i < len(decoupe) :
        tmp = des.standard_des(compteur, cle)
        compteur = tmp ^ decoupe[i]
        encrypt.append(compteur)
        compteur = tmp
    return encrypt


    
    
    
    
