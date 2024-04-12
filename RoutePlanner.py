import math
import queue

class RoutePlanner:

    def __init__(self, startLocation, desiredDestination, graph) -> None:
        """
        Initialize a RoutePlanner object.

        Args:
        - startLocation: The starting location
        - desiredDestination: The desired destination
        - graph: The graph containing location information

        Returns:
        - None
        """
        self.graph = graph
        self.infinity = math.inf
        self.startLocation = startLocation
        self.desiredDestination = desiredDestination

    def haversine_distance(self, loc, des) -> float:
        """
        Calculate the Haversine distance between two geographical coordinates.

        Args:
        - loc: The coordinates of the current location
        - des: The coordinates of the destination

        Returns:
        - The Haversine distance between the two coordinates
        """
        lat1, lon1 = loc
        lat2, lon2 = des
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        radius = 6371 
        distance = radius * c * 1000  
        return distance

    def get_neighbours(self, location) -> list[str]:
        """
        Get the neighboring locations of a given location.

        Args:
        - location: The location to find neighbors for

        Returns:
        - A list of neighboring locations
        """
        return list(self.graph.nodes[location].paths.keys())

    def check_penalty(self, location, destination) -> tuple[float, float]:
        """
        Check penalty for traversing from one location to another.

        Args:
        - location: The current location
        - destination: The destination location

        Returns:
        - The distance and penalty for traversing between the two locations
        """
        path = self.graph.get_path(location, destination)
        penalty = 1
        if path.is_slope: penalty += 0.3
        if not path.is_paved: penalty += 0.4 
        return path.distance, penalty

    def path_cost(self, cost_so_far, location, destination) -> float:
        """
        Calculate the cost of traversing from one location to another.

        Args:
        - cost_so_far: The cost accumulated so far
        - location: The current location
        - destination: The destination location

        Returns:
        - The total cost of traversing from the current location to the destination
        """
        distance, penalty = self.check_penalty(location, destination)
        return cost_so_far + (distance * penalty or self.infinity)

    def reconstruct_path(self, came_from, start, goal) -> list[str]:
        """
        Reconstruct the path from start to goal using the came_from dictionary.

        Args:
        - came_from: A dictionary storing the previous node for each node in the path
        - start: The starting location
        - goal: The desired destination

        Returns:
        - The reconstructed path from start to goal
        """
        current = goal
        full_path = []
        while current != start:
            full_path.append(current)
            current = came_from[current]
        full_path.append(start)
        full_path.reverse()
        return full_path
    
    def a_star_search(self) -> list[str]:
        """
        Perform A* search to find the shortest path from startLocation to desiredDestination.

        Returns:
        - The shortest path from startLocation to desiredDestination
        """
        min_priority_queue = queue.PriorityQueue()
        min_priority_queue.put((0, self.startLocation))
        came_from = {}
        cost_so_far = {}
        came_from[self.startLocation] = None
        cost_so_far[self.startLocation] = 0

        while not min_priority_queue.empty():
            current = min_priority_queue.get()[1]

            if current == self.desiredDestination:
                break
            
                
            for next_location in self.get_neighbours(current):
                new_cost = self.path_cost(cost_so_far[current], current, next_location)
                if next_location not in cost_so_far or new_cost < cost_so_far[next_location]:
                    cost_so_far[next_location] = new_cost
                    priority = new_cost + self.haversine_distance(self.graph.nodes[next_location].location, self.graph.nodes[self.desiredDestination].location)
                    min_priority_queue.put((priority, next_location))
                    came_from[next_location] = current

        path = self.reconstruct_path(came_from, self.startLocation, self.desiredDestination)
        return path
    
    def dfs_search(self) -> list[str]:
        """
        Perform Depth-First Search (DFS) to find a path from startLocation to desiredDestination.

        Returns:
        - The path found by DFS from startLocation to desiredDestination
        """
        stack = [(self.startLocation, [self.startLocation])]
        visited = set()

        while stack:
            (current, path) = stack.pop()
            visited.add(current)

            if current == self.desiredDestination:
                break

            for next_location in self.get_neighbours(current):
                if next_location not in visited:
                    stack.append((next_location, path + [next_location]))

        dfs_path = path

        return dfs_path
    


    # This function was used to generate the chart data for every possible route.
    
    # def comparison_data(self):
    #     min_priority_queue = queue.PriorityQueue()
    #     short_min_priority_queue = queue.PriorityQueue()

    #     min_priority_queue.put((0, self.startLocation))
    #     short_min_priority_queue.put((0, self.startLocation))

    #     came_from = {}
    #     short_came_from = {}

    #     cost_so_far = {}
    #     short_cost_so_far = {}

    #     came_from[self.startLocation] = None
    #     short_came_from[self.startLocation] = None
    #     cost_so_far[self.startLocation] = 0
    #     short_cost_so_far[self.startLocation] = 0

    #     visited_count = 0
    #     short_visited_count = 0

    #     distance_traveled = {}
    #     short_distance_traveled = {}
    #     distance_traveled[self.startLocation] = 0
    #     short_distance_traveled[self.startLocation] = 0

    #     dfs_stack = [(self.startLocation, [self.startLocation])]
    #     dfs_visited = set()
    #     dfs_distance_traveled = 0

    #     while not min_priority_queue.empty():
    #         current = min_priority_queue.get()[1]
    #         visited_count += 1
    #         if current == self.desiredDestination:
    #             break
    #         for next_location in self.get_neighbours(current):
    #             new_cost = self.path_cost(cost_so_far[current], current, next_location)
    #             if next_location not in cost_so_far or new_cost < cost_so_far[next_location]:
    #                 cost_so_far[next_location] = new_cost
    #                 distance_traveled[next_location] = distance_traveled[current] + self.graph.get_path(current, next_location).distance or self.infinity
    #                 priority = new_cost + self.haversine_distance(self.graph.nodes[next_location].location, self.graph.nodes[self.desiredDestination].location)
    #                 min_priority_queue.put((priority, next_location))
    #                 came_from[next_location] = current
                    
    #     while not short_min_priority_queue.empty():
    #         short_current = short_min_priority_queue.get()[1]
    #         short_visited_count  += 1
    #         if short_current == self.desiredDestination:
    #             break
    #         for next_location in self.get_neighbours(short_current):
    #             new_cost = self.graph.get_path(short_current, next_location).distance + short_cost_so_far[short_current] or self.infinity
    #             if next_location not in short_cost_so_far or new_cost < short_cost_so_far[next_location]:
    #                 short_cost_so_far[next_location] = new_cost
    #                 short_distance_traveled[next_location] = short_distance_traveled[short_current] + self.graph.get_path(short_current, next_location).distance or self.infinity
    #                 priority = new_cost + self.haversine_distance(self.graph.nodes[next_location].location, self.graph.nodes[self.desiredDestination].location)
    #                 short_min_priority_queue.put((priority, next_location))
    #                 short_came_from[next_location] = short_current

    #     while dfs_stack:
    #         (current, path) = dfs_stack.pop()
    #         dfs_visited.add(current)

    #         if current == self.desiredDestination:
    #             break

    #         for next_location in self.get_neighbours(current):
    #             if next_location not in dfs_visited:
    #                 dfs_stack.append((next_location, path + [next_location]))
    #                 dfs_distance_traveled += self.graph.get_path(current, next_location).distance

    #     dfs_visited_count = len(dfs_visited)

    #     path_a_star = self.reconstruct_path(came_from, self.startLocation, self.desiredDestination)
    #     path_shortest = self.reconstruct_path(short_came_from, self.startLocation, self.desiredDestination)
    #     dfs_path = path

    #     # Save data to file
    #     self.save_paths_to_json_comparison(path_a_star, cost_so_far[self.desiredDestination], visited_count, distance_traveled[self.desiredDestination],
    #                                         path_shortest, short_cost_so_far[self.desiredDestination], short_visited_count, short_distance_traveled[self.desiredDestination],
    #                                         dfs_path, None, dfs_visited_count, dfs_distance_traveled)


    # def save_paths_to_json_comparison(self, path_a_star, cost_a_star, visited_count_a_star, distance_traveled_a_star,
    #                                     path_shortest, cost_shortest, visited_count_shortest, distance_traveled_shortest,
    #                                     dfs_path, dfs_cost, dfs_visited_count, dfs_distance_traveled):
    #     path_data = {
    #         "start_location": self.startLocation,
    #         "desired_destination": self.desiredDestination,
    #         "a_star_path": {
    #             "path": path_a_star,
    #             "cost": cost_a_star,
    #             "visited_count": visited_count_a_star,
    #             "distance_traveled": distance_traveled_a_star
    #         },
    #         "shortest_path": {
    #             "path": path_shortest,
    #             "cost": cost_shortest,
    #             "visited_count": visited_count_shortest,
    #             "distance_traveled": distance_traveled_shortest
    #         },
    #         "dfs_path": {
    #             "path": dfs_path,
    #             "cost": dfs_cost,
    #             "visited_count": dfs_visited_count,
    #             "distance_traveled": dfs_distance_traveled
    #         }
    #     }
    #     with open("path_data.json", "a") as file:
    #         if file.tell() != 0:  
    #             file.write(",\n")  
    #         json.dump(path_data, file, indent=4)
