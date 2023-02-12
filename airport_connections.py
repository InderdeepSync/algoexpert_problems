def airport_connections(airports, routes, start):
    pass


if __name__ == "__main__":
    airports_list = [
        "BGI",
        "CDG",
        "DEL",
        "DOH",
        "DSM",
        "EWR",
        "EYW",
        "HDN",
        "ICN",
        "JFK",
        "LGA",
        "LHR",
        "ORD",
        "SAN",
        "SFO",
        "SIN",
        "TLV",
        "BUD",
    ]
    routes = [
         ["DSM", "ORD"],
         ["ORD", "BGI"],
         ["BGI", "LGA"],
         ["SIN", "CDG"],
         ["CDG", "SIN"],
         ["CDG", "BUD"],
         ["DEL", "DOH"],
         ["DEL", "CDG"],
         ["TLV", "DEL"],
         ["EWR", "HND"],
         ["HND", "ICN"],
         ["HND", "JFK"],
         ["ICN", "JFK"],
         ["JFK", "LGA"],
         ["EYW", "LHR"],
         ["LHR", "SFO"],
         ["SFO", "SAN"],
         ["SFO", "DSM"],
         ["SAN", "EYW"]
    ],
    print("Airport Connections: {}".format(airport_connections(airports_list, routes, "LGA")))
