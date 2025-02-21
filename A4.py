def palindromo(cadena):
    if len(cadena) <= 1:
        return True
    if cadena[0] == cadena[-1]:
        return palindromo(cadena[1:-1])
    return False

entrada = "reconocer"
print(palindromo(entrada))