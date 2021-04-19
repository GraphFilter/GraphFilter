import os
import unittest
from src.domain.filter_list import FilterList
import src.domain.operations_and_invariants.bool_invariants as i_bool
from src.domain.operations_and_invariants.bool_invariants import Utils
from src.domain.operations_and_invariants import num_invariants as i_num
from src.domain.operations_and_invariants import operations as oper
import networkx as nx


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
        ftl.set_inputs(Helper.list_graphs_from(file), expression, choices)
        return ftl.run_filter()

    @staticmethod
    def some_c_exem(file, expression, choices):
        ftl = FilterList()
        ftl.set_inputs(Helper.list_graphs_from(file), expression, choices)
        boolean = ftl.run_find_counterexample()
        return boolean, ftl.list_out


class ExpressionUnitTests(unittest.TestCase):

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
        ftl = FilterList()
        ftl.set_inputs([], '', [])
        self.assertEqual(expression_translated, ftl.split_translate_expression(expression1)[0])
        self.assertEqual(expression_translated, ftl.split_translate_expression(expression2)[0])
        self.assertEqual(('', 'error'), ftl.split_translate_expression(expression3))

    def test_translate_code_to_code_literal(self):
        i_num.InvariantNum()
        oper.GraphOperations()
        ftl = FilterList()
        ftl.set_inputs([], '', [])
        for inv in i_num.InvariantNum().all:
            expression = f'{inv.code}(G)==1'
            expression_translated = f'{inv.code_literal}(G)==1'
            self.assertEqual(expression_translated, ftl.split_translate_expression(expression)[0])

    def test_name_of_all_num_invariant(self):
        i_num.InvariantNum()
        oper.GraphOperations()
        for inv in i_num.InvariantNum().all:
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6', f'{inv.code}(G)==1', []) >= 0)

    def test_validate_expression(self):
        ftl = FilterList()
        chi = str(i_num.ChromaticNumber.code)
        eta = str(i_num.Nullity.code)
        c = str(oper.Complement.code)
        self.failureException(ftl.validate_expression('xx'))
        self.failureException(ftl.validate_expression(f'{chi}(G)=2'))
        self.failureException(ftl.validate_expression(f'{chi}(G)'))
        self.failureException(ftl.validate_expression(f'{chi}(G)=2l'))
        self.failureException(ftl.validate_expression(f'{chi}(G)=2 OR {eta}({c}(G))=2'))
        self.failureException(ftl.validate_expression(f'{chi}(G)=2 OR {eta}({c}(G))==2 AND {chi}(G)>2'))
        self.failureException(ftl.validate_expression(f'{chi}(G)==2 OR {eta}({c}(G))<2 AND {chi}(G)>=2'))


