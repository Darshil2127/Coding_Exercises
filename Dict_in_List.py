travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country_visited, visits_total, cities_names):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = visits_total
    new_country["cities"] = cities_names
    print(new_country)
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint petersburg"])


print(travel_log)