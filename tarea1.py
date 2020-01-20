import time

temperatura_actual = 0
limite = 230

if __name__ == "__main__":
    while True:
        # temperatura_actual = 
        if temperatura_actual > limite:
            # TODO encender los venitladores
            pass
        elif temperatura_actual <= limite:
            """ Función para el gas
            y = -0.43478 x + 100 
            """
            # TODO darle gas 
            pass
        time.sleep(1)
