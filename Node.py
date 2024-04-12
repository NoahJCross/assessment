
class Node():
  
  def __init__(self, location, paths) -> None:  
    """
    Initialize a Node object.

    Args:
    - location: Tuple representing the geographical coordinates of the node
    - paths: A dictionary representing paths from this node to other nodes (default is an empty dictionary)
    
    Returns:
    - None
    """   
    self.location = location  
    self.paths = paths or {}

