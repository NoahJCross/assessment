from Path import *
class Graph:
  
  def __init__(self, nodes=None, directed=True) -> None:
    """
    Initialize a Graph object.

    Args:
    - nodes: A dictionary representing nodes and their connections (default is None)
    - directed: A boolean indicating whether the graph is directed (default is True)
    """
    self.nodes = nodes or {}
    self.directed = directed
    if not directed:
      self.MakeUndirected()

  def MakeUndirected(self) -> None:
    """Converts the graph to an undirected graph."""
    for node, node_data in self.nodes.items():
      for destination, path in node_data.paths.items():
        self.AddConnection(destination, node, path.distance, path.is_slope, path.is_paved)

  def AddConnection(self, location, destination, distance, is_slope, is_paved) -> None:
    """
    Add a connection between two locations.
    Args:
    - location: The starting location
    - destination: The destination location
    - distance: The distance between the two locations
    - is_slope: A boolean indicating if there's a slope in the path
    - is_paved: A boolean indicating if the path is paved
    """
    self.nodes[location].paths[destination] = Path(distance, is_slope, is_paved)

  def get_path(self, location, destination) -> Path:
    """
    Get the path between two locations.

    Args:
    - location: The starting location
    - destination: The destination location

    Returns:
    - The path object representing the connection between the locations
    """
    return self.nodes[location].paths[destination]

def UndirectedGraph(nodes) -> Graph:
  """
  Create an undirected graph.

  Args:
  - nodes: A dictionary representing nodes and their connections

  Returns:
  - An instance of the Graph class representing an undirected graph
  """
  return Graph(nodes, directed=False)