from csv_helper import write_to_csv


class PricingManger:

    def __init__(self):
        self.row = []

    def append_row(self, entity):
        self.row.append(entity)

    def write_to_csv(self):
        write_to_csv(self.row, 'pricing.csv', './out')
