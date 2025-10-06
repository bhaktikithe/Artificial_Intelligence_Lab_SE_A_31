def dfs(maze, start, end):
    stack = [start]           # Initialize stack with start position
    visited = set()           # Track visited positions
    parent = {start: None}    # Keep track of how we reached each cell

    while stack:
        position = stack.pop()
        x, y = position

        # Check if we've reached the end
        if position == end:
            # Reconstruct path from end → start
            path = []
            while position is not None:
                path.append(position)
                position = parent[position]
            return path[::-1]  # Reverse for start → end

        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)

            if (0 <= new_x < len(maze) and 
                0 <= new_y < len(maze[0]) and
                maze[new_x][new_y] == 0 and
                new_pos not in visited and
                new_pos not in stack):  # Avoid duplicates
                stack.append(new_pos)
                parent[new_pos] = position  # Record the parent

    return None  # No path found


# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and end positions
start = (0, 0)
end = (4, 4)

# Solve the maze
path = dfs(maze, start, end)

if path:
    print("Path found!")
    print("Path:", path)
else:
    print("No path exists.")

