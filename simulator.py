# Se cargan los parametros desde parameters.txt
def load_parameters():
    parametros = {}
    with open('parameters.txt','r') as archivo:
        for linea in archivo:
            clave, valor = linea.strip().split("=")
            parametros[clave] = float(valor)
    return parametros

if __name__ == "__main__":
    params = load_parameters()
    print(params)
    
