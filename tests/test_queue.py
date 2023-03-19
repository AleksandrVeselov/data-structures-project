"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src import queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        """Тест правильности работы очереди"""

        q = queue.Queue()
        q.enqueue('data1')  # добавление в очередь первого элемента

        assert q.head.data == 'data1'  # проверка что он добавился в начало очереди
        assert q.head.next_node is None  # проверка что за ним никого нет

        q.enqueue('data2')  # добавление в очередь второго элемента
        assert q.tail.data == 'data2'  # проверка что он добавился в конец очереди
        assert q.tail.next_node is None  # проверка что за ним никого нет
        assert q.head.next_node.data == 'data2'  # проверка что у головы очереди есть ссылка на следующий в очереди элемент

        q.enqueue('data3')  # добавление в очередь третьего элемента
        assert q.tail.data == 'data3'  # проверка что он добавился в конец очереди
        assert q.tail.next_node is None  # проверка что за ним никого нет
        assert q.head.next_node.next_node.data == 'data3'  # проверка наличия ссылки на него у стоящего впереди элемента

    def test_str(self):
        """Тест правильности работы метода ___str__"""
        q = queue.Queue()
        q.enqueue('data1')  # добавление в очередь первого элемента
        q.enqueue('data2')  # добавление в очередь второго элемента
        q.enqueue('data3')  # добавление в очередь третьего элемента
        assert str(q) == 'data1\ndata2\ndata3'


