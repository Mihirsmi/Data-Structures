from Queue import Queue
class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

def insertNode(data,current):
	if current is None:
		current = Node(data)
		return current
	
	#Insertion at left
	if current.data > data:
		if current.left is None:
			current.left = Node(data)
			return None
		else:
			insertNode(data,current.left)
			
	#Insertion at right
	else:
		if current.right is None:
			current.right = Node(data)
			return None
		else:
			insertNode(data,current.right)

def inorder_traversal(current):
	if current is None:
		return 
	inorder_traversal(current.left)
	print current.data
	inorder_traversal(current.right)

def preorder_traversal(current):
	if current is None:
		return
	print current.data
	preorder_traversal(current.left)
	preorder_traversal(current.right)

def postorder_traversal(current):
	if current is None:
		return
	postorder_traversal(current.left)
	postorder_traversal(current.right)
	print current.data

def levelorder_traversal(root):
	if root is None:
		return
	q = Queue()
	q.put(root)
	while not q.empty():
		levelq = Queue()
		while not q.empty():
			levelq.put(q.get())
		while not levelq.empty():
			node = levelq.get()
			if node.left is not None:
				q.put(node.left)
			if node.right is not None:
				q.put(node.right)
			print node.data,		
		print  
	return

#def deleteNode():	

root = None
root = insertNode(8,root)
insertNode(11,root)
insertNode(5,root)
insertNode(6,root)
insertNode(4,root)
insertNode(10,root)
insertNode(12,root)
print 'Inorder Traversal'
inorder_traversal(root)
print 'Level Order Traversal'
levelorder_traversal(root)
