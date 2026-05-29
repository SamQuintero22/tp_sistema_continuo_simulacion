import math

# Implementacion del metodo de Euler
def euler(altura_actual, paso_integracion, derivada):
  return altura_actual + paso_integracion * derivada ## y(t + h)

# Implementacion de la derivada
def ec_dif(altura_actual, tiempo, altura_critica, K1, K2, gravedad, area):
  f_entrada = 15 + 5 * math.cos(0.1 * tiempo)
  if altura_actual <= altura_critica:
    f_salida = K1 * math.sqrt(gravedad * altura_actual)
  else:
    f_salida = (K1 + K2) * math.sqrt(gravedad * altura_actual)

  return (1/area) * f_entrada - (1/area) * f_salida

# Implementacion del metodo Heun
def heun(altura_actual, tiempo, altura_critica, K1, K2, gravedad, area, paso_integracion):
    
    # primer derivada
    k1 = ec_dif(altura_actual, tiempo, altura_critica, K1, K2, gravedad, area)

    # calculo auxiliar Euler (Xk + h*k1)
    altura_euler = altura_actual + paso_integracion * k1

    # segunda derivada, usando la estimacion 
    k2 = ec_dif(altura_euler, tiempo + paso_integracion, altura_critica, K1, K2, gravedad, area)
    
    # promedio de las dos derivadas
    return altura_actual + 0.5 * paso_integracion * (k1 + k2)

