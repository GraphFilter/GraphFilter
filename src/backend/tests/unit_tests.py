import os
import unittest
from filter_list import FilterList
import numpy as np
import operations_and_invariants.bool_invariants as i_bool
from operations_and_invariants.bool_invariants import Utils
from operations_and_invariants import num_invariants as i_num
from operations_and_invariants import operations as oper
import networkx as nx


class Helper:

    @staticmethod
    def choice_bool_inv(choices):
        ibool = i_bool.InvariantBool()
        inv_choices = []
        for x in choices:
            inv_choices.append(ibool.all[x])
        return inv_choices

    # NOTE:
    #  0: 'planar', 1: 'connected', 2: 'biconnected', 3: 'bipartite', 4: 'Eulerian', 5: 'Chordal', 6: 'Triangle-free',
    #  7: 'Regular', 8: 'Claw-free', 9: 'Tree', 10: 'k-regular', 11: 'Some A-eigenvalue integer',
    #  12: 'Some L-eigenvalue integer', 13: 'Some Q-eigenvalue integer', 14: 'Some D-eigenvalue integer',
    #  15: 'A-integral', 16: 'L-integral', 17: 'Q-integral', 18: 'D-integral', 19: 'Largest A-eigenvalue is integer',
    #  20: 'Largest L-eigenvalue is integer', 21: 'Largest Q-eigenvalue is integer',
    #  22: 'Largest D-eigenvalue is integer'}

    @staticmethod
    def list_graphs_from(name_file):
        file = open(os.path.abspath(name_file), 'r')
        group = file.read().splitlines()
        file.close()
        return group

    @staticmethod
    def run(file, expression, choices):
        ftl = FilterList(Helper.list_graphs_from(file), expression, Helper.choice_bool_inv(choices))
        return ftl.run()

    @staticmethod
    def some_c_exem(file, expression, choices):
        ftl = FilterList(Helper.list_graphs_from(file), expression, Helper.choice_bool_inv(choices))
        boolean = ftl.find_counter_example()
        return boolean, ftl.out


class BackendUnitTests(unittest.TestCase):

    def test_split_and_translate_expression(self):
        i_num.InvariantNum()
        oper.GraphOperations()
        chi = str(i_num.ChromaticNumber.code)
        line = str(oper.Line.code)
        omega = str(i_num.CliqueNumber.code)
        lambda1 = str(i_num.Largest1EigenA.code)
        n = str(i_num.NumberVertices.code)
        chi_str = str(i_num.ChromaticNumber.code_literal)
        line_str = str(oper.Line.code_literal)
        omega_str = str(i_num.CliqueNumber.code_literal)
        lambda1_str = str(i_num.Largest1EigenA.code_literal)
        n_str = str(i_num.NumberVertices.code_literal)
        expression1 = f'{chi}(G)==5 AND {omega}({line}(G))>=1 AND {n}(G)<={lambda1}(G)'
        expression_translated = [f'{chi_str}(G)==5', f'{omega_str}({line_str}(G))>=1', f'{n_str}(G)<={lambda1_str}(G)']
        expression2 = f'{chi}(G)==5 OR {omega}({line}(G))>=1 OR {n}(G)<={lambda1}(G)'
        expression3 = f'{chi}(G)==5 AND {omega}({line}(G))>=1 OR {n}(G)<={lambda1}(G)'
        self.assertEqual(expression_translated, FilterList.split_translate_expression(expression1)[0])
        self.assertEqual(expression_translated, FilterList.split_translate_expression(expression2)[0])
        self.assertEqual('error', FilterList.split_translate_expression(expression3))

    def test_translate_code_to_code_literal(self):
        i_num.InvariantNum()
        oper.GraphOperations()
        for inv in i_num.InvariantNum().all:
            expression = f'{inv.code}(G)==1'
            expression_translated = f'{inv.code_literal}(G)==1'
            self.assertEqual(expression_translated, FilterList.split_translate_expression(expression)[0])

    def test_name_of_all_num_invariant(self):
        i_num.InvariantNum()
        oper.GraphOperations()
        for inv in i_num.InvariantNum().all:
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6', f'{inv.code}(G)==1', []) >= 0)

    def test_AND_logic(self):
        exp1 = str(i_num.EdgeConnectivity.code) + '(G) >=3'
        exp2 = str(i_num.VertexConnectivity.code) + '(G) >=5'
        exp3 = str(i_num.CliqueNumber.code) + '(G) ==4'
        exp4 = str(i_num.Largest1EigenL.code) + '(G) > 10'
        exp4_n = str(i_num.Largest1EigenL.code) + '(G) <= 10'
        self.assertEqual(1, Helper.run('resources/graphs/graphs11.g6',
                                       f'{exp1} AND {exp2} AND {exp3} AND {exp4}', []))
        self.assertEqual(0, Helper.run('resources/graphs/graphs11.g6',
                                       f'{exp1} AND {exp2} AND {exp3} AND {exp4_n}', []))

    def test_OR_logic(self):
        exp1 = str(i_num.EdgeConnectivity.code) + '(G) >=3'
        exp2 = str(i_num.IndependenceNumber.code) + '(G) >= 7'
        exp1_n = str(i_num.EdgeConnectivity.code) + '(G) <3'
        exp2_n = str(i_num.IndependenceNumber.code) + '(G) < 7'

        self.assertEqual(1, Helper.run('resources/graphs/graphs12.g6', f'{exp1} OR {exp2}', []))
        self.assertTrue(Helper.run('resources/graphs/graphs12.g6', f'{exp1_n} OR {exp2_n}', []) < 1)

    def test_integral(self):
        self.assertTrue(Utils.is_integer(1))
        self.assertTrue(Utils.is_integer(1.000001))
        self.assertTrue(Utils.is_integer(0.999998))
        self.assertEqual(1, Helper.run('resources/graphs/graphs2.g6', '', [16]))

    def test_name_of_all_bool_invariant(self):
        j = 0
        is_bool = True
        all_choices = np.arange(len(i_bool.InvariantBool().all))
        for inv in i_bool.InvariantBool().all:
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6', '', [j]) >= 0)
            is_bool = is_bool and inv.calculate(nx.from_graph6_bytes('I???h?HpG'.encode('utf-8')))
            j = j + 1
        self.assertTrue(isinstance(is_bool, bool))
        self.assertTrue(Helper.run('resources/graphs/single_graph.g6', '', all_choices) >= 0)

    def test_graph_operations(self):
        alpha = str(i_num.IndependenceNumber.code)
        for op in oper.GraphOperations.all:
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6',
                                       f'{alpha}{str(op.code)}(G)>0', []) >= 1)

    def test_math_operations(self):
        for op in oper.MathOperations.all:
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6',
                                       f'{str(op.code)}(2)>0', []) >= 0)

    def test_find_counterexample(self):
        # diam = str(i_num.Diameter.code)
        # self.assertFalse(Helper.some_c_exem('resources/graphs/graphs2.g6', '', [16])[0])
        # self.assertTrue(Helper.some_c_exem('resources/graphs/graphs9.g6', f'{diam}(G)<=4', [])[0])
        no_tree = 'ZGC?KA?_a?E??A?K?GWAQ?h?CA?GP?O@gH@CCg??WC?C?QOS?A@?@?]_A@r?'
        self.assertEqual(Helper.some_c_exem('resources/graphs/graphs1.g6', '', [9])[1][0]['g6code'], no_tree)

    def test_not_100percent_filter(self):
        diam = str(i_num.Diameter.code)
        self.assertEqual(1 / 3, Helper.run('resources/graphs/graphs9.g6', f'{diam}(G)==3', []))

    def test_interpret_composition_functions(self):
        diam = str(i_num.Diameter.code)
        sqrt = str(oper.Sqrt.code)
        c = str(oper.Complement.code)
        self.assertEqual(1, Helper.run('resources/graphs/single_graph.g6', f'{sqrt}({diam}({c}(G)))>0', []))

    def test_json_file_exported(self):
        a = str(i_num.AlgebraicConnectivity.code)
        diam = str(i_num.Diameter.code)
        ftl = FilterList(
            Helper.list_graphs_from('resources/graphs/graphs3.g6'),
            f'{a}(G)<=5 AND {a}(G)*{diam}(G)>=2 AND {diam}(G)==2',
            Helper.choice_bool_inv([7, 8]))
        ftl.run()
        file = ftl.load_json()
        self.assertTrue(file.name.endswith('.json'))


