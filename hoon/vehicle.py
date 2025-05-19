from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import schema, crud, models
from typing import List

router = APIRouter()

# 차량 등록
@router.post("/", response_model=schema.getVehicle)
def register_Vehicle(vehicle: schema.registerVehicle, db: Session = Depends(get_db)):
    db_vehicle = crud.register_vehicle(db, vehicle)
    return db_vehicle

# 장애 차량 등록 요청
@router.patch("/{vehicle_num}/request-disabled", response_model=schema.getVehicle)
def request_Disabled(vehicle_num: str, data: schema.requestDisabled, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).get(vehicle_num)
    if not vehicle:
        raise HTTPException(status_code=404, detail="차량을 찾을 수 없습니다.")

    if vehicle.is_disabled is False:
        vehicle.is_disabled = True

    vehicle.registered_by = data.registered_by
    db.commit()
    db.refresh(vehicle)
    return vehicle

# 차량 삭제
@router.delete("/{vehicle_num}", status_code=204)
def delete_Vehicle(vehicle_num: str, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).get(vehicle_num)
    if not vehicle:
        raise HTTPException(status_code=404, detail="차량을 찾을 수 없습니다.")

    db.delete(vehicle)
    db.commit()
    return Response(status_code=204)

@router.get("/{registered_by}", response_model=List[schema.getVehicle])
def show_Vehicles(id: int, db: Session = Depends(get_db)):
    return crud.show_vehicles(db, id)
