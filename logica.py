import csv

class Node:
    def __init__(self, id, name, lat=None, lon=None):
        self.id = id
        self.name = name
        self.lat = lat
        self.lon = lon
        self.next = None
        self.prev = None
        self.sub_list = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def cargar_todo():
    paises = LinkedList()
    
    colombia = Node("0", "Colombia")
    paises.head = colombia
    paises.tail = colombia
    colombia.sub_list = LinkedList()
    
    archivo = open('DIVIPOLA-_C_digos_municipios_20250505.csv', mode='r', encoding='utf-8')
    lector = csv.reader(archivo)
    next(lector)
    
    for fila in lector:
        try:
            id_dep = fila[0]
            nom_dep = fila[1]
            id_mun = fila[2]
            nom_mun = fila[3]
            
            longitud_temp = float(fila[5].replace(',', '.'))
            latitud_temp = float(fila[6].replace(',', '.'))
        except:
            continue

        actual_d = colombia.sub_list.head
        encontrado_d = None
        
        while actual_d != None:
            if actual_d.id == id_dep:
                encontrado_d = actual_d
                break
            actual_d = actual_d.next
            
        if encontrado_d == None:
            nuevo_d = Node(id_dep, nom_dep)
            nuevo_d.sub_list = LinkedList()
            
            if colombia.sub_list.head == None:
                colombia.sub_list.head = nuevo_d
                colombia.sub_list.tail = nuevo_d
            else:
                nuevo_d.prev = colombia.sub_list.tail
                colombia.sub_list.tail.next = nuevo_d
                colombia.sub_list.tail = nuevo_d
            encontrado_d = nuevo_d
            
        nuevo_m = Node(id_mun, nom_mun, latitud_temp, longitud_temp)
        
        if encontrado_d.sub_list.head == None:
            encontrado_d.sub_list.head = nuevo_m
            encontrado_d.sub_list.tail = nuevo_m
        else:
            nuevo_m.prev = encontrado_d.sub_list.tail
            encontrado_d.sub_list.tail.next = nuevo_m
            encontrado_d.sub_list.tail = nuevo_m
            
    archivo.close()
    return paises

def pasar_a_diccionario(lista_p):
    resultado = {"paises": []}
    p = lista_p.head
    while p != None:
        datos_p = {"nombre": p.name, "deptos": []}
        if p.sub_list != None:
            d = p.sub_list.head
            while d != None:
                datos_d = {"nombre": d.name, "municipios": []}
                if d.sub_list != None:
                    m = d.sub_list.head
                    while m != None:
                        datos_m = {"n": m.name, "la": m.lat, "lo": m.lon}
                        datos_d["municipios"].append(datos_m)
                        m = m.next
                datos_p["deptos"].append(datos_d)
                d = d.next
        resultado["paises"].append(datos_p)
        p = p.next
    return resultado