class DomainUnitTests(unittest.TestCase):

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
        L_integral = (i_bool.IntegralL.name, 'true')
        self.assertEqual(1, Helper.run('resources/graphs/graphs2.g6', '', [L_integral]))

    def test_inv_boolean_false(self):
        no_tree = (i_bool.Tree.name, False)
        self.assertEqual(1, Helper.run('resources/graphs/graphs2.g6', '', [no_tree]))

    def test_name_of_all_bool_invariant(self):
        j = 0
        is_bool = True
        for inv in i_bool.InvariantBool().all:
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6', '', [(inv.name, 'true')]) >= 0)
            self.assertTrue(Helper.run('resources/graphs/single_graph.g6', '', [(inv.name, 'false')]) >= 0)
            is_bool = is_bool and inv.calculate(nx.from_graph6_bytes('I???h?HpG'.encode('utf-8')))
            j = j + 1
        self.assertTrue(isinstance(is_bool, bool))

    def test_all_operations(self):
        ftl = FilterList()
        for opg in oper.GraphOperations.all:
            for opm in oper.MathOperations.all:
                for inv in i_num.InvariantNum.all:
                    self.assertTrue(Helper.run('resources/graphs/single_graph.g6',
                                               f'{str(opm.code)}({str(inv.code)}{str(opg.code)}(G))>0', []) >= 1
                                    )
                    self.assertEqual("",
                                     ftl.validate_expression(f'{str(opm.code)}({str(inv.code)}{str(opg.code)}(G))>0')
                                     )

    def test_find_counterexample(self):
        diam = str(i_num.Diameter.code)
        l_integral = (i_bool.IntegralL.name, 'true')
        tree = (i_bool.Tree.name, 'true')
        self.assertFalse(Helper.some_c_exem('resources/graphs/graphs2.g6', '', [l_integral])[0])
        self.assertTrue(Helper.some_c_exem('resources/graphs/graphs9.g6', f'{diam}(G)<=4', [])[0])
        graph_no_tree = 'ZGC?KA?_a?E??A?K?GWAQ?h?CA?GP?O@gH@CCg??WC?C?QOS?A@?@?]_A@r?'
        self.assertEqual(Helper.some_c_exem('resources/graphs/graphs1.g6', '', [tree])[1][0], graph_no_tree)

    def test_not_100percent_filter(self):
        diam = str(i_num.Diameter.code)
        self.assertEqual(1 / 3, Helper.run('resources/graphs/graphs9.g6', f'{diam}(G)==3', []))

    def test_interpret_composition_functions(self):
        diam = str(i_num.Diameter.code)
        sqrt = str(oper.Sqrt.code)
        c = str(oper.Complement.code)
        self.assertEqual(1, Helper.run('resources/graphs/single_graph.g6', f'{sqrt}({diam}({c}(G)))>0', []))

    def test_invalid_g6(self):
        diam = str(i_num.Diameter.code)
        chi = str(i_num.ChromaticNumber.code)
        self.assertEqual(1, Helper.run('resources/graphs/graphs14.g6', f'{diam}(G)>0', []))
        self.assertEqual(4/5, Helper.run('resources/graphs/graphs14.g6', f'{chi}(G)<8', []))
        self.assertEqual(True, Helper.some_c_exem('resources/graphs/graphs14.g6', f'{chi}(G)<8', [])[0])


class MiscellaneousTests(unittest.TestCase):

    def test_expression_with_choices(self):
        a = str(i_num.AlgebraicConnectivity.code)
        diam = str(i_num.Diameter.code)
        alpha = str(i_num.IndependenceNumber.code)
        gamma = str(i_num.DominationNumber.code)
        eigen1_a = str(i_num.Largest1EigenA.code)
        eigen1_q = str(i_num.Largest1EigenQ.code)
        planar = (i_bool.Planar.name, 'true')
        chordal = (i_bool.Chordal.name, 'true')
        regular = (i_bool.Regular.name, 'true')
        claw_free = (i_bool.ClawFree.name, 'true')
        self.assertEqual(
            1, Helper.run('resources/graphs/graphs3.g6', f'{a}(G)<=5 AND {a}(G)>=2 AND {diam}(G)==2',
                          [regular, claw_free]))

        self.assertEqual(1,
                         Helper.run('resources/graphs/graphs6.g6', f'({alpha}(G)/{gamma}(G))-3 >= (7/8)-{eigen1_a}(G)',
                                    [planar]))

        self.assertEqual(1,
                         Helper.run('resources/graphs/graphs10.g6', f'{eigen1_q}(G)>2 OR {eigen1_q}(G)<=2',
                                    [chordal]))

    def test_largest_eigen_L(self):
        eigen1_l = str(i_num.Largest1EigenL.code)
        tree = (i_bool.Tree.name, 'true')
        No_biconnected = (i_bool.Biconnected.name, 'false')
        self.assertEqual(1, Helper.run('resources/graphs/graphs5.g6', f'{eigen1_l}(G)>5', [tree, No_biconnected]))

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

    def test_random_with_boolean_false(self):
        avg_degree = str(i_num.DegreeAverage.code)
        no_regular = (i_bool.Regular.name, 'false')
        no_tree = (i_bool.Tree.name, 'false')
        tree = (i_bool.Tree.name, 'true')
        connected = (i_bool.Connected.name, 'true')
        self.assertEqual(0.99, Helper.run('resources/graphs/graphs13.g6', f'{avg_degree}(G)<5',
                                          [no_regular, no_tree, connected]))
        self.assertEqual(0.01, Helper.run('resources/graphs/graphs13.g6', '', [tree]))


if __name__ == '__main__':
    unittest.main()
