from node import Node


class City(Node):
    def __init__(self, id, name, lat=None, lon=None):
        super().__init__(id, name)
        self.lat = self.convert_float(lat)
        self.lon = self.convert_float(lon)

    def convert_float(self, value):
        if value is None:
            return None

        value = str(value).strip()
        value = value.replace('"', "")
        value = value.replace(",", ".")

        if value == "":
            return None

        try:
            return float(value)
        except ValueError:
            return None
