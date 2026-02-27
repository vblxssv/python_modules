from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum

# V.2 Requirements: ContactType Enum
class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

# AlienContact Model
class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_business_rules(self) -> 'AlienContact':
        # 1. Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # 2. Physical contact reports must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        # 3. Telepathic contact requires at least 3 witnesses
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')

        # 4. Strong signals (> 7.0) should include received messages
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should include received messages')
            
        return self

def main():
    print("Alien Contact Log Validation")
    print("=" * 38)

    # 1. Создание валидного экземпляра
    try:
        valid_data = {
            "contact_id": "AC_2024_001",
            "timestamp": datetime.now(),
            "location": "Area 51, Nevada",
            "contact_type": "radio",
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 5,
            "message_received": "Greetings from Zeta Reticuli"
        }
        contact = AlienContact(**valid_data)
        
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
        
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 38)

    # 2. Попытка создания невалидного экземпляра (telepathic < 3 witnesses)
    print("Expected validation error:")
    try:
        invalid_data = {
            "contact_id": "AC_XFILE_99",
            "timestamp": datetime.now(),
            "location": "Roswell",
            "contact_type": "telepathic",
            "signal_strength": 5.0,
            "duration_minutes": 10,
            "witness_count": 1  # Ошибка здесь
        }
        AlienContact(**invalid_data)
    except ValidationError as e:
        # Извлекаем только чистое сообщение об ошибке (Value error, ...)
        # Убираем префикс "Value error, ", чтобы соответствовать примеру
        raw_msg = e.errors()[0]['msg']
        print(raw_msg.replace("Value error, ", ""))

if __name__ == "__main__":
    main()