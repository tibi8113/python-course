''' precio por zonas
http://www.renfe.com/viajeros/cercanias/sansebastian/abonos_y_descuentos/index.html
'''
prices = {
    "go" : [1.70, 1.90, 2.60, 3.35, 3.80, 5.0],
    "return" : [2.60, 2.75, 4.10, 5.50, 6.40, 8.0],
    "monthly" : [34.45, 43.95, 58.65, 73.30, 85.80, 91.0]
}
zones = {
    "zone1" : ["Urnieta", "Hernani-Center", "Hernani", "Martutene", "Loiola", "Donostia", "Gros", "Ategorrieta", "Intxaurrondo", "Herrera", "Pasaia", "Lezo-Errenteria"],
    "zone2" : ["Billabona-Zizurkil", "Andoain-Center", "Andoain", "Urnieta", "Lezo-Errenteria", "Irun-Bentak", "Irun"],
    "zone3" : ["Alegia", "Tolosa", "Tolosa-Erdia", "Anoeta", "Billabona-Zizurkil"],
    "zone4" : ["Beasain", "Ordizia", "Itsasondo", "Legorreta", "Ikaztegieta", "Alegia"],
    "zone5" : ["Legazpi", "Zumarraga", "Ormaiztegi"],
    "zone6" : ["Brinkola", "Legazpi"]
}


def get_prices(num_zonas):
    ''' num_zonas [1-6] '''
    if num_zonas >= 1 and num_zonas <= 6:
        return prices[num_zonas - 1]
    else:
        return -1


def get_stations():
    s = []  # all stations list
    for zone, stations in zones.items():
        for station in stations:
            s.append(station)
    return s


def print_opt_menu():
    """ print menu and return the option """
    msg = "a)Go\tb)Return\tc)Monthly\n\n"
    opt = input(msg)
    
    if opt == "a":  # only go
        opt = "go"
    elif opt == "b":    # return
        opt = "return"
    elif opt == "c":    # monthly
        opt = "monthly"
    else:   # monthly
        opt = "error"
    
    return opt


def print_prices():
    """ print prices """
    print(prices)


def get_zones():
    return zones


def print_zones():
    """ print zones """
    print(zones)


def get_zones_of_station(station):
    # return the zone or zones of a station
    zs = []
    for zone, stations in zones.items():
        for s in stations:
            if s == station:
                zs.append(zone)

    return zs


def get_price(option, mystation, targetstation):
    ''' with option(go|return|monthly) and target station return the price '''
    
    price = -1
    
    mystation_zones = get_zones_of_station(mystation)
    target_zones = get_zones_of_station(targetstation)
    # sort?
    
    # how many zones?
    # one
    '''
    for myzones in mystation_zones:
        if myzones in target_zones:
            return prices[option][0]
    '''
    # more than one
    # idea: 
    #   int("zone3"[4:])) = 3
    #   int("zone5"[4:])) = 5
    #   distance = 5-3 = 2
    #   price[2]
    distances = []
    for z in mystation_zones:
        for tz in target_zones:
            x = abs(int(z[4:]) - int(tz[4:]))
            distances.append(x)

    distances.sort()

    # return the price of lowest distance
    return prices[option][distances[0]]