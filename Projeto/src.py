class City:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_connection(self, city, distance):
        self.connections[city] = distance

class Graph:
    def __init__(self):
        self.cities = {}

    def add_city(self, city):
        if city not in self.cities:
            self.cities[city] = City(city)

    def connect_cities(self, city1, city2, distance):
        self.add_city(city1)
        self.add_city(city2)
        self.cities[city1].add_connection(self.cities[city2], distance)
        self.cities[city2].add_connection(self.cities[city1], distance)

    def uniform_cost_search(self, start, goal):
        from queue import PriorityQueue
        visited = set()
        pq = PriorityQueue()
        pq.put((0, [start]))

        while not pq.empty():
            (cost, path) = pq.get()
            node = path[-1]
            if node.name == goal:
                return (path, cost)
            if node.name not in visited:
                visited.add(node.name)
                for adjacent in node.connections:
                    if adjacent.name not in visited:
                        pq.put((cost + node.connections[adjacent], path + [adjacent]))

    # Implementação das outras buscas seguindo a lógica específica de cada uma

# Exemplo de uso
graph = Graph()
graph.connect_cities('Porto', 'Aveiro', 68)
graph.connect_cities('Porto', 'Vila Real', 116)
graph.connect_cities("Porto", "Viseu", 100)
graph.connect_cities("Viseu", "Lisboa", 50)
graph.connect_cities("Lisboa", "Faro", 50)
graph.connect_cities("Viseu", "Faro", 100)
# Adicione todas as outras conexões conforme as tabelas fornecidas

# Busca de caminho
start_city = graph.cities['Porto']
goal_city = 'Faro'
path, cost = graph.uniform_cost_search(start_city, goal_city)
print("Caminho encontrado:", [city.name for city in path])
print("Custo total:", cost)
