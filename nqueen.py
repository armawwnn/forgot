import random
import matplotlib.pyplot as plt
import ipywidgets as widgets

plt.rcParams['figure.figsize'] = (6, 6)

class NQueensState:
    
    def __init__(self, queens=None, N=8):

        if queens:
            self.N = len(queens)
            self.queens = queens.copy()
        else:
            self.N = N
            self.queens = list(range(1, N + 1))

        self.num_conflicts = None    
        
    def __eq__(self, other):
        if self is other: return True
        if other is None: return False
        if not isinstance(other, NQueensState): return False
    
        return self.conflicts() == other.conflicts()
    
    def __ge__(self, other):
        if self is other: return True
        if other is None: return False
        if not isinstance(other, NQueensState): return False
    
        return self.conflicts() >= other.conflicts()        






    def conflicts(self):
        if self.num_conflicts is None:
            self.num_conflicts = 0
            for i in range(self.N - 1):
                for j in range(i + 1, self.N):
                    # Check if queens are on the same diagonal
                    if abs(self.queens[j] - self.queens[i]) == j - i:
                        self.num_conflicts += 1
            # Subtract the number of duplicate queens
            self.num_conflicts -= (self.N - len(set(self.queens)))
        return abs(self.num_conflicts)  # Take the absolute value





    def conflicts_old(self):

        if self.num_conflicts is None:
            self.num_conflicts = sum([abs(self.queens[j] - self.queens[i]) == j - i
                                      for i in range(self.N - 1)
                                      for j in range(i + 1, self.N)])

        return self.num_conflicts
                            
    def neighbors(self):

        N = self.N
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                neighbor = NQueensState(queens=self.queens)
                neighbor.queens[i], neighbor.queens[j] = neighbor.queens[j], neighbor.queens[i]
                yield neighbor
    
    def best_neighbor(self):

        min_conflicts = self.N * (self.N - 1) // 2
        best = None
        for neighbor in self.neighbors():
            if neighbor.conflicts() < min_conflicts:
                min_conflicts, best = neighbor.conflicts(), neighbor
        return best

        #         return min(self.neighbors(), key=lambda x: x.conflicts())
    
    def random_neighbor(self):

        i = random.randint(0, self.N - 2)
        j = random.randint(i + 1, self.N - 1)
        neighbor = NQueensState(queens=self.queens)
        neighbor.queens[i], neighbor.queens[j] = neighbor.queens[j], neighbor.queens[i]
        return neighbor
    
    @staticmethod
    def random_state(N=8):
        queens = list(range(1, N + 1))
        random.shuffle(queens)
        return NQueensState(queens=queens)

    def plot(self, ax=None, figsize=(6, 6), show_conflicts=False, fc='darkslateblue'):
        
        if ax is None:
            fig = plt.figure(figsize=figsize)
            ax = fig.add_subplot(1,1,1)
        
        N = self.N

        border = plt.Rectangle((0, 0), N, N, ec=fc, fc='w', alpha=0.35)
        ax.add_patch(border)

        for i in range(N):
            for j in range(N):
                alpha = 0.35 if (i + j) % 2 == 0 else 0.1
                cell = plt.Rectangle((i, j), 1, 1, fc=fc, alpha=alpha)
                ax.add_patch(cell)

        if show_conflicts:
            for i in range(N - 1):
                row_i = self.queens[i]
                for j in range(i + 1, N):
                    row_j = self.queens[j]
                    if row_i == row_j or abs(row_i - row_j) == j - i:
                        x1, x2 = i + 0.5, j + 0.5
                        y1, y2 = (row_i - 1) + 0.5, (row_j - 1) + 0.5
                        line = plt.Line2D((x1, x2), (y1, y2), lw=3, ls='-', color='orchid', alpha=0.6)
                        ax.add_line(line)

        for col, row in enumerate(self.queens):
            # c = 'k' if (col + row) % 2 == 0 else 'w'
            x = col + 0.5
            y = (row - 1) + 0.5
            fs = max(1, figsize[0] * 50 // N)
            ax.text(x, y, '♛', color='k', fontsize=fs, ha='center', va='center')

        ax.axis('square')
        ax.axis('off')
        ax.set_title("Conflicts = {}".format(self.conflicts()), fontsize=18)
        plt.show()    

    def get_queens(self):

        return self.queens
        
    def __str__(self):
        return f'{self.queens} <{self.conflicts()}>'
    
    def __repr__(self):
        return f'NQueensState(queens={self.queens})'
