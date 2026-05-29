# Se cargan los parametros desde parameters.txt
def load_parameters():
    params = {}
    with open('parameters.txt','r') as file:
        for line in file:
            key, value = line.strip().split("=")
            params[key] = float(value)
    return params 

if __name__ == "__main__":
    params = load_parameters()
    print(params)
    
