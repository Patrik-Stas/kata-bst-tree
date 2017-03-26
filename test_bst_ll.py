import unittest
from bst_ll import BstByLinkedList

class TestBstByLinkedList(unittest.TestCase):
	"""Tests for `primes.py`."""

	def test_new_tree_should_be_empty(self):
		bst = BstByLinkedList()

		self.assertIsNone(bst.root)


	def test_root_should_have_empty__parent(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50, "a")

		self.assertIsNotNone(bst.root)
		self.assertIsNone(bst.root._parent)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("a", bst.root.value)


	def test_it_should_insert_smaller_to__left(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50, "a")
		node2 = bst.insert(30, "b")

		self.assertEquals(None, bst.root._right)
		self.assertEquals(50, bst.root.key)
		self.assertEquals("a",  bst.root.value)
		self.assertEquals(30, bst.root._left.key)
		self.assertEquals("b",  bst.root._left.value)


	def test_it_should_insert_bigger_to__right(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50,  "a")
		node2 = bst.insert(100, "b")

		self.assertEquals(None, bst.root._left)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("a",  bst.root.value)
		self.assertEquals(100, bst.root._right.key)
		self.assertEquals("b", bst.root._right.value)


	def test_it_should_throw_exception_on_duplicate_key_insertion(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		
		with self.assertRaises(Exception) as context:
			node2 = bst.insert(50, "b")
		self.assertTrue('Duplicate key 50' in context.exception)


	def test_it_should_not_throw_exception_duplicate_value(self):
		bst = BstByLinkedList()
		
		bst.insert(50, "a")
		bst.insert(60, "a")	

		self.assertEquals("a", bst.root.value)
		self.assertEquals("a", bst.root._right.value)


	def test_insert__left__right(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(40, "c")

		self.assertIsNone(bst.root._right)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("a", bst.root.value)
		self.assertEquals(25,  bst.root._left.key)
		self.assertEquals("b", bst.root._left.value)
		self.assertEquals(40,  bst.root._left._right.key)
		self.assertEquals("c", bst.root._left._right.value)


	def test_insert__left__left(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(10, "c")

		self.assertIsNone(bst.root._right)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("a", bst.root.value)
		self.assertEquals(25,  bst.root._left.key)
		self.assertEquals("b", bst.root._left.value)
		self.assertEquals(10,  bst.root._left._left.key)
		self.assertEquals("c", bst.root._left._left.value)


	def test_insert__right__left(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50, "a")
		node2 = bst.insert(70, "b")
		node2 = bst.insert(60, "c")

		self.assertIsNone(bst.root._left)
		self.assertEquals("a", bst.root.value)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("b", bst.root._right.value)
		self.assertEquals(70,  bst.root._right.key)
		self.assertEquals("c", bst.root._right._left.value)
		self.assertEquals(60,  bst.root._right._left.key)


	def test_insert__left__left(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50, "a")
		node2 = bst.insert(70, "b")
		node2 = bst.insert(80, "c")

		self.assertIsNone(bst.root._left)
		self.assertEquals("a", bst.root.value)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("b", bst.root._right.value)
		self.assertEquals(70,  bst.root._right.key)
		self.assertEquals("c", bst.root._right._right.value)
		self.assertEquals(80,  bst.root._right._right.key)


	def test_insert_complex(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50,  "a")
		node2 = bst.insert(25,  "b")
		node2 = bst.insert(75,  "c")
		node2 = bst.insert(100, "d")
		node2 = bst.insert(10,  "e")
		node2 = bst.insert(15,  "f")
		node2 = bst.insert(40,  "g")

		self.assertEquals("a", bst.root.value)
		self.assertEquals(50,  bst.root.key)
		self.assertEquals("b", bst.root._left.value)
		self.assertEquals(25,  bst.root._left.key)
		self.assertEquals("c", bst.root._right.value)
		self.assertEquals(75,  bst.root._right.key)
		self.assertEquals("d", bst.root._right._right.value)
		self.assertEquals(100, bst.root._right._right.key)
		self.assertEquals("e", bst.root._left._left.value)
		self.assertEquals(10,  bst.root._left._left.key)
		self.assertEquals("f", bst.root._left._left._right.value)
		self.assertEquals(15,  bst.root._left._left._right.key)
		self.assertEquals("g", bst.root._left._right.value)
		self.assertEquals(40,  bst.root._left._right.key)


	def test_empty_tree_should_have_zero_nodes(self):
		bst = BstByLinkedList()

		self.assertEquals(0, bst.count_nodes())


	def test_it_should_count_every_inserted_node(self):
		bst = BstByLinkedList()

		node1 = bst.insert(50,  "a")
		node2 = bst.insert(25,  "a")
		node2 = bst.insert(75,  "a")
		node2 = bst.insert(100, "d")
		node2 = bst.insert(10,  "e")

		self.assertEquals(5, bst.count_nodes())


	def test_it_should_find_value_in_root(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(75, "c")
		node2 = bst.insert(15, "e")

		search_value = bst.search(50)

		self.assertEquals("a", search_value)


	def test_it_should_find_value_in_left_right_leaf(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(75, "c")
		node2 = bst.insert(10, "d")
		node2 = bst.insert(15, "e")

		search_value = bst.search(15)

		self.assertEquals("e", search_value)


	def test_it_should_find_value_in_left_left_leaf(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(75, "c")
		node2 = bst.insert(10, "d")

		search_value = bst.search(10)

		self.assertEquals("d", search_value)


	def test_it_should_find_value_in_node_with_both_childs(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(75, "c")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(10, "d")
		node2 = bst.insert(35, "e")

		search_value = bst.search(25)

		self.assertEquals("b", search_value)


	def test_it_should_delete_root(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(10, "d")
		node2 = bst.insert(100, "e")

		bst.delete(50)

		self.assertIsNotNone(bst.search(10))
		self.assertIsNotNone(bst.search(100))
		self.assertIsNone(bst.search(50))

	def test_it_should_delete_left_leaf(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(10, "d")
		node2 = bst.insert(35, "e")

		bst.delete(10)

		self.assertIsNone(bst.search(10))


	def test_it_should_delete_right_leaf(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(10, "d")
		node2 = bst.insert(35, "e")

		bst.delete(35)

		self.assertIsNone(bst.search(35))


	def test_it_should_substitute_deleted_inner_node_with_biggest_node_from_left_subtree(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(35, "f")
		node2 = bst.insert(10, "c")
		node2 = bst.insert(3, "d")
		node2 = bst.insert(13, "e")

		bst.delete(25)

		self.assertIsNone(bst.search(25))
		self.assertIsNotNone(bst.search(13))

		self.assertEquals(50, bst.root.key)
		self.assertEquals("a", bst.root.value)

		self.assertEquals(13, bst.root._left.key)
		self.assertEquals("e", bst.root._left.value)

		self.assertEquals(35, bst.root._left._right.key)
		self.assertEquals("f", bst.root._left._right.value)

		self.assertEquals(10, bst.root._left._left.key)
		self.assertEquals("c", bst.root._left._left.value)

		self.assertEquals(3, bst.root._left._left._left.key)
		self.assertEquals("d", bst.root._left._left._left.value)

		self.assertEquals(5, bst.count_nodes())

	def test_it_should_reconnect_child_and_parent_replacement_node_on_delete(self):
		bst = BstByLinkedList()
		node1 = bst.insert(100, "a")
		node2 = bst.insert(90,  "b")
		node2 = bst.insert(95,  "x")
		node2 = bst.insert(80,  "c")
		node2 = bst.insert(70,  "d")
		node2 = bst.insert(89,  "e")
		node2 = bst.insert(88,  "f")

		bst.delete(90)

		self.assertIsNone(bst.search(90))
		self.assertIsNotNone(bst.search(100))
		self.assertIsNotNone(bst.search(80))
		self.assertIsNotNone(bst.search(70))
		self.assertIsNotNone(bst.search(89))
		self.assertIsNotNone(bst.search(88))

		self.assertEquals(100, bst.root.key)
		self.assertEquals("a", bst.root.value)

		self.assertEquals(89, bst.root._left.key)
		self.assertEquals("e", bst.root._left.value)

		self.assertEquals(95, bst.root._left._right.key)
		self.assertEquals("x", bst.root._left._right.value)

		self.assertEquals(80, bst.root._left._left.key)
		self.assertEquals("c", bst.root._left._left.value)

		self.assertEquals(70, bst.root._left._left._left.key)
		self.assertEquals("d", bst.root._left._left._left.value)

		self.assertEquals(88, bst.root._left._left._right.key)
		self.assertEquals("f", bst.root._left._left._right.value)

		self.assertEquals(6, bst.count_nodes())


	def test_it_should_count_one_node_less_after_node_deletion(self):
		bst = BstByLinkedList()
		node1 = bst.insert(50, "a")
		node2 = bst.insert(25, "b")
		node2 = bst.insert(10, "d")
		node2 = bst.insert(35, "e")

		bst.delete(35)

		self.assertEquals(3, bst.count_nodes())




if __name__ == '__main__':
	unittest.main()