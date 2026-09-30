from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost + grid.h(root))
        
        reached = {}
        reached[root.state] = root.cost
        
        
        while True:
            if frontier.is_empty():
                return NoSolution
            n = frontier.pop()
        
            if grid.objective_test(n.state):
                return Solution(n,reached)
        
            for movimiento in grid.actions(n.state):
                s = grid.result(n.state,movimiento)
                c = n.cost + grid.individual_cost(n.state, movimiento)
                if s not in reached or c < reached[s]: 
                    n_ = Node("", s, c, n, movimiento)
                    reached[s] = c
                    frontier.add(n_, n_.cost + grid.h(n_))

        
        return NoSolution(reached)
