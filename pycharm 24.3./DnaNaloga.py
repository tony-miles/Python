dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

# Barva las: #

print dna.count("CCAGCAATCGC")  # Crna: 0 #
print dna.count("GCCAGTGCCG")                       # Rjava: 1 #
print dna.count("TTAGCTATCGC")   # Korencek: 0 #

# Oblika obraza: #

print dna.count("GCCACGG")                        # Kvadraten: 1 #
print dna.count("ACCACAA")  # Okrogel: 0 #
print dna.count("AGGCCTCA")  # Ovalen: 0 #

#Barva oci:#

print dna.count("TTGTGGTGGC")   # Modra:0 #
print dna.count("GGGAGGTGGC")                       # Zelena:1#
print dna.count("AAGTAGTGAC")  # Rjava:0 #

# Spol: #

print dna.count("TGCAGGAACTTC")                       # Moski:1 #
print dna.count("TGAAGGACCTTC")  # Zenska:0 #

# Rasa: #

print dna.count("AAAACCTCA")                          # Belec:1 #
print dna.count("CGACTACAG")  # Crnec:0 #
print dna.count("CGCGGGCCG")  # Azijec:0 #

# profil ustreza: belec, moski, zelene oci, kvadratne oblike obraza, rjave barve las #