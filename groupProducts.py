__author__ = 'jerry'

from operator import itemgetter
import unittest

#
# original version
#
def groupProducts(products):
    brandType = {}
    for p in products:
        if p['brand'] not in brandType.keys():
            brandType[p['brand']] = {}
        brandType[p['brand']][p['type']] = 1
    groupedProducts = []
    for b in sorted(brandType.keys()):
        for t in sorted(brandType[b].keys()):
           groupedProducts.append({
               'brand': b,
               'type': t
           })
    return groupedProducts

#
# faster version, use sorted function
#
def fastGroupProducts(products):
    groupedProducts = []
    for p in sorted(products, key=itemgetter('brand', 'type')):
        if p not in groupedProducts:
            groupedProducts.append(p);
    return groupedProducts


# Test
class Tes(unittest.TestCase):
    def test(self):
        # generate products in random order
        test_products = [
            {'brand': 'B_A', 'type': 'T_A'},
            {'brand': 'B_B', 'type': 'T_A'},
            {'brand': 'B_C', 'type': 'T_A'},
            {'brand': 'B_A', 'type': 'T_B'},
            {'brand': 'B_B', 'type': 'T_B'},
            {'brand': 'B_A', 'type': 'T_C'},
            # duplicate one
            {'brand': 'B_A', 'type': 'T_C'},
        ]

        correct_products = [
            {'brand': 'B_A', 'type': 'T_A'},
            {'brand': 'B_A', 'type': 'T_B'},
            {'brand': 'B_A', 'type': 'T_C'},
            {'brand': 'B_B', 'type': 'T_A'},
            {'brand': 'B_B', 'type': 'T_B'},
            {'brand': 'B_C', 'type': 'T_A'},
        ]

        print("test data: " + str(test_products))
        print("correct result: " + str(correct_products))
        groupedProducts1 = groupProducts(test_products)
        print("original version result: " + str(groupedProducts1))
        groupedProducts2 = fastGroupProducts(test_products)
        print("faster version result: " + str(groupedProducts2))
        self.assertEqual(correct_products, groupedProducts1)
        self.assertEqual(correct_products, groupedProducts2)

if __name__ == '__main__':
    unittest.main()