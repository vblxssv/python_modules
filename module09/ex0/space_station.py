from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

# IV.2 Requirements: SpaceStation Model
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)

def main():
    print("Space Station Data Validation")
    print("=" * 40)

    # 1. Создание валидного экземпляра
    try:
        valid_data = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": datetime.now(),
        }
        station = SpaceStation(**valid_data)
        
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational else 'Down'}")
        
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 40)

    # 2. Попытка создания невалидного экземпляра (crew_size > 20)
    print("Expected validation error:")
    try:
        invalid_data = {
            "station_id": "ISS002",
            "name": "Mars Gateway",
            "crew_size": 25,  # Ошибка: больше 20
            "power_level": 50.0,
            "oxygen_level": 50.0,
            "last_maintenance": datetime.now()
        }
        SpaceStation(**invalid_data)
    except ValidationError as e:
        # Извлекаем только текстовое сообщение об ошибке
        # В Pydantic v2 это поле 'msg' в первой ошибке списка
        error_msg = e.errors()[0]['msg']
        print(error_msg)

if __name__ == "__main__":
    main()