""" RENFE """
import renfefunctions as rf

my_station = "Irun"

def main():
    
    print(my_station.upper())
    print("----------------")
    # option (go | return | monthly)
    while True:
        opt = rf.print_opt_menu()
        if opt != "error":
            break
    
    print("Option: " + opt)

    # select station
    stations = rf.get_stations()
    print(stations)
    station = input("Select station:")
    # try if station exist
    while True:
        try:
            stations.index(station)
            break
        except ValueError:
            print("Error: incorrect station!!")
            print(stations)
            station = input("Select station:")

    # price
    print("\n\n\nthe price (" + opt + ") From " + my_station + " to " + station + " is:")
    print(rf.get_price(opt, my_station, station))

if __name__ == '__main__':
    # for debug
    #print(rf.get_price("monthly", "Tolosa", "Donostia"))
    # main program
    main()
