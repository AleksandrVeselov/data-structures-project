"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src import stack


class TestNode(unittest.TestCase):

    def test_stack(self):
        test_data = stack.Node('тест инициализатора node')
        self.assertEqual(test_data.data, 'тест инициализатора node')

        # Тест инициализатора Stack
        my_stack = stack.Stack()
        self.assertEqual(my_stack.stack, [])

        # Тест метода push(добавление в конец стека)
        my_stack.push('тест методов push/pop')
        my_stack.push('тест методов push/pop_1')
        self.assertEqual(my_stack.stack[0].data, 'тест методов push/pop')
        self.assertEqual(my_stack.stack[1].data, 'тест методов push/pop_1')

        # Тест метода pop(вытаскивание последнего объекта, помещенного в стек)
        pop_data = my_stack.pop()
        self.assertEqual(pop_data.data, 'тест методов push/pop_1')
