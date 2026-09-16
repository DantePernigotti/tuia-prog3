from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True


        frontier = QueueFrontier()
        frontier.add(root)


        while True:
            if frontier.is_empty():
                return NoSolution(reached)

            n = frontier.remove()

            for movimiento in grid.actions(n.state):

                s = grid.result(n.state,movimiento)
                if s not in reached.keys():

                    son = Node("",s,
                    cost=n.cost + grid.individual_cost(n.state, movimiento),
                    parent=n,
                    action=movimiento)

                    if grid.objective_test(s):
                        return Solution(son,reached=reached)
                    frontier.add(son)
                    reached[s] = True

           # Initialize frontier with the root node
                # TODO Complete the rest!!
                # ...
    
        
