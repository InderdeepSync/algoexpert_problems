def valid_starting_city(distances, fuel, mpg):  # Verified on LeetCode
    def is_valid_starting_city(city_index):
        current_city = city_index
        prev_fuel = 0
        while True:
            prev_fuel = prev_fuel + fuel[current_city] - distances[current_city]
            if prev_fuel < 0:
                return False

            current_city = (current_city + 1) % len(cities)
            if current_city == city_index:
                return True

    cities = range(len(distances))

    for city in cities:
        if is_valid_starting_city(city):
            return city

    return -1


if __name__ == "__main__":
    print("Valid Starting City: {}".format(valid_starting_city(distances=[3, 4, 3], fuel=[2, 3, 4], mpg=1)))

