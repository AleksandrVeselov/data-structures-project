"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src import linked_list


class TestLinkedList(unittest.TestCase):

    def test_linked_list(self):
        """Тест односвязного списка"""

        # Создаем пустой односвязный список
        ll = linked_list.LinkedList()

        # Добавляем данные
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        # Проверяем правильность реализации связного списка и метод __str__
        assert str(ll) == " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    def test_init_node(self):
        """Тест инициализатора класса Node"""
        node1 = linked_list.Node({'id': 1})
        node2 = linked_list.Node({'id': 2})
        node1.next_node = node2

        assert node1.data == {'id': 1}
        assert node1.next_node.data == {'id': 2}


