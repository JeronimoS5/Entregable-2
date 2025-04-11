from model.abb import ABB
from model.pet import Pet

class ABBService:
    def __init__(self):
        self.abb = ABB()

    def create(self, pet: Pet):
        self.abb.add(pet)

    def inorder(self):
        return self.abb.inorder()

    def count_by_breeds(self):
        return self.abb.count_by_breeds()

    def exists(self, pet_id: int):
        return self.abb.exists(pet_id)

    def update(self, pet_id: int, new_pet: Pet):
        self.abb.find_and_update(pet_id, new_pet)

    def delete(self, pet_id: int):
        self.abb.delete(pet_id)

# Instancia global del servicio
abb_service = ABBService()
