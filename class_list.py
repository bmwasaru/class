class ShoppingList:
	shopping_list = []

	def add_item(self, item):
		if item in self.shopping_list:
			pass
		self.shopping_list.append(item)
		print(self.shopping_list)

	def remove_item(self, item):
		if item not in self.shopping_list:
			print("Item is not on the list")
			exit()
		self.shopping_list.remove(item)
		print(self.shopping_list)

	def print_hell(self):
		return "Hello There"


class NewList(ShoppingList):
	pass

new = NewList()
new.print_hell()
