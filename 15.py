from typing import DefaultDict

class Graph:
  def __init__(self) -> None:
    self.vertices = set()
    self.edges = DefaultDict(list)
    self.distances = {}
  
  def addVertex(self, vertex) -> None:
    self.vertices.add(vertex)

  def addEdge(self, src, dst, weight) -> None:
    self.edges[src].append(dst)
    self.distances[(src,dst)] = weight

def dijkstra(src, graph):
  visited = {src : 0}
  vertices = set(graph.vertices)

  while vertices:

    minVertex = None
    for vertex in vertices:
      if vertex in visited:
        if minVertex is None:
          minVertex = vertex
        elif visited[vertex] < visited [minVertex]:
          minVertex = vertex
    
    if minVertex is None:
      break

    vertices.remove(minVertex)
    currentWeight = visited[minVertex]

    for edge in graph.edges[minVertex]:
      weight = currentWeight + graph.distances[(minVertex,edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
  
  return visited

customGraph = Graph()
input = open("15-input.txt").read().split()

for x in range(len(input)):
  for y in range(len(input[x])):
    customGraph.addVertex(str(x)+str(y))

    nx=x+1
    if nx < len(input):
      customGraph.addEdge(str(x)+str(y), str(nx)+str(y), int(input[nx][y]))

    nx=x-1
    if nx >= 0:
      customGraph.addEdge(str(x)+str(y), str(nx)+str(y), int(input[nx][y]))

    ny=y+1
    if ny < len(input[0]):
      customGraph.addEdge(str(x)+str(y), str(x)+str(ny), int(input[x][ny]))
    
    ny=y-1
    if ny >= 0:
      customGraph.addEdge(str(x)+str(y), str(x)+str(ny), int(input[x][ny]))

print(dijkstra('00',customGraph)['9999'])
