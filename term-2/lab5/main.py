import openpyxl as xl

class LineCalc:
    def __init__(self, n: list[int]) -> None:
        self.unique = []
        self.ununique = []
        for i in n:
            if n.count(i) == 1:
                self.unique += [i]
            else:
                self.ununique += [i]

    def get_unique(self) -> list[int]:
        return self.unique
    
    def unique_count(self) -> int:
        return len(self.unique)

    def get_ununique(self) -> list[int]:
        return self.ununique

    def ununique_count(self) -> int:
        return len(self.ununique)
    
def tst_LineCalc():
    tmp = [62, 62, 62, 36, 251]
    ln = LineCalc(tmp)
    print(ln.get_unique())
    print(ln.unique_count())
    print(ln.get_ununique())
    print(ln.ununique_count())


if __name__ == "__main__":
    
    wb = xl.load_workbook('./06.xlsx')

    sheet = wb.active

    count = 0
    for line in sheet.iter_rows(values_only=True):
        lc = LineCalc(line)
        if lc.unique_count() == 3:
            if lc.unique_count() != 0 and lc.ununique_count() != 0:
                if (sum(lc.unique) / lc.unique_count()) < (sum(lc.ununique) / lc.ununique_count()):
                    count += 1

    print(count)