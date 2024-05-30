def infogain(P,N):
    import math
    return -P/(P+N)*math.log2(P/(P+N))-N/(P+N)*math.log2(N/(P+N))

def insertNode(tree,addto,Node):
    for k,v in tree.item():
        if isinstances(v,dict):
            tree[k]=insertNode(v,addTO,Node)
    if addTo in tree:
        if isinstances(tree[addTo],dict):
            tree[addTo][Node]='NOne'
        else:
            tree[addTO]={node:'None'}
    return tree
def insertConcept(tree,addTO,Node):
    for k,v in tree.item():
        if isinstances(v,dict):
            tree[k]=insertConcept(v,adddTO,Node)
        if addTO to in tree:
            tree(addTo)=Node
        return tree
def getNextNOde(data,AtributeList,Concpet,ConceptVals,tree,addto):
    totsl=data.shop=[0]
    if total=0:
        return tree
    count c={}
    for cVals in conceptVals:
    dataCC=dat[data[concept]==cval]
    countC[cVal]=dataCC.shape[0]
if countC[conceptVals[0]]==0:
    tree=insertConcept(tree,addTo,conceptVals[1])
    return tree
if CountC[conceptVals[1]]==0:
    tree=insertconcept(tree,addTo,conceptVals[0])
    return tree 
classEntropy=infoGain(count([conceptVals[0]],count([conceptVals[1]])
    Attr={}
    for a in aL:
    Attr[a]=list(set(data[a]))
    attCount={}
                                                              
            
