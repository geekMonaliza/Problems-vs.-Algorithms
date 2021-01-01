# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
from collections import defaultdict


class RouteTrieNode:
    def __init__(self):
        self.children = defaultdict(RouteTrieNode)
        self.handler = None


class RouteTrie:
    def __init__(self, basic_handler):
        self.root = RouteTrieNode()
        self.root.handler = basic_handler
        # Initialize the trie with an root node and a handler, this is the root path or home page node

    def insert(self, arr, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for e in arr:
            node = node.children[e]
        node.handler = handler

    def find(self, arr):
        node = self.root
        for e in arr:
            if e in node.children:
                node = node.children[e]
            else:
                return None
        return node.handler


class Router:
    def __init__(self, basic_handler):
        self.trie = RouteTrie(basic_handler)

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        path_elms = self.split_path(path)
        self.trie.insert(path_elms, handler)

    def lookup(self, path):
        path_elms = self.split_path(path)
        handler = self.trie.find(path_elms)
        return handler

    def split_path(self, path):
        elms = path.split("/")
        final_list = [e for e in elms if e != ""]
        return final_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
