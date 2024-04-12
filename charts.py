import json
import matplotlib.pyplot as plt

data_file = "path_data.json"

with open(data_file) as f:
    data = json.load(f)

# path_lengths_a_star = []
# path_lengths_shortest = []

# for route_data in data:
#     a_star_path_length = len(route_data["a_star_path"]["path"])
#     shortest_path_length = len(route_data["shortest_path"]["path"])
#     path_lengths_a_star.append(a_star_path_length)
#     path_lengths_shortest.append(shortest_path_length)

# max_path_length = max(max(path_lengths_a_star), max(path_lengths_shortest))
# min_path_length = min(min(path_lengths_a_star), min(path_lengths_shortest))

# plt.hist(path_lengths_a_star, label='A Star Path', bins=range(min_path_length, max_path_length+2), alpha=0.5)
# plt.hist(path_lengths_shortest, label='Shortest Path', bins=range(min_path_length, max_path_length+2), alpha=0.5)
# plt.xlabel('Path Length')
# plt.ylabel('Frequency')
# plt.title('Distribution of Path Length')
# plt.legend()
# plt.grid(True)
# plt.savefig('path_length_a_star.png')
# plt.show()



# percentage_increase = []
# for route_data in data:
#     a_star_cost = route_data["a_star_path"]["cost"]
#     shortest_cost = route_data["shortest_path"]["cost"]
#     increase = (a_star_cost - shortest_cost) / shortest_cost * 100
#     percentage_increase.append(increase)

# plt.hist(percentage_increase, bins=20)
# plt.xlabel('Percentage Increase in Cost (%)')
# plt.ylabel('Frequency')
# plt.title('Distribution of Percentage Increase in Cost')
# plt.grid(True)
# plt.savefig('percentage_increase_cost.png')
# plt.show()



# percentage_increase_distances = []

# for route_data in data:
#     a_star_distance = route_data["a_star_path"]["distance_traveled"]
#     shortest_distance = route_data["shortest_path"]["distance_traveled"]
#     percentage_increase = ((a_star_distance - shortest_distance) / shortest_distance) * 100
#     percentage_increase_distances.append(percentage_increase)

# non_zero_percentage_increase_distances = [x for x in percentage_increase_distances if x != 0]

# plt.hist(non_zero_percentage_increase_distances, bins=20, color='green', alpha=0.7)
# plt.xlabel('Percentage Increase in Distance Traveled')
# plt.ylabel('Frequency')
# plt.title('Distribution of Percentage Increase in Distance Traveled (Excluding 0%)')
# plt.grid(True)
# plt.savefig('percentage_increase_distance_a_star.png')
# plt.show()



# percentage_increase_distances = []

# for route_data in data:
#     dfs_distance = route_data["dfs_path"]["distance_traveled"]
#     shortest_distance = route_data["a_star_path"]["distance_traveled"]
#     percentage_increase = ((dfs_distance - shortest_distance) / shortest_distance) * 100
#     percentage_increase_distances.append(percentage_increase)

# percentage_increase_distances = [x for x in percentage_increase_distances if x < 10000]
# plt.hist(percentage_increase_distances, bins=100, color='green', alpha=0.7)
# plt.xlabel('Percentage Increase in Distance Traveled DFS')
# plt.ylabel('Frequency')
# plt.title('Distribution of Percentage Increase in Distance Traveled DFS')
# plt.grid(True)
# plt.savefig('percentage_increase_distance.png')
# plt.show()



# path_lengths_dfs = []
# path_lengths_shortest = []

# for route_data in data:
#     dfs_path_length = len(route_data["dfs_path"]["path"])
#     shortest_path_length = len(route_data["a_star_path"]["path"])
#     path_lengths_dfs.append(dfs_path_length)
#     path_lengths_shortest.append(shortest_path_length)

# max_path_length = max(max(path_lengths_dfs), max(path_lengths_shortest))
# min_path_length = min(min(path_lengths_dfs), min(path_lengths_shortest))

# plt.hist(path_lengths_dfs, label='DFS Path', bins=range(min_path_length, max_path_length+2), alpha=0.5)
# plt.hist(path_lengths_shortest, label='A Star Path', bins=range(min_path_length, max_path_length+2), alpha=0.5)
# plt.xlabel('Path Length DFS')
# plt.ylabel('Frequency')
# plt.title('Distribution of Path Length DFS')
# plt.legend()
# plt.grid(True)
# plt.savefig('path_length.png')
# plt.show()