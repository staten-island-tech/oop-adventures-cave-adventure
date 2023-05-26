
Adventure_name = "a"

class monster_attack():
    def spider_attack():
        print(f"spider bites {Adventure_name} for 40 damage")
        playerhp - "40"
    def bandit_attack():
        print(f"bandit shanks {Adventure_name} for 30 damage")
        playerhp - "30"
    def wanderer_attack():
        print(f"wanderer slashes {Adventure_name} for 45 damage")
        playerhp - "45"
    def mimic_attack():
        print(f"mimic crushes {Adventure_name} for 80 damage")
        playerhp - "80"
    def goblin_attack():
        print(f"goblin slashes {Adventure_name} for 20 damage")
        playerhp - "20"


def goblin_attack():
    playerhp = 100
    print(f"goblin slashes {Adventure_name} for 20 damage")
    endp = playerhp - 20 
    playerhp = endp
    print(playerhp)

goblin_attack()