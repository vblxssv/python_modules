import functools
import time
import re

def spell_timer(func: callable) -> callable:
    """Декоратор для измерения времени выполнения заклинания."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> callable:
    """Фабрика декораторов для проверки уровня магической силы."""
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Проверяем первый позиционный аргумент (power). 
            # Если это метод класса, первым будет self, поэтому берем args[1]
            # В данном задании для cast_spell(self, name, power) сила — это второй аргумент (index 2)
            # Однако, чтобы сделать его универсальным, проверим аргумент 'power' или второй/третий в списке
            pwr = kwargs.get('power') or (args[2] if len(args) > 2 else args[0])
            
            if pwr >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> callable:
    """Декоратор для повторных попыток произнесения заклинания."""
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Статический метод для валидации имени мага."""
        # Минимум 3 символа, только буквы и пробелы
        if len(name) < 3:
            return False
        return bool(re.fullmatch(r"[A-Za-z\s]+", name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Экземплярный метод для произнесения заклинания."""
        return f"Successfully cast {spell_name} with {power} power"

# --- Демонстрация работы ---

@spell_timer
def fireball():
    time.sleep(0.1) # Симуляция долгого каста
    return "Fireball cast!"

def main():
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    
    # Тест статического метода
    print(guild.validate_mage_name("Gandalf")) # True
    print(guild.validate_mage_name("G2"))       # False

    # Тест валидатора силы
    print(guild.cast_spell("Lightning", 15))    # Успех
    print(guild.cast_spell("Fire", 5))          # Ошибка

if __name__ == "__main__":
    main()