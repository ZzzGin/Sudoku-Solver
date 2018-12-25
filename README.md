# Sudoku-Solver
A Sudoku solver for Leetcode problem 0037

## For a sudoku problem:
![image](https://github.com/ZzzGin/Sudoku-Solver/raw/master/example.png)

You can import the module and do it in code:
```python
import SS
board = [
  ['.', '5', '.', '.', '.', '.', '.', '.', '8']
  ['.', '.', '.', '1', '.', '.', '.', '9', '2']
  ['.', '.', '.', '.', '4', '6', '3', '.', '.']
  ['.', '9', '3', '6', '1', '.', '.', '.', '.']
  ['4', '.', '.', '.', '.', '.', '.', '.', '1']
  ['.', '.', '.', '.', '5', '8', '7', '4', '.']
  ['.', '.', '9', '7', '6', '.', '.', '.', '.']
  ['3', '7', '.', '.', '.', '1', '.', '.', '.']
  ['8', '.', '.', '.', '.', '.', '.', '7', '.']
]
s = SS.Solution()
result = s.solveSudoku(board)
```

Or, you can just run the SSmain.py and input the sudoku as:
```
Input the board by rows, '.' as a blank.
row0: .5......8
row1: ...1...92
row2: ....463..
row3: .9361....
row4: 4.......1
row5: ....5874.
row6: ..976....
row7: 37...1...
row8: 8......7.
```

## Dependency
python3 and nothing.
