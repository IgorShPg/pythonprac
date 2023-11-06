import sys


class Maze:

    def __init__(self, size):
        self.maze = self.make_maze(size)


    def make_maze(self, n):
        m = [['\u2588' for i in range(2*n+1)] for j in range(2*n+1)]
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i !=0 and i!=len(m)-1:
                    if j%2 != 0 and i%2!=0:
                        m[i][j] = u"\u00B7"
        return m

    def __setitem__(self, key, value):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        if value == u'\u2588':
            if x0 == x1 or y0 == y1:
                if x0 == x1:
                    for i in range(2*y0 + 1, 2*y1 + 1) if y1>y0 else range(2*y0 + 1, 2*y1 + 1, -1):
                        if i % 2 == 0:
                            self.maze[i][2*x0+1] = value
                else:
                    for i in range(2*x0 + 1, 2*x1 + 1) if x1>x0 else range(2*x0 + 1, 2*x1 + 1, -1):
                        if i % 2 == 0:
                            self.maze[2*y0+1][i] = value

        else:
            if x0 == x1 or y0 == y1:
                if x0 == x1:
                    for i in range(2*y0 + 1, 2*y1 + 1) if y1>y0 else range(2*y0 + 1, 2*y1 + 1, -1):
                        self.maze[i][2*x0+1] = value
                else:
                    for i in range(2*x0 + 1, 2*x1 + 1) if x1>x0 else range(2*x0 + 1, 2*x1 + 1, -1):
                        self.maze[2*y0+1][i] = value
            else:
                return


    def __getitem__(self, key):
        x0, y0, x1, y1 = 2*key[0] + 1, 2*key[1].start + 1, 2*key[1].stop + 1, 2*key[2] + 1
        return self.solve_maze(self.maze, (y0, x0), (y1, x1))

    def __str__(self):
        str = ""
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                str+=self.maze[i][j]
            if i!=len(self.maze)-1:
                str+="\n"
        return str

    def explore_maze(self, maze, start, visited, stop):
        x, y = start
        x1, y1 = stop
        rows, cols = len(maze), len(maze[0])

        if x < 0 or x >= rows or y < 0 or y >= cols: 
            return False

        if x == x1 and y == y1:  
            return True

        if maze[x][y] == u'\u2588' or visited[x][y]:  
            return False

        visited[x][y] = True  


        if self.explore_maze(maze, (x + 1, y), visited, stop):
            return True
        if self.explore_maze(maze, (x - 1, y), visited, stop):
            return True
        if self.explore_maze(maze, (x, y + 1), visited, stop):
            return True
        if self.explore_maze(maze, (x, y - 1), visited, stop):
            return True

        return False

    def solve_maze(self, maze, start, stop):
        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]
        if start:
            return self.explore_maze(maze, start, visited, stop)
        else:
            return False

exec(sys.stdin.read())
