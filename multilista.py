class Node:
    def __init__(self,data):
        self.data=data
        self.head=None
        self.tail=None
        self.sublista=None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def leer():
        lista = []
        with open("DIVIPOLA-_C_digos_municipios_20250505.csv", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                Node = Node(
                    int(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6])
                )
                lista.append(Node)
        return lista
    def añadir(self,Node,data):
        data=lista
        for lista in 1:
            if Node.sublista==None:
                sublista=LinkedList()
                sublista.head=data
                sublista.tail=data
                Node.sublista=sublista
            else:
                current=Node.sublista.tail
                current.next=data
                data.prev=current
                Node.subllista.tail=data
        return Node.sublista