from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enumeration of possible alien contact types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Model for validating alien contact reports with business rules."""

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
    def check_business_rules(self) -> AlienContact:
        """Validate complex business rules after field validation."""

        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        is_physical = self.contact_type == ContactType.physical
        if is_physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        is_tele = self.contact_type == ContactType.telepathic
        if is_tele and self.witness_count < 3:
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses'
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages'
            )

        return self


def main():
    """Demonstrate validation of alien contact logs."""
    print("Alien Contact Log Validation")
    print("=" * 38)

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

    print("Expected validation error:")
    try:
        invalid_data = {
            "contact_id": "AC_XFILE_99",
            "timestamp": datetime.now(),
            "location": "Roswell",
            "contact_type": "telepathic",
            "signal_strength": 5.0,
            "duration_minutes": 10,
            "witness_count": 1
        }
        AlienContact(**invalid_data)
    except ValidationError as e:
        raw_msg = e.errors()[0]['msg']
        print(raw_msg.replace("Value error, ", ""))


if __name__ == "__main__":
    main()
