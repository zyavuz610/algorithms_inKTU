# Binary_tree_sort
D, L, R = 'data', 'left', 'right'

def binary_tree_sort(tree, data):
    if tree is None:
        tree = {D: data, L: None, R: None}
    elif data <= tree[D]:
        tree[L] = binary_tree_sort(tree[L], data)
    else:
        tree[R] = binary_tree_sort(tree[R], data)
    return tree

def traverse(tree):
    if tree is not None:
        for data in traverse(tree[L]):
            yield data
        yield tree[D]
        for data in traverse(tree[R]):
            yield data

array = [54,26,93,17,77,31,44,55,20]
tree = None
for i in array:
    tree = binary_tree_sort(tree, i)
print("sıralanmış dizi:",*traverse(tree))