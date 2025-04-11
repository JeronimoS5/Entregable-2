from fastapi import APIRouter, HTTPException
from model.pet import Pet
from service.abb_service import abb_service

router = APIRouter()

@router.get("/pets")
def list_pets():
    return abb_service.list_as_tree()

@router.get("/pets/inorder")
def pets_inorder():
    return abb_service.inorder()

@router.get("/pets/preorder")
def pets_preorder():
    return abb_service.preorder()

@router.get("/pets/postorder")
def pets_postorder():
    return abb_service.postorder()

@router.get("/pets/breeds/count")
def count_by_breeds():
    return abb_service.count_by_breeds()

@router.get("/pets/report/location-gender")
def report_location_gender():
    return abb_service.report_by_location_and_gender()

@router.post("/pets")
def create_pet(pet: Pet):
    try:
        abb_service.create(pet)
        return {"message": "Mascota creada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    try:
        return abb_service.get_by_id(pet_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/pets/{pet_id}/exists")
def exists_pet(pet_id: int):
    return {"exists": abb_service.exists(pet_id)}

@router.put("/pets/{pet_id}")
def update_pet(pet_id: int, pet: Pet):
    try:
        abb_service.update(pet_id, pet)
        return {"message": "Mascota actualizada"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    try:
        abb_service.delete(pet_id)
        return {"message": "Mascota eliminada"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
