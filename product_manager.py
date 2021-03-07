from csv_helper import write_to_csv


class ProductManager:

    def __init__(self):
        self.row = []

    def append_row(self, entity):
        self.row.append(entity)

    def extend_row(self, items):
        self.row.extend(items)

    def write_to_csv(self):
        write_to_csv(self.row, 'non-duplicated product.csv', './out')
