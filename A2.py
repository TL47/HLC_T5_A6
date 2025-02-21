import random
def contraseña():
    valores = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789[]{,}|@#~\€¬!·$%&/()=?¿¡!^*¨Ç_:;,.-"
    longitud = 8
    contraseña = ''
    for i in range(longitud):
        contraseña += valores[random.randint(0, len(valores)-1)]

    return contraseña

print(contraseña())