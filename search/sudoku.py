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

     # 最初に実行する関数
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
        # answer_countが1のときのみ数独が完成(答えが存在し、答えがひとつ)しているため、画面に表示する。
        if self.answer_count == 1:
            self.print_sudoku()
        else:
            self.print_error()

    #　数独が完成した時に呼ばれ、数独の答えが表示される。
    def print_sudoku(self):
        for row in range(9):
            for col in range(9):
                print(self.result[row][col], end="")
            print()
            
# sudokuの答えを作っていく関数
    def make_sudoku(self, row, col, number):
        #行row,列colを0の場所(初期状態で'.'であり値を新たに入れる必要がある箇所)まで移動させる
        while self.int_sudoku[row][col] != 0:
            row += 1
            if row > 8:
                row = 0
                col += 1
                # 行も列も8を超えたとき、数独は完成したことになるため、checkを行う。
                if col > 8:
                    self.check_sudoku()
                    return
        # 行row,列colに値numberを代入できるかチェック
        if not self.can_putnumber(row, col, number):
            return
        self.int_sudoku[row][col] = number
        #値を代入したら、次の'.'に値を入れるため、同じ関数を再帰する
        for number in range(1, 10):
            self.make_sudoku(row, col, number)
        #値を元に戻す
        self.int_sudoku[row][col] = 0

        # int_sudokuの行row,列colに値numberを配置できるか(同一行、列に同じ値がないか、左端から9マスずつに分けた場合に同じ値を含むマスがないか)チェック
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

    # 数独(int_sudoku)に最後の値まで入れれたときに、それが唯一の解かチェックする。
    def check_sudoku(self):
        for row in range(9):
            for col in range(9):
                # resultははじて全て0で初期化しているため、resultの値が0でなく、かつint_sudokuの値と異なる場合、この数独の解は複数あること(answer_countに+1を加える)になる。
                if self.result[row][col] == 0 or self.result[row][col] == self.int_sudoku[row][col]:
                    self.result[row][col] = self.int_sudoku[row][col]
                else:
                    self.answer_count += 1
                    return
        self.answer_count = 1
        return

    # 数独ははじめ文字のリストで与えられたが、値を変更しづらいため、数値の2重配列(int_sudoku)に変換する。このとき'.'は0とする。
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

    #まず、はじめに最初に与えられた数独が条件を満たしているか(行、列で数字が被っていないか、端から9マスずつ分けた場合に数字が被っていないか)チェックする。
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
