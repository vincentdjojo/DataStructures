#Reference: https://www.youtube.com/watch?v=f5dU3xoE6ms
class node:
    def __init__ ( self, value = None ):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__ ( self ):
        self.root = None

    def insert ( self, value ):
        if ( self.root == None ):
            self.root = node ( value )
        else:
            self._insert ( value, self.root )

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
                cur_node.left_child.parent=cur_node # set parent
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
                cur_node.right_child.parent=cur_node # set parent
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree ( self ):
        if ( self.root != None ):
            self._print_tree ( self.root )

    def _print_tree ( self, cur_node ):
        if ( cur_node != None ):
            self._print_tree ( cur_node.left_child )
            print ( str ( cur_node.value ) )
            self._print_tree ( cur_node.right_child )

    def height ( self ):
        if ( self.root != None ):
            return self._height ( self.root, 0 )
        else:
            return 0
    def _height ( self, cur_node, cur_height ):
        if ( cur_node == None ): return cur_height
        left_height = self._height ( cur_node.left_child, cur_height + 1 )
        right_height = self._height ( cur_node.right_child, cur_height + 1 )
        return max ( left_height, right_height )

    def search ( self, value ):
        if( self.root != None ):
            return self._search ( value, self.root )
        else:
            return False

    def _search ( self, value, cur_node ):
        if ( value == cur_node.value ):
            return True
        elif ( value < cur_node.value and cur_node.left_child != None ):
            return self._search ( value, cur_node.left_child )
        elif ( value > cur_node.value and cur_node.right_child != None ):
            return self._search ( value, cur_node.right_child )
        return False
tree = binary_search_tree () 
tree.insert ( 1 )
tree.insert ( 2 )
tree.insert ( 4 )
tree.insert ( 3 )
tree.print_tree ()
print ( tree.search ( 4 ) )
