from model.pet import Pet

class NodeABB:
    def __init__(self, data: Pet):
        self.data = data
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def add(self, data: Pet):
        if self.root is None:
            self.root = NodeABB(data)
        else:
            self._add_recursive(self.root, data)

    def _add_recursive(self, node, data: Pet):
        if data.id < node.data.id:
            if node.left is None:
                node.left = NodeABB(data)
            else:
                self._add_recursive(node.left, data)
        elif data.id > node.data.id:
            if node.right is None:
                node.right = NodeABB(data)
            else:
                self._add_recursive(node.right, data)
        else:
            raise Exception("Pet with this ID already exists")

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def exists(self, pet_id: int):
        return self._exists_recursive(self.root, pet_id)

    def _exists_recursive(self, node, pet_id: int):
        if node is None:
            return False
        if pet_id == node.data.id:
            return True
        elif pet_id < node.data.id:
            return self._exists_recursive(node.left, pet_id)
        else:
            return self._exists_recursive(node.right, pet_id)

    def find_and_update(self, pet_id: int, new_pet: Pet):
        node = self._find_node(self.root, pet_id)
        if node:
            node.data = new_pet
        else:
            raise Exception("Pet not found")

    def _find_node(self, node, pet_id: int):
        if node is None:
            return None
        if pet_id == node.data.id:
            return node
        elif pet_id < node.data.id:
            return self._find_node(node.left, pet_id)
        else:
            return self._find_node(node.right, pet_id)

    def delete(self, pet_id: int):
        self.root = self._delete_recursive(self.root, pet_id)

    def _delete_recursive(self, node, pet_id: int):
        if node is None:
            raise Exception("Pet not found")
        if pet_id < node.data.id:
            node.left = self._delete_recursive(node.left, pet_id)
        elif pet_id > node.data.id:
            node.right = self._delete_recursive(node.right, pet_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data.id)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def count_by_breeds(self):
        breeds = {}
        self._count_by_breeds_recursive(self.root, breeds)
        return breeds

    def _count_by_breeds_recursive(self, node, breeds):
        if node:
            breed = node.data.breed
            breeds[breed] = breeds.get(breed, 0) + 1
            self._count_by_breeds_recursive(node.left, breeds)
            self._count_by_breeds_recursive(node.right, breeds)
