def convert_text_bin(texte):
    """
    """
    result = list(format(c, 'b') for c in bytearray(texte, "utf-8"))
    return result

def mode_ecb(texte, cle, taille):
    """
    """
    binaire = convert_text_bin(texte)
    decoupe = []
    i = 0
    while i < len(binaire) :
        decoupe.append(binaire[i:taille])
        taille += taille
        i += taille
    return decoupe
print(mode_ecb("raraerzetzetgrfgbfdhrthtryhtjuytj", 0x1123456789abcdef, 10))
