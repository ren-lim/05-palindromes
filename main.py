"""Notre objectif est de déterminer si un mot est un palyndrome ou non"""
import string
#### Fonction secondaire
def ispalindrome(p):
    """Cette fonction nous permet de tester si notre mot en paramètre est un palyndrome"""
    accent = "àâäéèêëîïôöûüùç"
    sans_accent = "aaaeeeeiioouuuc"
    suppr_espace = string.punctuation + " " + "’"
    translation_table = str.maketrans(accent, sans_accent, suppr_espace)
    p_minuscule = p.lower().translate(translation_table)
    return p_minuscule == p_minuscule[::-1]

#### Fonction principale
def main():
    """C'est notre  fonction principale qui teste ispalindrome()"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
