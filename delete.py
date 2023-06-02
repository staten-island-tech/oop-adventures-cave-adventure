
Adventure_name = "a"

class monster_attack():
    def spider_attack():
        print(f"spider bites {Adventure_name} for 40 damage")
        eplayerhp = playerhp - 40
        print(eplayerhp)
        hpcheck()
    def bandit_attack():
        print(f"bandit shanks {Adventure_name} for 30 damage")
        eplayerhp = playerhp - 30
        print(eplayerhp)
        hpcheck()
    def wanderer_attack():
        print(f"wanderer slashes {Adventure_name} for 45 damage")
        eplayerhp = playerhp - 45
        print(eplayerhp)
        hpcheck()
    def mimic_attack():
        print(f"mimic crushes {Adventure_name} for 80 damage")
        eplayerhp = playerhp - 80
        print(eplayerhp)
        hpcheck()
    def goblin_attack():
        print(f"goblin slashes {Adventure_name} for 20 damage")
        eplayerhp = playerhp - 20
        print(eplayerhp)
        hpcheck()

