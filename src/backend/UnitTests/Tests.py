import os
import unittest
from FilterTheList import Filter
import FilterTheList as ftl
import Operations_and_Invariants.Invariant_bool as i_bool
from Operations_and_Invariants.Invariant_bool import Utils
from Operations_and_Invariants import Invariant_num as i_num
import networkx as nx
import abc


class Helper:

    @staticmethod
    def choice_bool_inv(choices):
        ibool = i_bool.Invariant_bool()
        inv_choices = []
        for x in choices:
            inv_choices.append(ibool.all[x])
        return inv_choices
        '''
        0: 'planar', 1: 'connected', 2: 'biconnected', 3: 'bipartite', 4: 'Eulerian', 5: 'Chordal', 6: 'Triangle-free',
        7: 'Regular', 8: 'Claw-free', 9: 'Tree', 10: 'k-regular', 11: 'Some A-eigenvalue integer', 
        12: 'Some L-eigenvalue integer', 13: 'Some Q-eigenvalue integer', 14: 'Some D-eigenvalue integer', 
        15: 'A-integral', 16: 'L-integral', 17: 'Q-integral', 18: 'D-integral', 19: 'Largest A-eigenvalue is integer',
        20: 'Largest L-eigenvalue is integer', 21: 'Largest Q-eigenvalue is integer',
        22: 'Largest D-eigenvalue is integer'}
        '''

    @staticmethod
    def list_graphs_from(name_file):
        file = open(os.path.abspath(name_file), 'r')
        list = file.read().splitlines()
        file.close()
        return list

    @staticmethod
    def Run(file, expression, choices):
        return Filter.Run(Helper.list_graphs_from(file), expression, Helper.choice_bool_inv(choices))[1]


class Backend_tests(unittest.TestCase):


    def test_split_expression(self):
        expression1 = 'chi(G)==5 AND omega(l(G))>=1 AND n(G)<=lambda1(G)'
        expression_split = ['chi(G)==5', 'omega(l(G))>=1', 'n(G)<=lambda1(G)']
        expression2 = 'chi(G)==5 OR omega(l(G))>=1 OR n(G)<=lambda1(G)'
        expression3 = 'chi(G)==5 AND omega(l(G))>=1 OR n(G)<=lambda1(G)'
        self.assertEqual(expression_split, ftl.Split_The_Expression(expression1)[0])
        self.assertEqual(expression_split, ftl.Split_The_Expression(expression2)[0])
        self.assertEqual('error', ftl.Split_The_Expression(expression3))

    def test_integral(self):
        self.assertTrue(Utils.Is_a_integer(1))
        self.assertTrue(Utils.Is_a_integer(1.000001))
        self.assertTrue(Utils.Is_a_integer(0.999998))

    def test_name_of_all_num_invariant(self):
        for inv in i_num.Invariant_num().all:
            for j in range(0, len(inv.code)):
                self.assertTrue(Helper.Run('single_graph.g6', inv.code[j]+'(G)==1', []) >= 0)

    def test_name_of_all_bool_invariant(self):
        j= 0
        isBool=True
        for inv in i_bool.Invariant_bool().all:
            self.assertTrue(Helper.Run('single_graph.g6', '', [j]) >= 0)
            isBool = isBool and inv.calculate(nx.from_graph6_bytes('I???h?HpG'.encode('utf-8')))
            j=j+1
        self.assertTrue(isinstance(isBool, bool))

    def test1_filter(self):
        self.assertEqual(1,Helper.Run('file1.g6', '', [1, 16, 20]))

    def test2_filter(self):
        self.assertEqual(0.5, Helper.Run('file2.g6', '', [1, 16, 20]))

    def test3_filter(self):
        self.assertEqual(1,Helper.Run('file3.g6', 'a(G)<=5 AND a(G)>=2 AND diam(G)==2', [7, 8]))
        #self.assertEqual(Helper.Run('file3_single.g6', 'a(G)<=5 AND a(G)>=2 AND diam(G)==2', [7, 8]), 1)
        #problema com K~z\c\qRXVa~

    def test4_filter(self):
        self.assertEqual(1,Helper.Run('file4.g6', 'econ(G)==3', [0, 7]))

    def test5_filter(self):
        self.assertEqual(1,Helper.Run('file5.g6', 'eigen1L(G)>5', [9]))

    def test6_filter(self):
        self.assertEqual(1,Helper.Run('file6.g6', '(alpha(G)/gamma(G))-3 >= (7/8)-eigen1A(G)', [0]))

    def test7_filter(self):
        self.assertEqual(1,Helper.Run('file7.g6', 'chi(G)<=eigen1A(G)+1', []))

    def test8_filter(self):
        self.assertEqual(1,Helper.Run('file8.g6', 'chi(G)==omega(G)', []))

    def test9_filter(self):
        self.assertTrue(Helper.Run('file9.g6', 'match(G)**4+diam(G)>=81.3', []) > (10/137)-1)

    def test10_filter(self):
        self.assertEqual(1, Helper.Run('file10.g6', 'eigen1Q(G)>2 OR eigen1Q(G)<=2', [5]))


if __name__ == '__main__':
    unittest.main()
