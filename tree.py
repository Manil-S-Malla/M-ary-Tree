from MAryTree import MAryTree

tree = MAryTree(
    'root', [
        MAryTree('a', [
            MAryTree('aa'), 
            MAryTree('ab')
        ]),
        MAryTree('b', [
            MAryTree('ba'),
            MAryTree('bb'),
            MAryTree('bc', [
                MAryTree('bca'),
                MAryTree('bcb'),
                MAryTree('bcc')
            ])
        ]),
        MAryTree('c')
        ]
    )

print('\n\t\t\t M-ary Tree')
print(f"\n\t This program lets you emulate a M-ary Tree and some of it's functions.\n")
print('''tree = MAryTree(
    'root', [
        MAryTree('a', [
            MAryTree('aa'), 
            MAryTree('ab')
        ]),
        MAryTree('b', [
            MAryTree('ba'),
            MAryTree('bb'),
            MAryTree('bc', [
                MAryTree('bca'),
                MAryTree('bcb'),
                MAryTree('bcc')
            ])
        ]),
        MAryTree('c')
        ]
    )
    is a m-ary tree.

    It is displayed as \n
''')
tree.display()

print(f'It has {tree.no_of_nodes()} nodes')

print(f'and has a height of {tree.get_height()}.')


