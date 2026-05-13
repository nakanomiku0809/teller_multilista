import csv
import files
class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None
        self.sub_list = None

class DobleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def leer(self, file_path):
        countries = DoubleLinkedList()
        colombia = Country("CO", "Colombia")
        countries.append(colombia)

        departments = {}

        with open(file_path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dept_code = row["cod_depto"]
                dept_name = row["departamento"]

                city_code = row["cod_mpio"]
                city_name = row["municipio"]

                lat = row["lat"]
                lon = row["lon"]

    def add_child(self, parent, child):
        if parent.sub_list is None:
            sublist = DoubleLinkedList()
            sublist.head = child
            sublist.tail = child
            parent.sub_list = sublist
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child

        return parent.sub_list
    
    def mostrar(self,level=0):
        if self.head is None:
            print("lista vacia")
            return
        while current:
            print(" "*level+str(current)
            if current.sublista:
                current.sublista.mostrar(level +1)
            current=current.next
    
    def buscar(self,attr,value):
        current=self.head

        