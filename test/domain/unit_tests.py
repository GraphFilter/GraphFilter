import os
import unittest

import networkx as nx
import numpy

import source.store.operations_and_invariants.bool_invariants as inv_bool
import source.store.operations_and_invariants.num_invariants as inv_num
import source.store.operations_and_invariants.other_invariants as inv_other
import source.store.operations_and_invariants.operations as oper

from source.domain.equation import Equation
from source.domain.filter_list import FilterList
from source.store.operations_and_invariants.invariants import UtilsToInvariants


class Helper:

    @staticmethod
    def list_graphs_from(name_file):
        file = open(os.path.abspath(name_file), 'r')
        group = file.read().splitlines()
        file.close()
        return group

    @staticmethod
    def run(file, expression, choices):
        ftl = FilterList()
        ftl.set_inputs(Helper.list_graphs_from('resources/graphs/' + file), expression, choices, Helper.fake_update)
        return ftl.run_filter()

    @staticmethod
    def some_c_exem(file, expression, choices):
        ftl = FilterList()
        ftl.set_inputs(Helper.list_graphs_from('resources/graphs/' + file), expression, choices, Helper.fake_update)
        boolean = ftl.run_find_counterexample()
        return boolean, ftl.list_out

    @staticmethod
    def fake_update(value):
        pass


class ExpressionUnitTests(unittest.TestCase):

    def test_split_and_translate_expression(self):
        chi = str(inv_num.ChromaticNumber.code)
        line = str(oper.Line.code)
        omega = str(inv_num.CliqueNumber.code)
        lambda1 = str(inv_num.Largest1EigenA.code)
        n = str(inv_num.NumberVertices.code)
        chi_str = str(inv_num.ChromaticNumber.code_literal)
        line_str = str(oper.Line.code_literal)
        omega_str = str(inv_num.CliqueNumber.code_literal)
        lambda1_str = str(inv_num.Largest1EigenA.code_literal)
        n_str = str(inv_num.NumberVertices.code_literal)
        expression1 = f'{chi}(G)==5 AND {omega}({line}(G))>=1 AND {n}(G)<={lambda1}(G)'
        expression_translated = [f'{chi_str}(G)==5', f'{omega_str}({line_str}(G))>=1', f'{n_str}(G)<={lambda1_str}(G)']
        expression2 = f'{chi}(G)==5 OR {omega}({line}(G))>=1 OR {n}(G)<={lambda1}(G)'
        expression3 = f'{chi}(G)==5 AND {omega}({line}(G))>=1 OR {n}(G)<={lambda1}(G)'
        self.assertEqual(expression_translated, Equation.split_translate_expression(expression1)[0])
        self.assertEqual(expression_translated, Equation.split_translate_expression(expression2)[0])
        self.assertEqual(('', 'error'), Equation.split_translate_expression(expression3))

    def test_translate_code_to_code_literal(self):
        inv_num.InvariantNum()
        oper.GraphOperations()
        for inv in inv_num.InvariantNum().all:
            expression = f'{inv.code}(G)==1'
            expression_translated = f'{inv.code_literal}(G)==1'
            self.assertEqual(expression_translated, Equation.split_translate_expression(expression)[0])

    def test_name_of_all_num_invariant(self):
        inv_num.InvariantNum()
        oper.GraphOperations()
        for inv in inv_num.InvariantNum().all:
            self.assertTrue(Helper.run('single_graph.g6', f'{inv.code}(G)==1', {}) >= 0)
            print(inv.name)

    def test_math_symbol(self):
        # {"<=": "\u2264", ">=": "\u2265", "!=": "\u2260", "**": "^", "pi": "\u03c0"}
        self.assertEqual(1, Helper.run('graphs1.g6', 'floor(2.3) \u2264 floor(2.1) ', {}))
        self.assertEqual(1, Helper.run('graphs1.g6', 'ceiling(1.01) \u2265 1.9 ', {}))
        self.assertEqual(0, Helper.run('graphs1.g6', '2 \u2260 2 ', {}))
        self.assertEqual(1, Helper.run('graphs1.g6', '2^4 \u2265 pi ', {}))

    def test_validate_expression(self):

        chi = str(inv_num.ChromaticNumber.code)
        eta = str(inv_num.Nullity.code)
        c = str(oper.Complement.code)
        self.failureException(Equation.validate_expression('xx'))
        self.failureException(Equation.validate_expression(f'{chi}(G)=2'))
        self.failureException(Equation.validate_expression(f'{chi}(G)'))
        self.failureException(Equation.validate_expression(f'{chi}(G)=2l'))
        self.failureException(Equation.validate_expression(f'{chi}(G)=2 OR {eta}({c}(G))=2'))
        self.failureException(Equation.validate_expression(f'{chi}(G)=2 OR {eta}({c}(G))==2 AND {chi}(G)>2'))
        self.failureException(Equation.validate_expression(f'{chi}(G)==2 OR {eta}({c}(G))<2 AND {chi}(G)>=2'))


