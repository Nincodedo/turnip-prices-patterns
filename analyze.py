import csv


class AnalyzeTurnips:
    allowed_blank_days = 0

    def is_valid_row(self, row):
        valid_row = True
        count = 1
        while count < len(row):
            if row[count - 1] != '' and row[count] == '':
                valid_row = False
            count = count + 1
        return valid_row

    def get_algorithm_for_week(self, week):
        if self.is_decreasing_pattern(week):
            return "decreasing"
        else:
            return "unknown"

    def is_decreasing_pattern(self, week):
        count = 0
        diff = self.generate_percentage_diff(week)
        while count < len(diff) - 1:
            if diff[count] != 0.9:
                return False
            count = count + 1
        return True

    def generate_percentage_diff(self, week):
        count = 0
        price_list = []
        while count < len(week) - 1:
            price = round(int(week[count + 1]) / int(week[count]), 2)
            if price > 1.5:
                price_list.append(1.5)
            elif price > 1:
                price_list.append(1.1)
            elif 0.98 < price < 1.02:
                price_list.append(1)
            elif price < 0.6:
                price_list.append(0.5)
            elif price < 1:
                price_list.append(0.9)
            count = count + 1
        return price_list

    def main_function(self):
        print("Starting")
        valid_turnip_prices = []
        with open("turnips.csv", "r", newline='') as csv_file:
            turnip_reader = csv.reader(csv_file, delimiter=',')
            for row in turnip_reader:
                if self.is_valid_row(row):
                    price_row = []
                    for price in row:
                        price_row.append(int(price))
                    valid_turnip_prices.append(price_row)
        print(valid_turnip_prices)
        for week in valid_turnip_prices:
            algorithm = self.get_algorithm_for_week(week)
            if algorithm == 'unknown':
                print('\nUnknown algorithm, generating percentage differences')
                print(week)
                print(self.generate_percentage_diff(week))
            else:
                print("\n")
                print(algorithm)
                print(week)
