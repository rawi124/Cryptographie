#operations de decalage et astuces

MASK = x << n # cree une valeur avec x premiers bits de poids forts a un et le reste
                #donc n-x a zero


dernier = n & 1 # recupere la valeur du dernier bit de n
premier = (n >> len(n)) & 1 #recuperer la valeur du premier bit de n

left = (tempo >> 32)
right = tempo & MASK32 #decoupe un mot de 64 bits en deux blocs de 32 bits

bit = (entree >> pos ) & 1 #extrait le bit de la position pos

sortie = sortie | (bit << i) # ici le ou c est pour ajouter un nouveau bit 


