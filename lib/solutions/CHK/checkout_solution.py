
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        offers = {"A": (3, 130), "B": (2, 45), "C": None, "D": None}

        count = {"A": 0, "B": 0, "C": 0, "D": 0}

        for sku in skus:
            if sku in count:
                count[sku] += 1
            else:
                return -1
            
        total_price = 0

        for k, v in count.items():
            if offers[k] is None:
                total_price += v * prices[k]
            else:
                offer_count, offer_price = offers[k]
                num_offers = v // offer_count
                remaining = v % offer_count

                total_price += offer_price * num_offers + remaining * prices[k]

        return total_price
