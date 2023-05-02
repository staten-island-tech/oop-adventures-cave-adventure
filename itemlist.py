playerhp = int(input("hp input "))
if playerhp <= int(0):
    print("""death""")
if playerhp >= int(100):
    playerhp = 100
print(playerhp)