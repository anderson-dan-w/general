#!/usr/bin/python3
from time import time
from math import sqrt
import sys

class Cell:
    def __init__(self, position, span, value=0, preset=False):
        self.position = position
        self.value = value
        self.preset = preset
        self.row = int(position / span)
        self.column = position % span
        self.div = int(sqrt(span))
        self.possibles = list(range(1, span+1))
        self.block = int(int(self.column / self.div) + self.div * int(self.row / self.div))
        self.rcb = (self.row, self.column, self.block)
        self.relatedRows = []
        self.relatedCols = []
        for num in range(1, self.div):
            self.relatedRows.append(((self.row+num) % self.div) +
                                    self.div * int(self.row/self.div)) 
            self.relatedCols.append(((self.column+num) % self.div) +
                                    self.div * int(self.column/self.div))
            
    
    def presetValue(self, value):
        self.value = value
        self.preset = True

    def unsetValue(self):
        self.value = 0
        self.preset = False


class Strip:
    def __init__(self, span):
        self.span = span
        self.cells = []
        self.cellPositions = []

    def addCell(self, cell):
        if not isinstance(cell, Cell):
            print("Pass in Cell object")
            return False
        self.cells.append(cell)
        self.cellPositions.append(cell.position)

    def getValues(self):
        ls = []
        for cell in self.cells:
            if cell.value:
                ls.append(cell.value)
        return ls

    def getOpenCells(self): 
        ls = []
        for num in range(len(self.cells)):
            cell = self.cells[num]
            if not cell.value:
                ls.append(self.cellPositions[num])
        return ls


class Grid:
    def __init__(self, span):
        self.span = span
        self.div = int(sqrt(span))
        self.cells = [None]*(span*span)
        self.rows = [None]*span
        self.cols = [None]*span
        self.blks = [None]*span
        for sp in range(span):
            self.rows[sp] = Strip(span)
            self.cols[sp] = Strip(span)
            self.blks[sp] = Strip(span)
        for cell in range(len(self.cells)):
            self.cells[cell] = Cell(cell, span)
        for cell in self.cells:
            (r, c, b) = cell.rcb
            self.rows[r].addCell(cell)
            self.cols[c].addCell(cell)
            self.blks[b].addCell(cell)
        self.values = ["-"] + list(range(1, self.span+1))
        
    def __repr__(self):
        totalans = ""
        x = self.span
        z = self.div
        for g in range(z):
            divrows = ""
            for h in range(z):
                onerow = ""
                for i in range(z):
                    divvals = ""
                    for j in range(z):
                        val = ""
                        val += str(self.values[
                            self.cells[g*z*x + h*x + i*z + j].value])+" "
                        divvals += val
                    onerow += divvals + "  "
                divrows += onerow + "\n"
            totalans += divrows + "\n"
        return totalans

###################
## Set up stuff  ##
###################
    def setValueList(self, ls):
        if not isinstance(ls, list):
            print("Needs to be a list...")
            return False
        ls = list(set(ls))
        ls.sort()
        if len(ls) != self.span :
            print("Thats not the right length list...")
            return False
        for num in range(len(ls)):
            self.values[num+1] = ls[num]
        return True

    def presetValues(self, d, val=0):
        if isinstance(d, dict):
            for key, value in d.items():
                for cell in value:
                    self.cells[cell].presetValue(key)
            return True
        if isinstance(d, list):
            for cell in d:
                self.cells[cell].presetValue(val)
            return True
        if isinstance(d, int):
            self.cells[d].presetValue(val)
            return True
        print("Whatd you enter? Dict, list, int?")
        return False

    def isDone(self):
        for cell in self.cells:
            if not cell.value:
                return False
        return True
####################
## Logic solve    ##
####################
    def overlapStrips(self, strip1, strip2):
        return list(set(strip1.cellPositions).intersection(strip2.cellPositions))
    
    def onlyValuesHere(self, cell):
        if not isinstance(cell, Cell):
            cell = self.cells[cell]
        if cell.value:
            return 0
        temp = set(range(1, self.span+1))
        (r, c, b) = cell.rcb
        used = set(self.rows[r].getValues() + self.cols[c].getValues()
                   +self.blks[b].getValues())
        ls = list(temp.difference(used))
        if len(ls) == 1:
            cell.presetValue(ls[0])
            return ls[0]
        cell.possibles = ls
        return 0

    def valOnlyHere(self, cell, value):
        if not isinstance(cell, Cell):
            cell = self.cells[cell]
        if cell.value:
            return False
        (r, c, b) = cell.rcb
        block = self.blks[b]
        openCells = self.blks[b].getOpenCells()
        if cell.position in openCells:
            openCells.remove(cell.position)
        for r in cell.relatedRows:
            row = self.rows[r]
            if value in row.getValues():
                overlap = self.overlapStrips(block, row)
                for c in overlap:
                    if c in openCells:
                        openCells.remove(c)
        for c in cell.relatedCols:
            col = self.cols[c]
            if value in col.getValues():
                overlap = self.overlapStrips(block, col)
                for c in overlap:
                    if c in openCells:
                        openCells.remove(c)
        if openCells:
            return False
        cell.presetValue(value)
        return True
        
    def fillInObvis(self, once=False, verb=False):
        st = time()
        changes = 1
        while changes:
            changes = 0
            for num in range(len(self.cells)):
                cell = self.cells[num]
                if cell.value:
                    next
                if self.onlyValuesHere(num):
                    changes += 1
                    next
                for val in cell.possibles:
                    if self.valOnlyHere(cell, val):
                        changes += 100
                        next
            if verb:
                print("Changes: ", changes, "\n")
                print(self)
            if once:
                changes = 0
            if not changes and verb:
                print("Exiting, took: ", time()-st)
        return True

def main():
    st = time()
    filename = sys.argv[1]
    f = open(filename, mode='r')
    text = f.read()
    text = text.replace("\s","").replace("\n","")
    grids = text.split("Grid")
    for i in range(len(grids)):
        grid = grids[i]
        grid = grid[3:]
        if grid:
            newboard = Grid(9)
            for index in range(len(grid)):
                num = int(grid[index])
                if num:
                    newboard.presetValues([index], num)
                    newboard.fillInObvis()
                    newboard.setValueList(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if newboard.isDone():
                print("Board#: ", i+1)
                print(newboard)
    el = time()-st
    print("Took all of: ", el)
    return

if __name__ == '__main__':
    main()








            

