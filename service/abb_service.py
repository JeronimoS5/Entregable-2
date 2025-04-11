from model.abb import ABB
from model.pet import Pet

class ABBService:
    def __init__(self):
        self.abb = ABB()

    def create(self, pet: Pet):
        self.abb.add(pet)

    def list_as_tree(self):
        return self.abb.list_nodes_preorder_with_children()

    def preorder(self):
        return self.abb.preorder()

    def postorder(self):
        return self.abb.postorder()

    def inorder(self):
        return self.abb.inorder()

    def get_by_id(self, pet_id: int):
        pet = self.abb.get_by_id(pet_id)
        if pet is None:
            raise Exception("Mascota no encontrada")
        return pet

    def exists(self, pet_id: int):
        return self.abb.exists(pet_id)

    def delete(self, pet_id: int):
        self.abb.delete(pet_id)

    def update(self, pet_id: int, new_pet: Pet):
        if not self.exists(pet_id):
            raise Exception("Mascota no encontrada")
        self.delete(pet_id)
        self.create(new_pet)

    def count_by_breeds(self):
        return self.abb.count_by_breeds()

    def report_by_location_and_gender(self):
        return self.abb.report_by_location_and_gender()

abb_service = ABBService()
