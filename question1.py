def stack(stack_list, operation=None, new_element=None):

	if operation == 'add' and new_element is not None:
		print("Added the element  " + str(new_element) + "  to the stack.")
		stack_list.insert(0, new_element)

	if operation == 'remove':
		if len(stack_list) == 0:
			print("Stack Underflow: No element in the stack to remove.")
			return None


		print("Removed the element  " + str(stack_list[0]) + "  from the stack.")
		stack_list.pop(0)



def queue(queue_list, operation=None, new_element=None):

	if operation == 'add' and new_element is not None:
		print("Added the element  " + str(new_element) + "  to the queue.")
		queue_list.append(new_element)

	if operation == 'remove':
		if len(queue_list) == 0:
			print("Stack Underflow: No element in the stack to remove.")
			return None


		print("Removed the element  " + str(queue_list[0]) + "  from the queue.")
		queue_list.pop(0)



print("-------------------------------------------")
print('ARRAY IMPLEMENTED AS STACK')
print("-------------------------------------------")
data_list = [1, 2, 3, 4]
print("The Initial Array is ", data_list)
print()

stack(data_list, 'add', 0)
print(data_list)
print()

stack(data_list, 'remove')
print(data_list)
print()

stack(data_list, 'add', 3)
print(data_list)
print()

stack(data_list, 'add', 5)
print(data_list)
print()

stack(data_list, 'remove')
print(data_list)
print()

stack(data_list, 'remove')
print(data_list)
print()


print()
print()
print("-------------------------------------------")
print('ARRAY IMPLEMENTED AS QUEUE')
print("-------------------------------------------")
data_list = [1, 2, 3, 4]
print("The Initial Array is ", data_list)
print()

queue(data_list, 'add', 0)
print(data_list)
print()

queue(data_list, 'remove')
print(data_list)
print()

queue(data_list, 'add', 3)
print(data_list)
print()

queue(data_list, 'add', 5)
print(data_list)
print()

queue(data_list, 'remove')
print(data_list)
print()

queue(data_list, 'remove')
print(data_list)
print()
