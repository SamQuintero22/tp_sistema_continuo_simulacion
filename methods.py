import math

# Implementacion del metodo de Euler
def euler(qt, h, derivada):
  return qt + h * derivada ## y(t + h)

# Implementacion de la derivada
def ec_dif(t, h_nivel, hc, K1, K2, g, A):
  f_entrada = 15 + 5 * math.cos(0.1 * t)
  if h_nivel <= hc:
    f_salida = K1 * math.sqrt(g * h_nivel)
  else:
    f_salida = (K1 + K2) * math.sqrt(g * h_nivel)

  return (1/A) * f_entrada - (1/A) * f_salida

