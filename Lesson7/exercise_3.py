# 3. Реализовать программу работы с органическими клетками.
class Cellular:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cellular(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells <= other.cells:
            print("Количество ячеек должно быть больше, чем в другой клетке!")
            return
        return Cellular(self.cells - other.cells)

    def __mul__(self, other):
        return Cellular(self.cells * other.cells)

    def __truediv__(self, other):
        div = round(self.cells / other.cells)
        if div < 1:
            print("Слишком мало ячеек по сравнению с другой клеткой")
            return
        return Cellular(div)

    def make_order(self, n_cells):
        return "".join([n_cells * '*' + '\n' for raw in range(self.cells // n_cells)] + [(self.cells % n_cells) * '*'])


cell_1 = Cellular(5)
cell_2 = Cellular(12)
cell_sum = cell_1 + cell_2
print(f"Кол-во ячеек в cell_sum: {cell_sum.cells}")
cell_sub_1 = cell_1 - cell_2
cell_sub_2 = cell_2 - cell_1
print(f"Кол-во ячеек в cell_sub_2: {cell_sub_2.cells}")
cell_mult = cell_1 * cell_2
print(f"Кол-во ячеек в cell_mult: {cell_mult.cells}")
cell_div_1 = cell_1 / cell_mult
cell_div_2 = cell_2 / cell_1
print(f"Кол-во ячеек в cell_div_2: {cell_div_2.cells}")
print(cell_mult.make_order(13))
