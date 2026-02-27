from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Enumeration of space agency ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Model representing a single crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Model representing a space mission with complex safety validation."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> SpaceMission:
        """Validate safety requirements for the mission and crew."""
        # 1. Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # 2. Must have at least one Commander or Captain
        senior_ranks = {Rank.commander, Rank.captain}
        if not any(member.rank in senior_ranks for member in self.crew):
            raise ValueError(
                'Mission must have at least one Commander or Captain'
            )

        # 3. All crew members must be active
        if not all(member.is_active for member in self.crew):
            raise ValueError('All crew members must be active')

        # 4. Long missions (> 365 days) need 50% experienced crew (5+ years)
        if self.duration_days > 365:
            exp_crew = [m for m in self.crew if m.years_experience >= 5]
            if len(exp_crew) < (len(self.crew) / 2):
                raise ValueError(
                    'Long missions need 50% experienced crew (5+ years)'
                )

        return self


def main():
    """Demonstrate mission validation with valid and invalid crew setups."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    # 1. Создание валидной миссии
    try:
        crew_list = [
            CrewMember(
                member_id="C01", name="Sarah Connor", rank=Rank.commander,
                age=45, specialization="Mission Command", years_experience=20
            ),
            CrewMember(
                member_id="C02", name="John Smith", rank=Rank.lieutenant,
                age=30, specialization="Navigation", years_experience=8
            ),
            CrewMember(
                member_id="C03", name="Alice Johnson", rank=Rank.officer,
                age=28, specialization="Engineering", years_experience=4
            )
        ]

        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 12, 1),
            duration_days=900,
            budget_millions=2500.0,
            crew=crew_list
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for m in valid_mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 41)

    # 2. Попытка создания невалидной миссии
    print("Expected validation error:")
    try:
        invalid_crew = [
            CrewMember(
                member_id="C04", name="Bob Cadet", rank=Rank.cadet,
                age=20, specialization="Cleaning", years_experience=0
            )
        ]
        SpaceMission(
            mission_id="M_FAIL_01",
            mission_name="Short Trip",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            budget_millions=10.0,
            crew=invalid_crew
        )
    except ValidationError as e:
        raw_msg = e.errors()[0]['msg']
        print(raw_msg.replace("Value error, ", ""))


if __name__ == "__main__":
    main()
