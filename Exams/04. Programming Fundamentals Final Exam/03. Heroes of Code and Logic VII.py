def hero_index(heroes_f, hero_f):
    for ind, p in enumerate(heroes_f):
        if p[0] == hero_f:
            return ind


def stat_restore(hero_stat_f, max_stat_f, restored_f):
    restored = restored_f
    if hero_stat_f + restored > max_stat_f:
        restored = restored - abs(max_stat_f - (hero_stat_f + restored))
    return restored


n = int(input())
heroes = []

for _ in range(n):
    hero = input().split()
    hero_name, hero_hp, hero_mp = hero
    heroes.append([hero_name, int(hero_hp), int(hero_mp)])

max_hp = 100
max_mana = 200

command = input()

while command != "End":
    command = command.split(" - ")
    action = command[0]
    hero = command[1]
    i = hero_index(heroes, hero)
    if action == "CastSpell":
        mana_needed = int(command[2])
        spell_name = command[3]
        mana_points = int(heroes[i][2])
        if mana_points >= mana_needed:
            heroes[i][2] -= mana_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[i][2]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage_taken = int(command[2])
        attacker = command[3]
        if damage_taken < heroes[i][1]:
            heroes[i][1] -= damage_taken
            print(f"{hero} was hit for {damage_taken} HP by {attacker} and now has {heroes[i][1]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            heroes.pop(i)

    elif action == "Recharge":
        mana_recharge = int(command[2])
        recharged = stat_restore(heroes[i][2], max_mana, mana_recharge)
        heroes[i][2] += recharged
        print(f"{hero} recharged for {recharged} MP!")

    elif action == "Heal":
        heal = int(command[2])
        healed = stat_restore(heroes[i][1], max_hp, heal)
        heroes[i][1] += healed
        print(f"{hero} healed for {healed} HP!")

    command = input()

for h in heroes:
    print(f"{h[0]}")
    print(f"  HP: {h[1]}")
    print(f"  MP: {h[2]}")
