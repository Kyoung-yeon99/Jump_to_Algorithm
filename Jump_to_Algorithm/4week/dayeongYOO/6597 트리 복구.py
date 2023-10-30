def get_postorder(preorder, inorder):
    if len(preorder) <= 1:
        return preorder
    k_i = inorder.index(preorder[0])
    return get_postorder(preorder[1:k_i + 1], inorder[:k_i]) + get_postorder(preorder[k_i + 1:], inorder[k_i + 1:]) + \
           preorder[0]


while True:
    try:
        query = input()
        preorder, inorder = query.split()
        if not preorder:
            break
        print(get_postorder(preorder, inorder))
    except EOFError:
        break
