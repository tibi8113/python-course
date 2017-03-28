''' Renfe OOP Classes '''

class Renfe:
    
    _prices = {
        "go" : [1.70, 1.90, 2.60, 3.35, 3.80, 5.0],
        "return" : [2.60, 2.75, 4.10, 5.50, 6.40, 8.0],
        "monthly" : [34.45, 43.95, 58.65, 73.30, 85.80, 91.0]
    }
    _zones = {
        "zone1" : ["Urnieta", "Hernani-Center", "Hernani", "Martutene", "Loiola", "Donostia", "Gros", "Ategorrieta", "Intxaurrondo", "Herrera", "Pasaia", "Lezo-Errenteria"],
        "zone2" : ["Billabona-Zizurkil", "Andoain-Center", "Andoain", "Urnieta", "Lezo-Errenteria", "Irun-Bentak", "Irun"],
        "zone3" : ["Alegia", "Tolosa", "Tolosa-Erdia", "Anoeta", "Billabona-Zizurkil"],
        "zone4" : ["Beasain", "Ordizia", "Itsasondo", "Legorreta", "Ikaztegieta", "Alegia"],
        "zone5" : ["Legazpi", "Zumarraga", "Ormaiztegi"],
        "zone6" : ["Brinkola", "Legazpi"]
    }

    def get_prices(self):
        pass

class Station:
    pass


class Zone:
    pass