class DomainUnitTests(unittest.TestCase):

    def test_AND_logic(self):
        exp1 = str(inv_num.EdgeConnectivity.code) + '(G) >=3'
        exp2 = str(inv_num.VertexConnectivity.code) + '(G) >=5'
        exp3 = str(inv_num.CliqueNumber.code) + '(G) ==4'
        exp4 = str(inv_num.Largest1EigenL.code) + '(G) > 10'
        exp4_n = str(inv_num.Largest1EigenL.code) + '(G) <= 10'
        self.assertEqual(1, Helper.run('graphs11.g6',
                                       f'{exp1} AND {exp2} AND {exp3} AND {exp4}', {}))
        self.assertEqual(0, Helper.run('graphs11.g6',
                                       f'{exp1} AND {exp2} AND {exp3} AND {exp4_n}', {}))

    def test_OR_logic(self):
        exp1 = str(inv_num.EdgeConnectivity.code) + '(G) >=3'
        exp2 = str(inv_num.IndependenceNumber.code) + '(G) >= 7'
        exp1_n = str(inv_num.EdgeConnectivity.code) + '(G) <3'
        exp2_n = str(inv_num.IndependenceNumber.code) + '(G) < 7'

        self.assertEqual(1, Helper.run('graphs12.g6', f'{exp1} OR {exp2}', {}))
        self.assertTrue(Helper.run('graphs12.g6', f'{exp1_n} OR {exp2_n}', {}) < 1)

    def test_integral(self):
        self.assertTrue(UtilsToInvariants.is_integer(1))
        self.assertTrue(UtilsToInvariants.is_integer(1.000001))
        self.assertTrue(UtilsToInvariants.is_integer(0.999998))
        L_integral = {inv_bool.IntegralL.name: 'true'}
        self.assertEqual(1, Helper.run('graphs2.g6', '', L_integral))

    def test_inv_boolean_false(self):
        no_tree = {inv_bool.Tree.name: 'false'}
        self.assertEqual(1, Helper.run('graphs2.g6', '', no_tree))

    def test_name_of_all_bool_invariant(self):
        for inv in inv_bool.InvariantBool().all:
            self.assertTrue(Helper.run('single_graph.g6', '', {inv.name: 'true'}) >= 0)
            self.assertTrue(Helper.run('single_graph.g6', '', {inv.name: 'false'}) >= 0)
            self.assertTrue(isinstance(inv.calculate(nx.from_graph6_bytes('I???h?HpG'.encode('utf-8'))), bool))

    def test_all_invariants_with_trivial_graph(self):
        trivial = nx.trivial_graph()
        for inv in inv_num.InvariantNum().all:
            self.assertTrue(isinstance(inv.calculate(trivial), (float, int, numpy.int32)))
        for inv in inv_bool.InvariantBool().all:
            self.assertTrue(isinstance(inv.calculate(trivial), bool))
        for inv in inv_other.InvariantOther().all:
            self.assertTrue(isinstance(inv.calculate(trivial), (numpy.ndarray, list, tuple, dict, str, set)))
        for op in oper.GraphOperations().all:
            self.assertTrue(isinstance(op.calculate(trivial), nx.Graph))

    def test_calculate_other_invariants(self):
        g = nx.generators.complete_graph(10)
        for inv in inv_other.InvariantOther().all:
            self.assertTrue(isinstance(inv.calculate(g), (numpy.ndarray, list, tuple, dict, str, set)))

    def test_all_operations(self):
        for opg in oper.GraphOperations().all:
            for opm in oper.MathOperations().all:
                for inv in inv_num.InvariantNum().all:
                    print(f'{opm.name}-{str(inv.name)}-{str(opg.name)}')
                    self.assertTrue(Helper.run('single_graph.g6',
                                               f'{str(opm.code)}({str(inv.code)}({str(opg.code)}(G)))>0', {}) >= 0
                                    )

                    self.assertEqual(
                        "", Equation.validate_expression(f'{str(opm.code)}({str(inv.code)}({str(opg.code)}(G)))>0')
                    )

    def test_find_counterexample(self):
        diam = str(inv_num.Diameter.code)
        l_integral = {inv_bool.IntegralL.name: 'true'}
        tree = {inv_bool.Tree.name: 'true'}
        self.assertFalse(Helper.some_c_exem('graphs2.g6', '', l_integral)[0])
        self.assertTrue(Helper.some_c_exem('graphs9.g6', f'{diam}(G)<=4', {})[0])
        graph_no_tree = 'ZGC?KA?_a?E??A?K?GWAQ?h?CA?GP?O@gH@CCg??WC?C?QOS?A@?@?]_A@r?'
        self.assertEqual(Helper.some_c_exem('graphs1.g6', '', tree)[1][0], graph_no_tree)

    def test_not_100percent_filter(self):
        diam = str(inv_num.Diameter.code)
        self.assertEqual(1 / 3, Helper.run('graphs9.g6', f'{diam}(G)==3', {}))

    def test_interpret_composition_functions(self):
        diam = str(inv_num.Diameter.code)
        sqrt = str(oper.Sqrt.code)
        c = str(oper.Complement.code)
        self.assertEqual(1, Helper.run('single_graph.g6', f'{sqrt}({diam}({c}(G)))>0', {}))

    def test_invalid_g6(self):
        diam = str(inv_num.Diameter.code)
        chi = str(inv_num.ChromaticNumber.code)
        self.assertEqual(5 / 8, Helper.run('graphs14.g6', f'{diam}(G)>0', {}))
        self.assertEqual(4 / 8, Helper.run('graphs14.g6', f'{chi}(G)<8', {}))
        self.assertEqual(True, Helper.some_c_exem('graphs14.g6', f'{chi}(G)<8', {})[0])


