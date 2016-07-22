#Given Pre-order and In-order traversal we will build a binary tree with insertNode() method
#Given Post-order and In-order traversal we will build a binary tree with insertInBinaryTree() method
#Detail Explanation in Method 
class Node:
	def __init__(self, data=None, right=None, left=None):
		self.data = data
		self.right = right
		self.left = left

def insertNode(preorder, inorder):
	#First element of preorder traversal will be root for that tree/subtree. We will stick with tree for explanation
	#Find index of root in inorder traversal
	#Elements before the root in inorder traversal will be inorder traversal of its left subtree
	#Elements after the root in inorder traversal will be inorder traversal of its right subtree
	#Elements after root with len(left_inorder) will be preorder traversal of its left subtree
	#Elements after len(left_inorder)+1 till end will be preorder traversal of its right subtree
	root = Node(preorder[0]) #First element of preorder traversal
	index = inorder.index(root.data)
	left_inorder = inorder[:index]
	right_inorder = inorder[(index+1):]
 	left_preorder = preorder[1:len(left_inorder)+1]
	right_preorder = preorder[len(left_inorder)+1:]
	
	#If root did not have a left subtree then it won't have any left preorder and left inorder traversal
	#In that case its left child will be None
	#Else it has a left child implying it has left subtree
	if len(left_preorder) == 0 and len(left_inorder) == 0:
		root.left = None
	else:
		root.left = insertNode(left_preorder, left_inorder)

	#If root did not have a right child then it won't have any right subtree
	#In that case right it won't have preoder and right inorder traversal for its right subtree
	#Else it has a right child implying it has right subtree
	if len(right_preorder) == 0 and len(right_inorder) == 0:
		root.right = None
	else:
		root.right =  insertNode(right_preorder, right_inorder)

	#Now that root's left and right subtrees are taken care of we can return root
	return root

def insertInBinaryTree(postorder, inorder):
	#Last element of postorder traversal will be root
	#Find index of root in inorder traversal
	#Elements before root in inorder traversal will be inorder traversal of its left subtree
	#Elements after root in inorder traversal will be inorder traversal of its right subtree
	#First elements of len(left_inorder) will be postorder traversal of its left subtree
	#Next elements after that of len(right_inorder) will be post traversal of its right subtree
	root = Node(postorder[-1]) #Last Element of postorder will be root of that tree/subtree
	index = inorder.index(root.data)
	left_inorder = inorder[:index]
	right_inorder = inorder[(index+1):]
	left_postorder = postorder[:len(left_inorder)]
	right_postorder = postorder[len(left_inorder)+1:len(right_inorder)+1]

        #If root did not have a left subtree then it won't have any left postorder and left inorder traversal
        #In that case its left child will be None
        #Else it has a left child implying it has left subtree
	if len(left_inorder) and len(left_postorder) == 0:
		root.left = None
	else:
		root.left = insertInBinaryTree(left_postorder, left_inorder)

	#If root did not have a right child then it won't have any right subtree
        #In that case right it won't have preoder and right inorder traversal for its right subtree
        #Else it has a right child implying it has right subtree
	if len(right_inorder) == 0 and len(right_inorder) == 0:
		root.right = None
	else:
		root.right = insertInBinaryTree(right_postorder, right_inorder)
	
	#Now that roots left and right subtrees are taken care of, we can return root
	return root

def inorderTraversal(root):
	#If root is None then it has no left,right subtree to traverse
	if root is None:
		return

	#Traverse Whole Left subtree
	inorderTraversal(root.left)

	#Print root's data
	print root.data

	#Traverse Whole right subtree
	inorderTraversal(root.right)

def preOrderTraversal(root):
	if root is None:
		return 
	
	#Print root's data
	print root.data
	
	#Traverse left subtree of root
	preOrderTraversal(root.left)
	
	#Traverse right subtree of root
	preOrderTraversal(root.right)
	
def postOrderTraversal(root):
	if root is None:
		return

	#Traverse whole left subtree
	postOrderTraversal(root.left)

	#Traverse whole right subtree
	postOrderTraversal(root.right)
	
	#Print root's data
	print root.data

preorder = map(int, raw_input('Specify Preorder Traversal of tree ').split(' '))
inorder = map(int, raw_input('Specify Inorder Traversal of tree ').split(' '))
root = Node()
root =  insertNode(preorder, inorder)
print 'Inorder Traversal'
inorderTraversal(root)
print 'Preorder Traversal'
preOrderTraversal(root)
print 'Postorder Traversal'
postOrderTraversal(root)

postorder = map(int, raw_input('Specify Postorder Traversal of tree ').split(' '))
inorder = map(int, raw_input('Specify Inorder Traversal of tree ').split(' '))
preorder_root = Node()
preorder_root = insertInBinaryTree(postorder, inorder)
print 'Inorder Traversal'
inorderTraversal(preorder_root)
print 'Preorder Traversal'
preOrderTraversal(preorder_root)
print 'Postorder Traversal'
postOrderTraversal(preorder_root)

