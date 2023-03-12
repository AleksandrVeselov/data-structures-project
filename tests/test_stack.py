"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src import stack


class TestNode(unittest.TestCase):

    def test_stack(self):
        my_stack = stack.Stack()
        my_stack.push('data1')
        self.assertEqual(my_stack.top.data, 'data1')
        my_stack.push('data2')
        self.assertEqual(my_stack.top.data, 'data2')
        self.assertEqual(my_stack.top.next_node.data, 'data1')
        top = my_stack.pop()
        self.assertEqual(top.data, 'data2')
        self.assertEqual(my_stack.top.data, 'data1')

    def test_node(self):
        n1 = stack.Node(5, None)
        n2 = stack.Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, n1)


