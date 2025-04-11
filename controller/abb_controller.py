from fastapi import APIRouter, HTTPException
from model.pet import Pet
from service.abb_service import abb_service

router = APIRouter()

@router.post("/pets")
def create_pet(pet: Pet):
    try:
        abb_service.create(pet)
        return {"message": "Pet added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pets")
def list_pets():
    return abb_service.inorder()

@router.get("/pets/count-by-breeds")
def get_count_by_breeds():
    return abb_service.count_by_breeds()

@router.get("/pets/{pet_id}/exists")
def pet_exists(pet_id: int):
    return {"exists": abb_service.exists(pet_id)}

@router.put("/pets/{pet_id}")
def update_pet(pet_id: int, pet: Pet):
    try:
        abb_service.update(pet_id, pet)
        return {"message": "Pet updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    try:
        abb_service.delete(pet_id)
        return {"message": "Pet deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
