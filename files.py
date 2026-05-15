import csv
import glob
import unicodedata

from doublelinklist import DoubleLinkedList
from country import Country
from department import Department
from city import City


class Files:
    def normalize(self, text):
        text = str(text).strip().lower()
        text = unicodedata.normalize("NFKD", text)
        text = "".join(letter for letter in text if not unicodedata.combining(letter))
        text = text.replace(":", "")
        text = text.replace("_", " ")
        text = " ".join(text.split())
        return text

    def get_value(self, row, names):
        clean_row = {}

        for key, value in row.items():
            clean_row[self.normalize(key)] = value

        for name in names:
            clean_name = self.normalize(name)

            if clean_name in clean_row:
                return clean_row[clean_name]

        return None

    def find_csv(self):
        csv_files = glob.glob("DIVIPOLA*.csv")

        if len(csv_files) == 0:
            csv_files = glob.glob("*.csv")

        if len(csv_files) == 0:
            raise FileNotFoundError("No se encontro ningun archivo csv")

        return csv_files[0]

    def read_divipola(self, file_path=None):
        if file_path is None:
            file_path = self.find_csv()

        print("Leyendo archivo:", file_path)

        countries = DoubleLinkedList()
        colombia = Country("CO", "Colombia")
        countries.append(colombia)

        departments = {}

        with open(file_path, encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                dept_code = self.get_value(row, [
                    "Codigo Departamento",
                    "Código Departamento",
                    "cod depto",
                    "cod_depto"
                ])

                dept_name = self.get_value(row, [
                    "Nombre Departamento",
                    "departamento"
                ])

                city_code = self.get_value(row, [
                    "Codigo Municipio",
                    "Código Municipio",
                    "cod municipio",
                    "cod_mpio"
                ])

                city_name = self.get_value(row, [
                    "Nombre Municipio",
                    "municipio"
                ])

                lon = self.get_value(row, [
                    "Longitud",
                    "lon",
                    "lng"
                ])

                lat = self.get_value(row, [
                    "Latitud",
                    "lat"
                ])

                if dept_code is None or dept_name is None or city_code is None or city_name is None:
                    continue

                if dept_code not in departments:
                    department = Department(dept_code, dept_name)
                    countries.add_child(colombia, department)
                    departments[dept_code] = department

                city = City(city_code, city_name, lat, lon)
                countries.add_child(departments[dept_code], city)

        return countries

    def get_markers(self, multilist):
        markers = []
        country = multilist.head

        while country is not None:
            if country.sub_list is not None:
                department = country.sub_list.head
            else:
                department = None

            while department is not None:
                if department.sub_list is not None:
                    city = department.sub_list.head
                else:
                    city = None

                while city is not None:
                    if city.lat is not None and city.lon is not None:
                        markers.append({
                            "name": city.name,
                            "department": department.name,
                            "lat": city.lat,
                            "lon": city.lon
                        })

                    city = city.next

                department = department.next

            country = country.next

        return markers

    def to_json(self, multilist):
        data = []
        country = multilist.head

        while country is not None:
            country_data = {
                "id": country.id,
                "name": country.name,
                "departments": []
            }

            if country.sub_list is not None:
                department = country.sub_list.head
            else:
                department = None

            while department is not None:
                department_data = {
                    "id": department.id,
                    "name": department.name,
                    "municipalities": []
                }

                if department.sub_list is not None:
                    city = department.sub_list.head
                else:
                    city = None

                while city is not None:
                    department_data["municipalities"].append({
                        "id": city.id,
                        "name": city.name,
                        "lat": city.lat,
                        "lon": city.lon
                    })

                    city = city.next

                country_data["departments"].append(department_data)
                department = department.next

            data.append(country_data)
            country = country.next

        return data
