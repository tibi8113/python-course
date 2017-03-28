
poblacion = "Irun"

zonas = {"zona1" : 
            {
            "ida":2.0, 
            "ida-vuelta":2.0,
            "mensual":40, 
            "destinos":["Irun","Donostia"]
            },
        "zona2" : 
            {
            "ida":1.5, 
            "ida-vuelta":3.0,
            "mensual":45, 
            "destinos":["Tolosa","Alegi"]
            }
}

def min_precio(opc):
    min = []
    for z, v in zonas.items():
        min.append(v[opc])
    
    min.sort()
    return min[0]

def print_zonas():
    for z, v in zonas.items():
        print(z)
        print(v['destinos'])


def mi_zona(destino):
    for z, v in zonas.items():
        if destino in v["destinos"]:
            return z 
    
    return "No Zona"

def print_ordered():
    for z in sorted(zonas):
        print(z + ":")
        print(zonas[z])

#print_zonas()
#print(mi_zona("Alegifff"))
#print(min_precio("ida"))
print_ordered()
    