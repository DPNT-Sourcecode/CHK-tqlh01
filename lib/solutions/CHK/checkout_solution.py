
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        offers = {"A": [(5, 200), (3, 130)], "B": [(2, 45)], "C": [None], "D": [None], "E": [(2, 0, "B")]}

        count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

        free_b_count = 0
        count_e = 0

        for sku in skus:
            if sku in count:
                count[sku] += 1
                if sku == "E":
                    count_e += 1
                    if count_e == 2:
                        free_b_count += 1
                        count_e = 0
            else:
                return -1
            
        total_price = 0

        for item, item_count in count.items():
            if offers[item] is None:
                total_price += item_count * prices[item]
            else:
                for offer in offers:
                    offer_count, offer_price
                # offer_count, offer_price = offers[k]
                # num_offers = v // offer_count
                # remaining = v % offer_count

                # total_price += offer_price * num_offers + remaining * prices[k]

        return total_price
