class MAryTree:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
        self.count = 0
        self.height = 0

    
    def size(self, tree):
        for node in tree:
            if(type(node) is list):         #   If the node has children nodes, use recursion to go deeper in the tree. 
                self.size(node)
            else:         #   If the node has no further children nodes, increase the count of the nodes. 
                self.count += 1
                
        return self.count


    def no_of_nodes(self):
        self.count = 0
        return (self.size(self.children) + 1)


    def __log(self, tree, repeat = 0):
        for node in tree:
            print('|' + ' ' * (repeat * 6) + '|______' +  f'[{str(node.value)}]')
            if(len(node.children) > 0):         #   If the node has children nodes, use recursion to go deeper in the tree. 
                self.__log(node.children, repeat + 1)
                
    
    def __list_log(self, tree, repeat = -1):
        for node in tree:
            if(type(node) is list):         #   If the node has children nodes, use recursion to go deeper in the tree. 
                self.__list_log(node, repeat + 1)
            else:         #   If the node has no further children nodes, display the node. 
                print('|' + ' ' * (repeat * 6) + '|______' +  f'[{str(node)}]')
                
    
    def display(self):
        print(f'[{self.value}]')
        self.__log(self.children)
                

    def __tree_height(self, tree, h = 0):
        for node in tree:
            if len(node.children) > 0:
                self.__tree_height(node.children, h + 1)
            else:
                if self.height < h:
                    self.height = h
        return  self.height

    
    def get_height(self):
        if len(self.children) > 0:
            return self.__tree_height(self.children, 1)
        else:
            return 0

    