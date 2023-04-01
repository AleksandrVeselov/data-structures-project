class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None  # начало списка
        self.tail = None  # конец списка

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""

        if not self.head:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node

    def to_list(self) -> list:
        """Преобразование связного списка в обычный"""
        linked_list = []
        beginning = self.head  # Начало связного списка

        # Цикл пока не достигнем конца связного списка
        while beginning:
            linked_list.append(beginning.data)  # выдача данных из элемента связного списка
            beginning = beginning.next_node  # присвоение beginning ссылки на следующий элемент связного списка
        return linked_list

    def get_data_by_id(self, element_id: int) -> dict | str:
        """Получение данных из связного списка по переданному ключу id"""

        beginning = self.head  # Начало связного списка

        # Цикл пока не достигнем конца связного списка
        while beginning:
            try:
                if beginning.data['id'] == element_id:
                    return beginning.data  # возвращение элемента если значение по ключу id совпадает с переданным
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
            beginning = beginning.next_node  # присвоение beginning ссылки на следующий элемент связного списка
        return f'Данных по id {element_id} не найдено'  # Если нужного id не найдено

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
