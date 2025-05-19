from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schema

def register_vehicle(db: Session, vehicle: schema.registerVehicle):
    db_vehicle = models.Vehicle(
        vehicle_num=vehicle.vehicle_num,
        is_disabled=vehicle.is_disabled,
        registered_by=vehicle.registered_by
    )
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def request_disabled(db: Session, vehicle_num: str, data: schema.requestDisabled):
    vehicle = db.query(models.Vehicle).get(vehicle_num)
    if not vehicle:
        raise HTTPException(status_code=404, detail="차량을 찾을 수 없습니다.")

    if not vehicle.is_disabled:
        vehicle.is_disabled = True

    vehicle.registered_by = data.registered_by
    db.commit()
    db.refresh(vehicle)
    return vehicle

def delete_vehicle(db: Session, vehicle_num: str):
    vehicle = db.query(models.Vehicle).get(vehicle_num)
    if not vehicle:
        raise HTTPException(status_code=404, detail="차량을 찾을 수 없습니다.")

    db.delete(vehicle)
    db.commit()

#관리자 페이지에서만 보이는 모든 차량 조회 기능
def show_vehicles(db: Session, id: int):
    vehicles = db.query(models.Vehicle).filter(models.Vehicle.registered_by == id).all()
    if not vehicle:
        raise HTTPException(status_code=404, detail="등록된 차량이 없습니다.")
    return vehicles
