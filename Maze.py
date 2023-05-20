def dfs(maze, start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
            return path + [current]

        visited.add(current)
        row, col = current

        # Explore the neighbors in four directions: up, right, down, left
        neighbors = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor

            # Check if the neighbor is within the maze boundaries
            if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]):

                # Check if the neighbor is not a wall and has not been visited before
                if maze[n_row][n_col] != '#' and (n_row, n_col) not in visited:
                    stack.append((neighbor, path + [current]))

    return None  # No path found


maze = [
    # 0    1    2    3    4    5   6   7   8
    ['S', '.', '#', '#', '.', 'G' '.' '.' 'G'],
    ['#', '.', '.', '#', '.', '#' '#' '.' '.'],
    ['#', '#', '.', '#', '.', '#' '.' '.' '#'],
    ['#', '.', '.', '.', '.', '#' '.' '#' '.'],
    ['#', '#', '#', '#', '.', '#' '.' '#' '.'],
    ['#', '#', '#', '#', '.', '.' '.' '#' '.'],
    ['#', '#', '#', '#', '.', '.' '#' '#' '.'],
]

start = (0, 0)
goal = (0, 5)

path = dfs(maze, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path exists.")
