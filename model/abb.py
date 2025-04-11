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
            raise Exception("Ya existe una mascota con ese ID.")

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def list_nodes_preorder_with_children(self):
        result = []
        self._collect_preorder_with_children(self.root, result, 1)  # size inicia en 1
        return result

    def _collect_preorder_with_children(self, node, result, depth):
        if node:
            pet_data = {
                "id": node.data.id,
                "name": node.data.name,
                "age": node.data.age,
                "breed": node.data.breed,
                "gender": node.data.gender,
                "location": node.data.location,
                "size": depth,
                "left": {
                    "id": node.left.data.id,
                    "name": node.left.data.name
                } if node.left else None,
                "right": {
                    "id": node.right.data.id,
                    "name": node.right.data.name
                } if node.right else None
            }
            result.append(pet_data)
            self._collect_preorder_with_children(node.left, result, depth + 1)
            self._collect_preorder_with_children(node.right, result, depth + 1)

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

    def get_by_id(self, pet_id: int):
        return self._get_by_id_recursive(self.root, pet_id)

    def _get_by_id_recursive(self, node, pet_id: int):
        if node is None:
            return None
        if pet_id == node.data.id:
            return node.data
        elif pet_id < node.data.id:
            return self._get_by_id_recursive(node.left, pet_id)
        else:
            return self._get_by_id_recursive(node.right, pet_id)

    def delete(self, pet_id: int):
        self.root = self._delete_recursive(self.root, pet_id)

    def _delete_recursive(self, node, pet_id: int):
        if node is None:
            raise Exception("Mascota no encontrada")
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
        self._count_breeds_recursive(self.root, breeds)
        return breeds

    def _count_breeds_recursive(self, node, breeds):
        if node:
            breed = node.data.breed
            breeds[breed] = breeds.get(breed, 0) + 1
            self._count_breeds_recursive(node.left, breeds)
            self._count_breeds_recursive(node.right, breeds)

    def report_by_location_and_gender(self):
        report = {}
        self._report_recursive(self.root, report)
        return report

    def _report_recursive(self, node, report):
        if node:
            loc = node.data.location
            gen = node.data.gender
            if loc not in report:
                report[loc] = {"M": 0, "H": 0, "total": 0}
            report[loc][gen] += 1
            report[loc]["total"] += 1
            self._report_recursive(node.left, report)
            self._report_recursive(node.right, report)
