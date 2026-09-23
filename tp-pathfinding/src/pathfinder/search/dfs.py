from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()
        expanded[root.state]= True

        frontier = StackFrontier()
        frontier.add(root)

        if grid.objective_test(root.state):
            return Solution(root.state,reached=expanded)
        
        while True:
            if frontier.is_empty():
                return NoSolution(expanded)
            
            n = frontier.remove()

            for movimiento in grid.actions(n.state):
                s = grid.result(n.state,movimiento)

                if s not in expanded.keys():

                    son = Node("",s,
                    cost=n.cost + grid.individual_cost(n.state, movimiento),
                    parent=n,
                    action=movimiento
                    )

                    if grid.objective_test(s):
                        return Solution(son,reached=expanded)
                    frontier.add(son)
                    expanded[s] = True

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...

        return NoSolution(expanded)
