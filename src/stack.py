class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, next_node=self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        item = self.top
        self.top = item.next_node
        return item.data

    def __str__(self):
        stack = []  # Список с данными всех элементов из стека(изначально пуст)
        node = self.top  # Берем последний положенный в стек элемент

        # Пока не доберемся первого элемента (у него в атрибуте next_node ничего нет)
        while node is not None:
            stack.append(node.data)
            node = node.next_node
        return '\n'.join(stack)
