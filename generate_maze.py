import maze
import random

# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    backtrack_stack = []
    rand_cell_index = random.randint(0, len(m.maze_array) - 1)
    visited_cells = 1
    while visited_cells < len(m.maze_array):
        unvisited_neighbors = m.cell_neighbors(rand_cell_index)
        if len(unvisited_neighbors) >= 1:
            rand_neighbor = unvisited_neighbors[random.randint(0, len(unvisited_neighbors) - 1)]
            m.connect_cells(rand_cell_index, rand_neighbor[0], rand_neighbor[1])
            backtrack_stack.append(rand_cell_index)
            rand_cell_index = rand_neighbor[0]
            visited_cells += 1
        else:
            rand_cell_index = backtrack_stack.pop()
        m.refresh_maze_view()
    m.state = "solve"

def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
