# import itertools

# def calculate_distance(city1, city2):
#     return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

# def total_distance(route, cities):
#     return sum(calculate_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

# def travelling_salesman(cities):
#     city_indices = list(range(len(cities)))
#     shortest_route = None
#     min_distance = float('inf')

#     for route in itertools.permutations(city_indices):
#         current_distance = total_distance(route + (route[0],), cities)
#         if current_distance < min_distance:
#             min_distance = current_distance
#             shortest_route = route

#     return shortest_route, min_distance

# # Example usage
# cities = [(0, 0), (1, 2), (2, 4), (3, 1)]
# route, distance = travelling_salesman(cities)
# print("Shortest route:", route)
# print("Minimum distance:", distance)

#------------------------------------------------------- For Better Visualization -----------------------------------------------------

import itertools
import matplotlib.pyplot as plt

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(route, cities):
    return sum(calculate_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

def travelling_salesman(cities):
    city_indices = list(range(len(cities)))
    shortest_route = None
    min_distance = float('inf')

    for route in itertools.permutations(city_indices):
        current_distance = total_distance(route + (route[0],), cities)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = route

    return shortest_route, min_distance

def plot_route(cities, route):
    x, y = zip(*[cities[i] for i in route] + [cities[route[0]]])  # Close the loop to return to the start
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o-', markersize=10, label="Cities & Route")
    for i, (x_coord, y_coord) in enumerate(cities):
        plt.text(x_coord, y_coord, f"{i}", fontsize=12, ha="center", va="center", color="black")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Travelling Salesman Problem - Shortest Route")
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
cities = [(0, 0), (1, 2), (2, 4), (3, 1)]
route, distance = travelling_salesman(cities)
print("Shortest route:", route)
print("Minimum distance:", distance)

# Plotting the route
plot_route(cities, route)
