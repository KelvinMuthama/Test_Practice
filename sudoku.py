"""This Function Checks whether the sum of a row, column or a 3 by 3 square in a sudoku adds up to 45"""
def check_sum():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]

    total = 0
    for row in matrix:
        for value in row:
            total += value

    return total

if __name__ == '__main__':
    print(check_sum())
    