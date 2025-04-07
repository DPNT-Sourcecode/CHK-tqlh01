
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20,
                  "H": 10, "I": 35, "J": 60, "K": 80, "L": 90, "M": 15, "N": 40,
                  "O": 10, "P": 50, "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40,
                "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}
        

        count = {item : 0 for item in prices.keys()}

        for sku in skus:
            if sku in count:
                count[sku] += 1
            else:
                return -1
        
        total_price = 0

        grouped_items = ["S","T","X","Y","Z"]
        group_counts = {item: count[item] for item in grouped_items}

        sorted_group_counts = sorted(grouped_items, key=lambda item: prices[item], reverse=True)

        total_group_count = sum(group_counts.values())
        group_offers =  total_group_count // 3

        if group_offers > 0:
            total_price += group_offers * 45

            items_to_reduce = group_offers * 3
            for item in sorted_group_counts:
                reduce_by = min(group_counts[item], items_to_reduce)
                group_counts[item] -= reduce_by
                items_to_reduce -= reduce_by
                if items_to_reduce == 0:
                    break
            
        for item in grouped_items:
            count[item] = group_counts[item]

        free_b_count = count["E"] // 2
        remaining_b = max(0, count["B"] - free_b_count)

        free_m_count = count["N"] // 3
        remaining_m = max(0, count["M"] - free_m_count)

        free_q_count = count["R"] // 3
        remaining_q = max(0, count["Q"] - free_q_count)
 

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
            elif sku == "H":
                ten_h_offers = value // 10
                total_price += ten_h_offers * 80
                value -= ten_h_offers * 10

                five_h_offers = value // 5
                total_price += five_h_offers * 45
                value -= five_h_offers * 5

                total_price += value * prices["H"]
            elif sku == "K":
                k_offers = value // 2
                total_price += k_offers * 150
                value -= k_offers * 2

                total_price += value * prices["K"]
            elif sku == "U":
                u_free = value // 4
                value -= u_free
                total_price += value * prices["U"]
            elif sku == "M":
                total_price += remaining_m * prices["M"]
            elif sku == "P":
                p_offers = value // 5
                total_price += p_offers * 200
                value -= p_offers * 5

                total_price += value * prices["P"]
            elif sku == "Q":
                q_offers = remaining_q // 3
                total_price += q_offers * 80
                remaining_q -= q_offers * 3

                total_price += remaining_q * prices["Q"]
            elif sku == "V":
                three_q_offers = value // 3
                total_price += three_q_offers * 130
                value -= three_q_offers * 3

                two_h_offers = value // 2
                total_price += two_h_offers * 90
                value -= two_h_offers * 2

                total_price += value * prices["V"]
            else:
                total_price += value * prices[sku]

        return total_price




