import random
from collections import deque

class Hanoi:
    def __init__(self, n_disks, arrangement):
        self.n_disks = n_disks
        self.arrangement = arrangement.lower()
        self.towers = {"A": [], "B": [], "C": []}
        self._setup_towers()

    def _setup_towers(self):
        if self.arrangement == "randomized":
            disks = list(range(1, self.n_disks + 1))
            random.shuffle(disks)
            self.towers["A"] = list(reversed(disks))
        else:
            # Standard arrangement
            self.towers["A"] = list(range(self.n_disks, 0, -1))
        self.towers["B"] = []
        self.towers["C"] = []

    def solve_standard(self):
        moves = []
        def move(n, source, dest, aux):
            if n == 1:
                moves.append((source, dest))
                return
            move(n-1, source, aux, dest)
            moves.append((source, dest))
            move(n-1, aux, dest, source)
        move(self.n_disks, "A", "C", "B")
        return moves

    def solve_randomized(self):
        start = tuple(tuple(self.towers[p]) for p in ("A", "B", "C"))
        goal = (tuple(), tuple(), tuple(range(self.n_disks, 0, -1)))
        if start == goal:
            return []

        queue = deque([start])
        parents = {start: None}
        moves_dict = {start: None}
        pegs = ("A", "B", "C")

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for i, stack in enumerate(current):
                if not stack:
                    continue
                disk = stack[-1]
                for j, dst in enumerate(current):
                    if i == j:
                        continue
                    if dst and dst[-1] < disk:
                        continue
                    temp = [list(s) for s in current]
                    temp[i].pop()
                    temp[j].append(disk)
                    next_state = tuple(tuple(s) for s in temp)
                    if next_state not in parents:
                        parents[next_state] = current
                        moves_dict[next_state] = (pegs[i], pegs[j])
                        queue.append(next_state)

        path = []
        state = goal
        if goal not in parents:
            return []
        while state != start:
            move_ = moves_dict[state]
            path.append(move_)
            state = parents[state]
        path.reverse()
        return path


# --- Terminal interface ---
while True:
    try:
        n = int(input("Enter number of disks (3-8): "))
        if 3 <= n <= 8:
            break
        print("Please enter a number between 3 and 8.")
    except ValueError:
        print("Enter a valid integer.")

while True:
    arrangement = input("Choose arrangement (Standard/Randomized): ").strip().lower()
    if arrangement in ("standard", "randomized"):
        break
    print("Enter 'Standard' or 'Randomized'.")

game = Hanoi(n, arrangement)
print("\nInitial Towers:", game.towers)

if arrangement == "standard":
    moves = game.solve_standard()
    print("\nMoves to solve standard arrangement:")
else:
    moves = game.solve_randomized()
    if not moves:
        print("\nNo legal solution found for randomized arrangement!")
        exit()
    print("\nMoves to solve randomized arrangement:")

for i, move in enumerate(moves, 1):
    print(f"{i}: {move}")