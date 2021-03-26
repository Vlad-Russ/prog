from anytree import Node, RenderTree

x0 = Node("x0")
pawn = Node("pawn", parent=x0)
a = Node("1984", parent=pawn)
m = Node("m", parent=a)
cobol = Node("cobol", parent=a)
a1 = Node("2014", parent=cobol)
a2 = Node("1982", parent=cobol)
a3 = Node("1982", parent=cobol)

b = Node("1986", parent=pawn)
xojo = Node("xojo", parent=b)
oz = Node("oz", parent=b)
b1 = Node("2014", parent=oz)
b2 = Node("1982", parent=oz)
b3 = Node("2011", parent=oz)

c = Node("1973", parent=pawn)
m = Node("m", parent=c)
xojo = Node("xojo", parent=m)
oz = Node("oz", parent=m)

cobol = Node("cobol", parent=c)

blade = Node("blade", parent=x0)
clips = Node("clips", parent=x0)

print(x0)
Node('/x0')

for pre, fill, node in RenderTree(x0):
    print("%s%s" % (pre, node.name))
    # pip install anytree
