
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
        # offers = {"A": [(5, 200), (3, 130)], "B": [(2, 45)], "C": [None], "D": [None], "E": [None]}

        count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

        for sku in skus:
            if sku in count:
                count[sku] += 1
            else:
                return -1
        
        free_b_count = count["E"] // 2
        remaining_b = max(0, count["B"] - free_b_count)
 
        total_price = 0

        for sku, value in count.items():
            if sku == "A":
                five_a_offers = value // 5
                total_price += five_a_offers * 200
                value -= five_a_offers * 5

                three_a_offers = value // 3
                total_price += three_a_offers * 130
                value -= three_a_offers * 3

                total_price += value * prices["A"]
            elif sku == "B":
                b_offers = remaining_b // 2
                total_price += b_offers * 45
                remaining_b -= b_offers * 2

                total_price += remaining_b * prices["B"]
            elif sku == "F":
                f_free = value // 3
                value -= f_free
                total_price += value * prices["F"]
            else:
                total_price += value * prices[sku]

        return total_price