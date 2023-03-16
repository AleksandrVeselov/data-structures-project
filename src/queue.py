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
        if not self.head:
            self.head = Node(data, next_node=None)

        elif not self.tail:
            self.tail = Node(data, next_node=None)
            self.head.next_node = self.tail

        else:
            node = Node(data, next_node=None)
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        if self.tail:
            node = self.tail
            self.tail = self.tail.next_node

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        pass
