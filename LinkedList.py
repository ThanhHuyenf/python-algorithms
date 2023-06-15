class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while temp.next is not None:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True

  def pop_first(self):
    if self.head is None:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp

  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    temp = self.get(index-1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True

  def remove(self, index):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.pop_first()
    if index == self.length:
      return self.pop()
    temp = self.get(index-1)
    removed = temp.next
    temp.next = removed.next
    removed.next = None
    if self.length == 0:
      self.tail = None
    self.length -= 1
    return removed

  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
    return True

  def remove_duplicates(self):
    values = set()
    previous = None
    current = self.head
    while current:
      if current.value in values:
        previous.next = current.next
        self.length -= 1
      else:
        values.add(current.value)
        previous = current
      current = current.next


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
# my_linked_list.print_list()
my_linked_list.pop()
# my_linked_list.print_list()
my_linked_list.prepend(1)
# my_linked_list.print_list()

# print(my_linked_list.get(2).value)
# print(my_linked_list.get(4).value)
my_linked_list.set_value(1, 2)
# my_linked_list.print_list()

my_linked_list.insert(0, 5)
# my_linked_list.print_list()

my_linked_list.remove(1)
my_linked_list.print_list()