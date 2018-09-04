# * クラス名：Sudoku
# * 関数名 : solve
# * 内容　：数独の答えを返して表示するアルゴリズム。答えが複数ある場合、答えが存在しない場合はErrorと表示
# * 引数　：
#    sudoku  : リスト　数独の初期状態を表し'.' or 数字からなります。'.'は空白。
# * 返値　： 数独の答え
# 例)
"""
sudoku ={".8..1..2.","6..3.5..1","..7...4..",".2.1.9.5.","7.......6",".9.6.3.4.","..5...3..","9..2.1..8",".3..6..7."}
この場合↓のようになる
.8..1..2.
6..3.5..1
..7...4..
.2.1.9.5.
7.......6
.9.6.3.4.
..5...3..
9..2.1..8
.3..6..7.
実行すると以下のように表示される
389714625
642395781
517826439
426179853
753482196
198653247
865947312
974231568
231568974
"""


class Solve:

    result = 0
    answer_count = 0
    sudoku = []
    int_sudoku = [[0 for j in range(9)] for i in range(9)]
    result = [[0 for j in range(9)] for i in range(9)]

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solve(self):
        if len(self.sudoku) != 9:
            self.print_error()
            return
        has_answer = self.create_int_sudoku()
        if not has_answer:
            self.print_error()
            return
        if not self.first_check():
            self.print_error()
            return
        for number in range(1, 10):
            self.make_sudoku(0, 0, number)
        if self.answer_count == 1:
            self.print_sudoku()
        else:
            self.print_error()

    def print_sudoku(self):
        for row in range(9):
            for col in range(9):
                print(self.result[row][col], end="")
            print()

    def make_sudoku(self, row, col, number):

        while self.int_sudoku[row][col] != 0:
            row += 1
            if row > 8:
                row = 0
                col += 1
                if col > 8:
                    self.check_sudoku()
                    return
        if not self.can_putnumber(row, col, number):
            return
        self.int_sudoku[row][col] = number
        for number in range(1, 10):
            self.make_sudoku(row, col, number)

        self.int_sudoku[row][col] = 0

    def can_putnumber(self, row, col, number):
        for index in range(9):
            if index != row and self.int_sudoku[index][col] == number:
                return False
            if index != col and  self.int_sudoku[row][index] == number:
                return False
        row_2 = row // 3
        col_2 = col // 3
        for r_index in range(row_2 * 3, (row_2 + 1) * 3):
            for c_index in range(col_2 * 3, (col_2 + 1) * 3):
                if r_index != row and c_index != col and self.int_sudoku[r_index][c_index] == number:
                    return False
        return True

    def check_sudoku(self):
        for row in range(9):
            for col in range(9):
                if self.result[row][col] == 0 or self.result[row][col] == self.int_sudoku[row][col]:
                    self.result[row][col] = self.int_sudoku[row][col]
                else:
                    self.answer_count += 1
                    return
        self.answer_count = 1
        return

    def create_int_sudoku(self):
        for row in range(len(self.sudoku)):
            if len(self.sudoku[row]) != 9:
                self.print_error()
                return False
            for col in range(len(self.sudoku[row])):
                if self.sudoku[row][col] == '.':
                    self.int_sudoku[row][col] = 0
                else:
                    self.int_sudoku[row][col] = int(self.sudoku[row][col])
        return True

    def first_check(self):
        for row in range(9):
            for col in range(9):
               if self.int_sudoku[row][col] != 0 and not self.can_putnumber(row, col, self.int_sudoku[row][col]):
                   return False
        return True

    # エラーページの表示
    def print_error(self):
        print("ERROR")

#Exampleの実行
sudoku =[".8..1..2.","6..3.5..1","..7...4..",".2.1.9.5.","7.......6",".9.6.3.4.","..5...3..","9..2.1..8",".3..6..7."]
solve = Solve(sudoku)
solve.solve()