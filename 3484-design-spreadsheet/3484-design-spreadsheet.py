import string
import re

class Spreadsheet:
    def __init__(self, rows: int):
        self.idx_chr_mapping = {letter: index for index, letter in enumerate(string.ascii_uppercase)}
        self.spreadsheet = [[0 for _ in range(26)] for _ in range(rows + 1)]
        for i in range(26):
            self.spreadsheet[0][i] = chr(ord('A') + i)

    def setCell(self, cell: str, value: int) -> None:
        col_name, row_val_str = re.findall(r'([A-Z]+)(\d+)', cell)[0]
        row_val = int(row_val_str)
        col_idx = self.idx_chr_mapping[col_name]
        self.spreadsheet[row_val][col_idx] = value

    def resetCell(self, cell: str) -> None:
        col_name, row_val_str = re.findall(r'([A-Z]+)(\d+)', cell)[0]
        row_val = int(row_val_str)
        col_idx = self.idx_chr_mapping[col_name]
        self.spreadsheet[row_val][col_idx] = 0

    def getValue(self, formula: str) -> int:
        if formula.startswith("="):
            expression = formula[1:]
            
            parts = re.findall(r'[A-Z]+\d+|\d+', expression)
            
            total = 0
            for part in parts:
                if part.isdigit():
                    total += int(part)
                else:  
                    col_name, row_val_str = re.findall(r'([A-Z]+)(\d+)', part)[0]
                    row_val = int(row_val_str)
                    col_idx = self.idx_chr_mapping[col_name]
                    total += self.spreadsheet[row_val][col_idx]
            return total
        else: 
            col_name, row_val_str = re.findall(r'([A-Z]+)(\d+)', formula)[0]
            row_val = int(row_val_str)
            col_idx = self.idx_chr_mapping[col_name]
            return self.spreadsheet[row_val][col_idx]
        
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)