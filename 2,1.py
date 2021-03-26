from anytree import Node, RenderTree

x0 = Node("x0")
nix = Node("nix", parent=x0)
eq = Node("eq", parent=nix)
elm = Node("elm", parent=eq)
a = Node("1981", parent=elm)
a = Node("1957", parent=elm)
pog = Node("pog", parent=eq)
a = Node("1981", parent=pog)
a = Node("2019", parent=pog)
dm = Node("dm", parent=nix)
lsl = Node("lsl", parent=nix)
sage = Node("sage", parent=x0)
ioke = Node("ioke", parent=x0)

print(x0)
Node('/x0')

for pre, fill, node in RenderTree(x0):
    print("%s%s" % (pre, node.name))
    # pip install anytree