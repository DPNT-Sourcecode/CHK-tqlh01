
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        # offers = {"A": [(5, 200), (3, 130)], "B": [(2, 45)], "C": [None], "D": [None], "E": [None]}

        count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

        for sku in skus:
            if sku in count:
                count[sku] += 1
            else:
                return -1
        
        free_b_count = count["E"] // 2
        remaining_b = count["B"] - free_b_count
 
        total_price = 0

        a_count = count["A"]
        five_a_offers = a_count // 5
        total_price += five_a_offers * 200
        a_count -= five_a_offers

        three_a_offers = a_count // 3
        total_price += three_a_offers * 130
        a_count -= three_a_offers

        total_price += a_count * prices["A"]

        return total_price
