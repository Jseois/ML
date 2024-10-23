import random

class NameGenerator:
    def __init__(self):
        self.first_names_male = [
            "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph",
            "Thomas", "Charles", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul",
            "Alexander", "Benjamin", "Nicholas", "Samuel", "Christopher", "Andrew"
        ]
        
        self.first_names_female = [
            "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", 
            "Jessica", "Sarah", "Karen", "Lisa", "Nancy", "Betty", "Margaret", "Emma",
            "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Amelia", "Harper"
        ]
        
        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
            "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Thompson", "White"
        ]

        self.fantasy_prefixes = [
            "Star", "Moon", "Sun", "Wind", "Storm", "Fire", "Ice", "Dawn", "Dusk",
            "Silver", "Golden", "Shadow", "Light", "Dark", "Crystal", "Dragon", "Silent"
        ]
        
        self.fantasy_suffixes = [
            "weaver", "blade", "heart", "soul", "wing", "whisper", "walker", "rider",
            "seeker", "bringer", "singer", "dancer", "keeper", "master", "born", "child"
        ]

        # Mobile Legends heroes organized by role
        self.ml_heroes = {
            "Tank": [
                "Tigreal", "Minotaur", "Akai", "Franco", "Johnson", "Hylos", "Grock",
                "Gatot Kaca", "Belerick", "Khufra", "Atlas", "Barats", "Edith", "Fredrinn"
            ],
            "Fighter": [
                "Alucard", "Bane", "Zilong", "Freya", "Chou", "Sun", "Alpha", "Ruby",
                "Argus", "Martis", "Leomord", "Thamuz", "X.Borg", "Silvanna", "Yu Zhong",
                "Paquito", "Yin", "Julian"
            ],
            "Assassin": [
                "Saber", "Fanny", "Hayabusa", "Natalia", "Karina", "Gusion", "Helcurt",
                "Selena", "Hanzo", "Ling", "Joy", "Aamon", "Mathilda", "Benedetta"
            ],
            "Mage": [
                "Alice", "Nana", "Eudora", "Aurora", "Cyclops", "Odette", "Kagura",
                "Harley", "Vexana", "Valir", "Lunox", "Harith", "Lylia", "Cecilion",
                "Yve", "Valentina", "Xavier"
            ],
            "Marksman": [
                "Miya", "Bruno", "Clint", "Layla", "Karrie", "Irithel", "Yi Sun-shin",
                "Lesley", "Hanabi", "Claude", "Granger", "Wanwan", "Popol and Kupa",
                "Brody", "Beatrix", "Melissa"
            ],
            "Support": [
                "Rafaela", "Estes", "Angela", "Diggie", "Lolita", "Carmilla", "Floryn",
                "Faramis", "Mathilda", "Yin", "Julian"
            ]
        }

    def generate_regular_name(self, gender=None):
        """Generate a regular first and last name"""
        if gender == "male":
            first = random.choice(self.first_names_male)
        elif gender == "female":
            first = random.choice(self.first_names_female)
        else:
            # Randomly choose gender if none specified
            first = random.choice(self.first_names_male + self.first_names_female)
            
        last = random.choice(self.last_names)
        return f"{first} {last}"

    def generate_fantasy_name(self):
        """Generate a fantasy-style name"""
        return random.choice(self.fantasy_prefixes) + random.choice(self.fantasy_suffixes)

    def generate_ml_hero(self, role=None):
        """Generate a Mobile Legends hero name, optionally filtered by role"""
        if role:
            if role in self.ml_heroes:
                return random.choice(self.ml_heroes[role])
            else:
                raise ValueError(f"Invalid role. Choose from: {', '.join(self.ml_heroes.keys())}")
        else:
            # If no role specified, choose from all heroes
            all_heroes = [hero for heroes in self.ml_heroes.values() for hero in heroes]
            return random.choice(all_heroes)

    def generate_multiple_names(self, count=5, name_type="regular", gender=None, role=None):
        """Generate multiple names of specified type"""
        names = []
        for _ in range(count):
            if name_type == "fantasy":
                names.append(self.generate_fantasy_name())
            elif name_type == "ml_hero":
                names.append(self.generate_ml_hero(role))
            else:
                names.append(self.generate_regular_name(gender))
        return names

# Example usage
generator = NameGenerator()

# Generate random ML heroes
print("Random ML Hero:", generator.generate_ml_hero())

# Generate ML heroes by role
print("\nRandom Tank:", generator.generate_ml_hero(role="Tank"))
print("Random Assassin:", generator.generate_ml_hero(role="Assassin"))

# Generate multiple ML heroes
print("\nMultiple Random Heroes:", generator.generate_multiple_names(3, name_type="ml_hero"))
print("Multiple Mages:", generator.generate_multiple_names(3, name_type="ml_hero", role="Mage"))

# Original functionality still works
print("\nRegular name:", generator.generate_regular_name())
print("Fantasy name:", generator.generate_fantasy_name())
