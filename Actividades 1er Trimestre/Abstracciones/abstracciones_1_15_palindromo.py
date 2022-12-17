"dasdasd"
palindrome = lambda x : \
    x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")).replace(" ", "").lower() == \
    x.translate(x.maketrans("áéíóúÁÉÍÓÚ","aeiouAEIOU")).replace(" ", "").lower()[::-1]
