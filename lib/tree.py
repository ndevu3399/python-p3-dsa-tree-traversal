class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, id):
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current['id'] == id:
                return current
            for child in reversed(current['children']):
                stack.append(child)
        return None