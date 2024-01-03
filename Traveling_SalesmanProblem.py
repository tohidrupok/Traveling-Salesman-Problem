#pip install geopy

from geopy.distance import great_circle
Data_of_Bank_locations = [
    {"id": 1, "lati": 23.8728568, "long": 90.3984184, "address": "Uttara Branch"},
    {"id": 2, "lati": 23.8513998, "long": 90.3944536, "address": "City Bank Airport"},
    {"id": 3, "lati": 23.8330429, "long": 90.4092871, "address": "City Bank Nikunja"},
    {"id": 4, "lati": 23.8679743, "long": 90.3840879, "address": "City Bank Beside Uttara Diagnostic"},
    {"id": 5, "lati": 23.8248293, "long": 90.3551134, "address": "City Bank Mirpur 12"},
    {"id": 6, "lati": 23.827149, "long": 90.4106238, "address": "City Bank Le Meridien"},
    {"id": 7, "lati": 23.8629078, "long": 90.3816318, "address": "City Bank Shaheed Sarani"},
    {"id": 8, "lati": 23.8673789, "long": 90.429412, "address": "City Bank Narayanganj"},
    {"id": 9, "lati": 23.8248938, "long": 90.3549467, "address": "City Bank Pallabi"},
    {"id": 10, "lati": 23.813316, "long": 90.4147498, "address": "City Bank JFP"}
]

#get distance two bank
def distance_of_this_two_bank(loc1, loc2):

    return great_circle((loc1["lati"], loc1["long"]), (loc2["lati"], loc2["long"])).km

# get total distance for a singel road.
def distance_of_this_road(This_road, Data_of_Bank_locations):
    total_distance = 0
    for i in range(len(This_road) - 1):
        total_distance += distance_of_this_two_bank(Data_of_Bank_locations[This_road[i] - 1], Data_of_Bank_locations[This_road[i + 1] - 1])
    total_distance += distance_of_this_two_bank(Data_of_Bank_locations[This_road[-1] - 1], Data_of_Bank_locations[This_road[0] - 1])  # Return to the starting bank(ID:1)
    return total_distance

# Solve Using Depth-first search (DFS) 
class TSPDFS:
    def __init__(self, Data_of_Bank_locations):
        self.Data_of_Bank_locations = Data_of_Bank_locations
        self.best_route = None
        self.min_distance = float('inf')
        self.visited = set()

    def solve(self):
        n = len(self.Data_of_Bank_locations)
        initial_node = 1  # Start bank id == 1
        self.visited.add(initial_node)
        self.dfs(initial_node, [initial_node])

    def dfs(self, current_node, current_road):
        #base_Case
        if len(current_road) == len(self.Data_of_Bank_locations):
            # Update best road which is min cost.
            current_distance = distance_of_this_road(current_road, self.Data_of_Bank_locations)
            if current_distance < self.min_distance:
                self.min_distance = current_distance
                self.best_route = current_road.copy()
            return
        #recursion
        for next_bank in range(1, len(self.Data_of_Bank_locations) + 1):
            if next_bank not in self.visited:
                self.visited.add(next_bank)
                self.dfs(next_bank, current_road + [next_bank])
                self.visited.remove(next_bank)

# Create TSP solver and solve the problem
tsp_solver = TSPDFS(Data_of_Bank_locations)
tsp_solver.solve()

#output in a vscode
print("Optimal Route:", tsp_solver.best_route)
print("Total Distance, k.m = ", tsp_solver.min_distance) 

#write a new file
with open("Min_Cost_road.txt", "w") as file:
    for bank_id in tsp_solver.best_route:
        branch = next(loc for loc in Data_of_Bank_locations if loc["id"] == bank_id)
        file.write(f"-----TO-----\n{branch['address']} (ID: {bank_id})\n")



#This code run within 30 seconds.
#Solve this problem by the core concept of DFS. I have aslo option {{Branch and Bound },{Dynamic Problem}}
#Please Install the Python library.
#Tohidul Islam Rupok
#BSc In CSE, DIU.
        