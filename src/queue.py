class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        # Если нет начала очереди, добавляем в начало
        if not self.head:
            self.head = Node(data, next_node=None)

        # Если нет хвоста очереди, добавляем в хвост
        elif not self.tail:
            self.tail = Node(data, next_node=None)
            self.head.next_node = self.tail

        # Если есть и голова и хвост, добавляем в хвост, предварительно изменив ссылку на следующий элемент у того,
        # кто уже находился в хвосте
        else:
            node = Node(data, next_node=None)
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        pass

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        list_deque = []  # Список с данными элементов из очереди(сначала пуст)
        node = self.head  # Чтение начинается с головы (FIFO)

        # Пока не достигнем последнего элемента, у которого в атрибуте next_node ничего нет
        while node is not None:
            list_deque.append(node.data)
            node = node.next_node

        return '\n'.join(list_deque)
