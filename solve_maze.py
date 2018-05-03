import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    stack = []
    cur_Cell = 0
    visited_cells = 0
    while not cur_Cell == len(m.maze_array) - 1:
        neighbors = m.cell_neighbors(cur_Cell)
        if len(neighbors) >= 1:
            new_cell = neighbors[random.randint(0, len(neighbors) - 1)]
            m.visit_cell(cur_Cell, new_cell[0], new_cell[1])
            stack.append(cur_Cell)
            cur_Cell = new_cell[0]
            visited_cells += 1
        else:
            m.backtrack(cur_Cell)
            cur_Cell = stack.pop()
        m.refresh_maze_view()
    m.state = "idle"

# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    queue = []
    cur_cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.insert(0, (cur_cell, in_direction))
    while not cur_cell == len(m.maze_array) - 1 and len(queue) > 0:
        cur_cell, in_direction = queue.pop()
        m.bfs_visit_cell(cur_cell, in_direction)
        visited_cells += 1
        m.refresh_maze_view()
        neighbors = m.cell_neighbors(cur_cell)
        for neighbor in neighbors:
            queue.insert(0, neighbor)
    m.reconstruct_solution(cur_cell)
    m.state = "idle"

def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
