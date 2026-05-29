import math
from methods import euler, heun, ec_dif
import matplotlib.pyplot as plt

# Se cargan los parametros desde parameters.txt
def load_parameters():
    parametros = {}
    with open('parameters.txt','r') as archivo:
        for linea in archivo:
            clave, valor = linea.strip().split("=")
            parametros[clave] = float(valor)
    return parametros

def simular(metodo):
    parametros = load_parameters()
    # inicializacion de variables
    tiempo_total = parametros['T']
    paso_integracion = parametros['h']
    altura_critica = parametros['Hc']
    valvula_K1 = parametros['K1']
    valvula_K2 = parametros['K2']
    gravedad = parametros['g']
    area = parametros['A']

    # estado inicial 
    tiempo = 0
    altura = parametros['h0']
    cantidad_pasos = int(tiempo_total / paso_integracion) + 1    
    # lista para almacenar resultados 
    tiempos = [0.0] * cantidad_pasos # 2000 posiciones para almacenar los tiempos
    alturas = [0.0] * cantidad_pasos 
    f_entradas = [0.0] * cantidad_pasos
    f_salidas = [0.0] * cantidad_pasos

    tiempos[0] = tiempo
    alturas[0] = altura 
    f_entradas[0] = 15 + 5 * math.cos(0.1 * 0)  # = 20
    f_salidas[0]  = valvula_K1 * math.sqrt(gravedad * altura)
    i = 1
    while tiempo < tiempo_total: 
        tiempo = round(tiempo + paso_integracion, 2) # Evita errores de precision acumulados
        
        if metodo == 'euler':
            derivada = ec_dif(alturas[i-1], tiempo, altura_critica, valvula_K1, valvula_K2, gravedad, area)
            altura = euler(alturas[i-1], paso_integracion,derivada)
        elif metodo == 'heun': 
            altura = heun(alturas[i-1], tiempo, altura_critica, valvula_K1, valvula_K2, gravedad, area, paso_integracion)
        
        if altura < 0: # Control de no negatividad por si cambiamos parametros
            altura = 0

        tiempos[i] = tiempo
        alturas[i] = altura 
        f_entradas[i] = 15 + 5 * math.cos(0.1 * tiempo)
        if alturas[i] <= altura_critica:
            f_salidas[i] = valvula_K1 * math.sqrt(gravedad * alturas[i])
        else:
            f_salidas[i] = (valvula_K1 + valvula_K2) * math.sqrt(gravedad * alturas[i])        
        i += 1

    return tiempos, alturas, f_entradas, f_salidas

def graficar(tiempos, alturas, f_entradas, f_salidas, altura_critica):
    fig, (grafico1, grafico2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    # Gráfico 1 - altura
    grafico1.plot(tiempos, alturas, 'b-', label='h(t)')
    grafico1.axhline(y=altura_critica, color='r', linestyle='--', label=f'hc = {altura_critica}')
    grafico1.set_ylabel('Altura (m)')
    grafico1.set_title('Evolución del nivel h(t)')
    grafico1.legend()
    grafico1.grid(True)

    # Gráfico 2 - flujos
    grafico2.plot(tiempos, f_entradas, 'g-', label='F_entrada(t)')
    grafico2.plot(tiempos, f_salidas,  'r-', label='F_salida(t)')
    grafico2.set_ylabel('Flujo (m³/s)')
    grafico2.set_xlabel('Tiempo')
    grafico2.set_title('Flujos de entrada y salida')
    grafico2.legend()
    grafico2.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tiempos,alturas,f_entrada,f_salida = simular('euler')
    graficar(tiempos,alturas,f_entrada,f_salida, 20.0)