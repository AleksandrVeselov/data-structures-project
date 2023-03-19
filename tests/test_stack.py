"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src import stack


class TestNode(unittest.TestCase):

    def test_stack(self):
        """Тест класса Stack"""

        my_stack = stack.Stack()  # Создание класса Stack
        my_stack.push('data1')  # Добавление в стек данных
        self.assertEqual(my_stack.top.data, 'data1')  # Проверка добавились ли
        my_stack.push('data2')  # Добавление в стек данных
        self.assertEqual(my_stack.top.data, 'data2')  # Проверка добавились ли
        self.assertEqual(my_stack.top.next_node.data, 'data1')  # Проверка ссылки на следующий элемент стека
        top = my_stack.pop()  # Вынимаем последний добавленный элемент из стека
        self.assertEqual(top, 'data2')  # Проверяем что в нем содержится
        self.assertEqual(my_stack.top.data, 'data1')  # Проверяем что в стеке сейчас следующий элемент

    def test_node(self):
        """Тест класса Node"""

        n1 = stack.Node(5, None)
        n2 = stack.Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, n1)

    def test_str(self):
        my_stack = stack.Stack()  # Создание класса Stack
        my_stack.push('data1')  # Добавление в стек данных
        assert str(my_stack) == 'data1'
        my_stack.push('data2')
        assert str(my_stack) == 'data2\ndata1'



