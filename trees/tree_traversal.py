def preorder(node):
    if node:
        print(node['val'])
        preorder(node.get('left'))
        preorder(node.get('right'))


def postorder(node):
    if node:
        postorder(node.get('left'))
        postorder(node.get('right'))
        print(node['val'])


def inorder(node):
    if node:
        inorder(node.get('left'))
        print(node['val'])
        inorder(node.get('right'))


def create_tree():
    tree = {'val': 'Aloo 1',
            'left': {
                'val': 'Achieng 2'
            },
            'right': {
                'val': 'Atieno 3'
            }
            }
    return tree
