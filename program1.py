class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # If the grid is empty, return 0 islands
        if not grid:
            return 0
        
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Function to perform DFS and mark the island as visited
        def dfs(r, c):
            # Boundary check and if the current cell is water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            
            # Mark the current cell as visited by setting it to 'W'
            grid[r][c] = 'W'
            
            # Explore neighboring cells (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        # Initialize the island count to 0
        island_count = 0
        
        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find a land cell ('L'), start a DFS
                if grid[r][c] == 'L':
                    island_count += 1  # Increment island count
                    dfs(r, c)  # Perform DFS to mark all parts of this island as visited
        
        # Return the total number of islands
        return island_count

# Example usage
solution = Solution()

# Test case 1
grid1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]
print(solution.getTotalIsles(grid1))  # Output: 1

# Test case 2
grid2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"]
]
print(solution.getTotalIsles(grid2))  # Output: 3
