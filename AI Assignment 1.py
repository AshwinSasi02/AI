vertices = set()
neigh=list()
graph = dict()

def take_input():
    n = int(input("Enter number of vertices : "))

    for v in range(n):
        v = input("Enter Vertex : ")
        vertices.add(v)
        nb= int(input("Enter number of neighbours of vertex "+ v ))
        for a in range(nb):
            a =input("Enter neighbour: ")
            neigh.append(a)
        graph[v] = []
        graph[v].extend(neigh)
        print(graph)
        neigh.clear()
        print("Vertex", v, "added.")



visited_dfs = set()
def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)


visited_bfs = []
queue = []
def BFS(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


take_input()

start_dfs = input("Enter starting vertex for DFS : ")
print("Result of Depth First Search")
DFS(visited_dfs, graph, start_dfs)

start_bfs = input("Enter starting vertex for BFS : ")
print("Result of Breadth First Search")
BFS(visited_bfs, graph, start_bfs)