def pFinder(inorder, preorder, imap, p_idx, instart, inend, res):
    if instart > inend:
        return p_idx
    
    root = preorder[p_idx]
    
    r_idx = imap[root]
    
    p_idx += 1
    
    p_idx = pFinder(inorder, preorder, imap, p_idx, instart, r_idx - 1, res)
    
    p_idx = pFinder(inorder, preorder, imap, p_idx, r_idx + 1, inend, res)
    
    res.append(root)
    
    return p_idx

def main():
    
    N = int(input())  

    inorder = list(map(int, input().split())) 

    preorder = list(map(int, input().split())) 
    
    imap = {}
    for idx, value in enumerate(inorder):
        imap[value] = idx

    
    res = []
    
    pFinder(inorder, preorder, imap, 0, 0, N - 1, res)
    
    print(" ".join(map(str, res)))

main()