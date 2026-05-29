import math

# Implementacion del metodo de Euler
def euler(qt, h, derivada):
  return qt + h * derivada ## y(t + h)

# Implementacion de la derivada
def ec_dif(t, h_nivel, hc, K1, K2, g, A):
  if h_nivel <= hc:

    return ((1/A) * (15 + 5 * math.cos(0.1 * t))) - ((1/A) * (K1 * math.sqrt(g * h_nivel)))
  else:

    return ((1/A) * (15 + 5 * math.cos(0.1 * t))) - ((1/A) * (K1 + K2) * math.sqrt(g * h_nivel))

