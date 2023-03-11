"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src import stack


class TestNode(unittest.TestCase):

    def test_stack(self):
        test_data_1 = stack.Node('тест инициализатора node')
        test_data_2 = stack.Node('тест методов push и pop')
        self.assertEqual(test_data_1.data, 'тест инициализатора node')

        # Тест инициализатора Stack
        my_stack = stack.Stack()
        self.assertEqual(my_stack.stack, [])

        # Тест метода push(добавление в конец стека)
        my_stack.push(test_data_1)
        my_stack.push(test_data_2)
        self.assertEqual(my_stack.stack, [test_data_1, test_data_2])

        # Тест метода pop(вытаскивание последнего объекта, помещенного в стек)
        pop_data = my_stack.pop()
        self.assertEqual(pop_data, test_data_2)
        self.assertEqual(my_stack.stack, [test_data_1])