class MiscellaneousTests(unittest.TestCase):

    def test_expression_with_choices(self):
        a = str(i_num.AlgebraicConnectivity.code)
        diam = str(i_num.Diameter.code)
        alpha = str(i_num.IndependenceNumber.code)
        gamma = str(i_num.DominationNumber.code)
        eigen1_a = str(i_num.Largest1EigenA.code)
        eigen1_q = str(i_num.Largest1EigenQ.code)
        self.assertEqual(1,
                         Helper.run('resources/graphs/graphs3.g6', f'{a}(G)<=5 AND {a}(G)>=2 AND {diam}(G)==2', [7, 8]))

        self.assertEqual(1,
                         Helper.run('resources/graphs/graphs6.g6', f'({alpha}(G)/{gamma}(G))-3 >= (7/8)-{eigen1_a}(G)',
                                    [0]))
        self.assertEqual(1, Helper.run('resources/graphs/graphs10.g6', f'{eigen1_q}(G)>2 OR {eigen1_q}(G)<=2', [5]))

    def test_largest_eigen_L(self):
        eigen1_l = str(i_num.Largest1EigenL.code)
        self.assertEqual(1, Helper.run('resources/graphs/graphs5.g6', f'{eigen1_l}(G)>5', [9]))

    def test_wilf_result(self):
        chi = str(i_num.ChromaticNumber.code)
        eigen1 = str(i_num.Largest1EigenA.code)
        self.assertEqual(1, Helper.run('resources/graphs/graphs7.g6', f'{chi}(G)<={eigen1}(G)+1', []))

    def test_independence_and_matching(self):
        alpha = str(i_num.IndependenceNumber.code)
        match = str(i_num.MatchingNumber.code)
        line = str(oper.Line.code)
        self.assertEqual(1, Helper.run('resources/graphs/graphs7.g6', f'{match}(G)=={alpha}({line}(G))', []))

    def test_perfect_graphs(self):
        chi = str(i_num.ChromaticNumber.code)
        omega = str(i_num.CliqueNumber.code)
        self.assertEqual(1, Helper.run('resources/graphs/graphs8.g6', f'{chi}(G)=={omega}(G)', []))


if __name__ == '__main__':
    unittest.main()
