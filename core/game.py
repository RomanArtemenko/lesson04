import random

class Game:
    EMPTY_CELL = 0   
    NUBERS = [2, 4]

    def __init__(self, size):
        self.width = size
        self.score = 0
        self.field = [[self.EMPTY_CELL for col in range(size)] for row in range(size)]

        self.add_number(2, self.NUBERS[:1])

    def add_number(self, count, list_value):
        i = 0 

        while i < count:
            row = random.randint(0, self.width - 1)
            col = random.randint(0, self.width - 1)

            if self.field[row][col] == self.EMPTY_CELL:
                self.field[row][col] = random.choice(list_value)
                i += 1

            if not self._has_empty_cell():
                break

    def move_left(self):
        self._shift_left() 
        self._merge_left()
        self._shift_left()
        self.add_number(1, self.NUBERS)

    def move_right(self):
        self._shift_right()
        self._merge_right()
        self._shift_right()        
        self.add_number(1, self.NUBERS)

    def move_up(self):
        self._shift_up()
        self._merge_up()
        self._shift_up() 
        self.add_number(1, self.NUBERS)

    def move_down(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        self._shift_down()
        self._merge_down()
        self._shift_down()
        self.add_number(1, self.NUBERS)

    def has_moves(self):
        return self._has_empty_cell() or self._has_merge_available()

    def _has_empty_cell(self):
        for row in self.field:
            if self.EMPTY_CELL in row:
                return True
        return False 

    def _has_merge_available(self):
        for row in range(self.width):
            for col in range(self.width - 1):
                if self.field[row][col] == self.field[row][col + 1]:
                    return True
                if (row + 1) <= (self.width - 1):
                    if self.field[row][col] == self.field[row + 1][col]:
                        return True
        
        return False

    def get_score(self):
        return self.score
 
    def get_field(self):
        return self.field

    def _get_cell(self, row, col):
        return self.field[row][col]

    def _shift_left(self):
        for row in range(self.width):
            for col in range(self.width - 1):
                for pos in range(self.width - 1 - col):
                    if self.field[row][pos] == self.EMPTY_CELL and self.field[row][pos + 1] != self.EMPTY_CELL:
                        self.field[row][pos], self.field[row][pos + 1] = self.field[row][pos + 1], self.field[row][pos]

    def _shift_right(self):
        for row in range(self.width):            
            for col in range(self.width - 1):
                for pos in range(self.width - 1, col, -1):
                    if self.field[row][pos] == self.EMPTY_CELL and self.field[row][pos - 1] != self.EMPTY_CELL:
                        self.field[row][pos], self.field[row][pos - 1] = self.field[row][pos - 1], self.field[row][pos] 

    def _shift_up(self):
        for col in range(self.width):
            for row in range(self.width - 1):
                for pos in range(self.width - 1 - row):
                    if self.field[pos][col] == self.EMPTY_CELL and self.field[pos + 1][col] != self.EMPTY_CELL:
                        self.field[pos][col], self.field[pos + 1][col] = self.field[pos + 1][col], self.field[pos][col]

    def _shift_down(self):
        for col in range(self.width):
            for row in range(self.width - 1):
                for pos in range(self.width - 1, row, -1):
                    if self.field[pos][col] == self.EMPTY_CELL and self.field[pos - 1][col] != self.EMPTY_CELL:
                        self.field[pos][col], self.field[pos - 1][col] = self.field[pos - 1][col], self.field[pos][col] 

    def _merge_left(self):
        for row in range(self.width):
            for col in range(self.width - 1):
                if self.field[row][col] != self.EMPTY_CELL and self.field[row][col] == self.field[row][col + 1]:
                    self.field[row][col], self.field[row][col + 1] = self.field[row][col] * 2, self.EMPTY_CELL
                    self.score += self.field[row][col]  

    def _merge_right(self):
        for row in range(self.width):            
            for col in range(self.width - 1, 0, -1):
                if self.field[row][col] != self.EMPTY_CELL and self.field[row][col] == self.field[row][col - 1]:
                    self.field[row][col], self.field[row][col - 1] = self.field[row][col] * 2, self.EMPTY_CELL
                    self.score += self.field[row][col] 

    def _merge_up(self):
        for col in range(self.width):
            for row in range(self.width - 1):
                if self.field[row][col] != self.EMPTY_CELL and self.field[row][col] == self.field[row + 1][col]:
                    self.field[row][col], self.field[row + 1][col] = self.field[row][col] * 2, self.EMPTY_CELL        

    def _merge_down(self):
        for col in range(self.width):
            for row in range(self.width - 1, 0, -1):
                if self.field[row][col] != self.EMPTY_CELL and self.field[row][col] == self.field[row - 1][col]:
                    self.field[row][col], self.field[row - 1][col] = self.field[row][col] * 2, self.EMPTY_CELL
                    self.score += self.field[row][col]