class MiscellaneousTests(unittest.TestCase):

    def test_expression_with_choices(self):
        a = str(inv_num.AlgebraicConnectivity.code)
        diam = str(inv_num.Diameter.code)
        alpha = str(inv_num.IndependenceNumber.code)
        gamma = str(inv_num.DominationNumber.code)
        eigen1_a = str(inv_num.Largest1EigenA.code)
        eigen1_q = str(inv_num.Largest1EigenQ.code)
        planar = {inv_bool.Planar.name: 'true'}
        chordal = {inv_bool.Chordal.name: 'true'}
        regular_clawfree = {inv_bool.Regular.name: 'true', inv_bool.ClawFree.name: 'true'}
        self.assertEqual(
            1, Helper.run('graphs3.g6', f'{a}(G)<=5 AND {a}(G)>=2 AND {diam}(G)==2',
                          regular_clawfree))

        self.assertEqual(1,
                         Helper.run('graphs6.g6', f'({alpha}(G)/{gamma}(G))-3 >= (7/8)-{eigen1_a}(G)',
                                    planar))

        self.assertEqual(1, Helper.run('graphs10.g6', f'{eigen1_q}(G)>2 OR {eigen1_q}(G)<=2', chordal))

    def test_largest_eigen_L(self):
        eigen1_l = str(inv_num.Largest1EigenL.code)
        tree_NoBiconnected = {inv_bool.Tree.name: 'true', inv_bool.Biconnected.name: 'false'}
        self.assertEqual(1, Helper.run('graphs5.g6', f'{eigen1_l}(G)>5', tree_NoBiconnected))

    def test_wilf_result(self):
        chi = str(inv_num.ChromaticNumber.code)
        eigen1 = str(inv_num.Largest1EigenA.code)
        self.assertEqual(1, Helper.run('graphs7.g6', f'{chi}(G)<={eigen1}(G)+1', {}))

    def test_independence_and_matching(self):
        alpha = str(inv_num.IndependenceNumber.code)
        match = str(inv_num.MatchingNumber.code)
        line = str(oper.Line.code)
        self.assertEqual(1, Helper.run('graphs7.g6', f'{match}(G)=={alpha}({line}(G))', {}))

    def test_perfect_graphs(self):
        chi = str(inv_num.ChromaticNumber.code)
        omega = str(inv_num.CliqueNumber.code)
        self.assertEqual(1, Helper.run('graphs8.g6', f'{chi}(G)=={omega}(G)', {}))

    def test_random_with_boolean_false(self):
        avg_degree = str(inv_num.DegreeAverage.code)
        no_regular_no_tree_connected = {inv_bool.Regular.name: 'false',
                                        inv_bool.Tree.name: 'false',
                                        inv_bool.Connected.name: 'true'
                                        }
        tree = {inv_bool.Tree.name: 'true'}
        self.assertEqual(0.99, Helper.run('graphs13.g6',
                                          f'{avg_degree}(G)<5', no_regular_no_tree_connected))

        self.assertEqual(0.01, Helper.run('graphs13.g6', '', tree))

    def test_main_eigenvalues(self):
        mainA = str(inv_num.MainEigenvalueAdjacency.code)
        self.assertEqual(1, Helper.run('graphs3.g6', f'{mainA}(G)==1', {}))


if __name__ == '__main__':
    unittest.main()
