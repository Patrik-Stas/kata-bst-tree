class Node:
	"""Node of a Tree"""

	def __init__(self, key, value, _parent=None):
		self.value = value
		self.key = key

		self._left = None
		self._right = None
		self._parent = _parent;

	def remove_child(self, child_to_remove):
		if (child_to_remove == self._left):
			self._left = None
		elif (child_to_remove == self._right):
			self._right = None

	def print_info(self):
		_left_str = "        " if (self._left == None) else  "_left: " + str(self._left.value) 
		_right_str = "         " if (self._right == None) else  "_right: " + str(self._right.value) 
		_parent_str = "   ROOT" if (self._parent == None) else "   _parent " + str(self._parent.value)
		print "Node(" + str(self.value) + ")  " + _left_str + "  " + _right_str + _parent_str

	def is_leaf(self):
		return (self._left == None) and (self._right == None)

	def is_root(self):
		return self._parent == None

	def set_right(self, child_node):
		self._right = child_node
		child_node._parent = self

	def set_left(self, child_node):
		self._left = child_node
		child_node._parent = self

	def replace_child(self, old_child, new_child):
		if (old_child == self._left):
			self.set_left(new_child)
		elif (old_child == self._right):
			self.set_right(new_child)
		else:
			raise Exception("old_child node not found")
		old_child._parent = None


class TreePrinter:
	def __init__(self, bst):
		self.bst = bst
		self.center = 40

	def printbst(self):
		print "foo"

	def print_preorder(self, nice_print=False):
		self.preorder(self.bst.root, nice_print)

	def preorder(self, traverse_node, nice_print):
		if (traverse_node == None):
			raise Exception("Passing None as node to preorder print is not expected.")
		
		if (nice_print):
			traverse_node.print_info()
		else:
			print str(traverse_node.value) + " ",

		if (traverse_node._left != None):
			self.preorder(traverse_node._left, nice_print)
		if (traverse_node._right != None):
			self.preorder(traverse_node._right, nice_print)



class BstByLinkedList:
	"""Binary Search Tree implemented by Linked List"""
	"""Smaller or equal to _left"""
	"""Bigger           to _right""" 

	def __init__(self):
		self.root = None

	def count_nodes(self):
		return self.__count_nodes(self.root)

	def __count_nodes(self, subtree_root):
		if (subtree_root != None):
			return 1 + self.__count_nodes(subtree_root._left) +  self.__count_nodes(subtree_root._right)
		else: 
			return 0

	def insert(self, key, value):
		if (key == None or value == None):
			raise Exception("Insert key or value is null.")
		elif (self.root == None):
			self.root = Node(key, value, _parent=None)
		else:
			self.__insert(self.root, key, value)

	def __insert(self, subtree_root, key, value):
		if (subtree_root.key == key):
			raise Exception("Duplicate key " + str(key))
		else:
			if (key < subtree_root.key):
				if (subtree_root._left == None):
					subtree_root.set_left(Node(key, value))
				else:
					self.__insert(subtree_root._left, key, value)
			else:
				if (subtree_root._right == None):
					subtree_root.set_right(Node(key, value))
				else:
					self.__insert(subtree_root._right, key, value)

	def __search(self, subtree_root, search_key):
		if (subtree_root == None):
			return None;
		if (subtree_root.key == search_key):
			return subtree_root
		elif (search_key < subtree_root.key):
			return self.__search(subtree_root._left, search_key)
		else: 
			return self.__search(subtree_root._right, search_key) 

	def search(self, search_key):
		node = self.__search(self.root, search_key)
		return node.value if (node != None) else None;

	def find_biggest_node_in_subtree(self, subtree_root):
		if (subtree_root._right == None):
			return subtree_root;
		else:
			return self.find_biggest_node_in_subtree(subtree_root._right)

	def delete(self, key_delete):
		node_to_delete = self.__search(self.root, key_delete)
		if (node_to_delete == None):
			raise Exception("Can't delete node with key " + str(key_delete) + " because it was not found in the tree.")
		deleted_value = node_to_delete.value
		if (node_to_delete == None):
			raise Exception("Value " + str(key_delete) + " not found in the tree.")
		if (node_to_delete.is_leaf()):
			node_to_delete._parent.remove_child(node_to_delete)
		elif (node_to_delete._left == None):
			node_to_delete._parent.replace_child(node_to_delete, node_to_delete._right)
		else:
			replacement_node = self.find_biggest_node_in_subtree(node_to_delete._left)
			if (replacement_node._left != None ):
				replacement_node._parent.replace_child(replacement_node, replacement_node._left)
			else:
				replacement_node._parent.remove_child(replacement_node)
			node_to_delete.key =  replacement_node.key
			node_to_delete.value = replacement_node.value
		return deleted_value




