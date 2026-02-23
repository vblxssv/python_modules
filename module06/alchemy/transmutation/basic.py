from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    return F"Lead transmuted to gold using {create_fire()}"


def stone_to_gem():
    return F"Stone transmuted to gem using {create_earth()}"
