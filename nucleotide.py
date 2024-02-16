def nucleotide2code(ch):
    if ch=='c' or ch=="C":
        return 0
    if ch=='t' or ch=="T":
        return 1
    if ch=='a' or ch=="A":
        return 2
    if ch=='g' or ch=="G":
        return 3
    return None

def code2nucleotide(code):
    if code == 0:
        return "C"    
    if code == 1:
        return "T"    
    if code == 2:
        return "A"    
    if code == 3:
        return "G"
    return None