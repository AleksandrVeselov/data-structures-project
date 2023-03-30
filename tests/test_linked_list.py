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
        print(ll)
        assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

    def test_init_node(self):
        """Тест инициализатора класса Node"""
        node1 = linked_list.Node({'id': 1})
        node2 = linked_list.Node({'id': 2})
        node1.next_node = node2

        assert node1.data == {'id': 1}
        assert node1.next_node.data == {'id': 2}

    def test_to_list(self):
        """Тест метода to_list"""
        # Создаем пустой односвязный список
        ll = linked_list.LinkedList()

        # Добавляем данные
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert ll.to_list() == [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}]

    def test_get_data_by_id(self):
        """тест метода get_data_by_id"""
        # Создаем пустой односвязный список
        ll = linked_list.LinkedList()

        # Добавляем данные
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        assert ll.get_data_by_id(2) == {'id': 2}  # Проверяем работу с корректным ID
        assert ll.get_data_by_id(55) == 'Данных по id 55 не найдено'  # Проверяем работу с некорректным ID
