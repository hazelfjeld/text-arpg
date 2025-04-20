import random

# ==== Item Data ====

shop_armor = {
    "BASIC ARMOR": {"defense": 60, "price": 10},
    "STEEL ARMOR": {"defense": 80, "price": 50},
    "MITHRIL ARMOR": {"defense": 105, "price": 100},
    "DRAGON SCALE ARMOR": {"defense": 150, "price": 300},
    "CELESTIAL PLATE": {"defense": 300, "price": 600}
}
items_armor = {
    "NONE": 50,
    "BASIC ARMOR": 60,
    "STEEL ARMOR": 80,
    "MITHRIL ARMOR": 105,
    "DRAGON SCALE ARMOR": 150,
    "CELESTIAL PLATE": 300
}
items_battle = {
    "BASIC POTION": 40
}
items_drops = {
    "GOBLIN EAR": 5,
    "SPIDER EYE": 8,
    "SLIME BALL": 7,
    "BAT WING": 10,
    "BONE SHARD": 12,
    "ORC TUSK": 15,
    "WOLF FUR": 18,
    "FLAME SCALE": 20,
    "CURSED CLOTH": 25,
    "DRAGON SCALE": 30,
    "BLACK ARMOR": 35,
    "HELLSTONE": 40,
    "HYDRA FANG": 45,
    "SOUL REAPER": 55,
    "DEMONIC KEY": 100  
}

area = 1
class Weapon:
    def __init__(self, name, damage, effect=None):
        self.name = name
        self.damage = damage
        self.effect = effect  # Options: "dot", "burn", "multi_hit", etc.

weapons = {
    None: Weapon("None",20),
    "BASIC SWORD": Weapon("BASIC SWORD", 30),
    "RUSTY SHIV": Weapon("RUSTY SHIV", 35, "multi_hit"),
    "SPIDER FANG SWORD": Weapon("SPIDER FANG SWORD", 40, "dot"),
    "GOO BLADE": Weapon("GOO BLADE", 38, "slow"),
    "ECHOBLADE": Weapon("ECHOBLADE", 36, "echo"),
    "BONE CRUSHER": Weapon("BONE CRUSHER", 40, "execute"),
    "ORC CLEAVER": Weapon("ORC CLEAVER", 45, "recoil"),
    "FERAL CLAWBLADE": Weapon("FERAL CLAWBLADE", 42, "crit"),
    "BLAZING SCIMITAR": Weapon("BLAZING SCIMITAR", 43, "burn"),
    "PHANTOM EDGE": Weapon("PHANTOM EDGE", 39, "armor_pierce"),
    "SCALDFANG": Weapon("SCALDFANG", 48, "fireburst"),
    "VOIDBREAKER": Weapon("VOIDBREAKER", 46, "purge"),
    "HELLFORGED BLADE": Weapon("HELLFORGED BLADE", 50, "lifedrain"),
    "VENOM HYDRA FANG": Weapon("VENOM HYDRA FANG", 44, "stacked_poison"),
    "SOUL REAVER": Weapon("SOUL REAVER", 52, "lifesteal"),
}

# ==== Monster Class ====
class Monster:
    def __init__(self, name, hp, attack, drop):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.drop = drop


# ==== Player Class ====
class Player:
    def __init__(self):
        self.base_health = 50
        self.base_attack = 20
        self.health = self.base_health
        self.attack = self.base_attack
        self.gold = 0
        self.inventory = ["BASIC SWORD", "BASIC ARMOR", "BASIC POTION"]
        self.equipped_armor=None
        self.equipped_weapon=None
    def equip(self, item):
        if item in weapons:
            self.attack = weapons[item].damage
            self.equipped_weapon = item  
            print(f"You equipped {item}. Attack is now {self.attack}.")
        elif item in items_armor:
            self.base_health = items_armor[item]
            self.health = self.base_health  
            self.equipped_armor = item
            print(f"You equipped {item}. Max Health is now {self.health}.")

        else:
            print("You can't equip that.")


    def use_item(self, item):
        if item in items_battle:
            heal_amount = items_battle[item]
            self.base_health = min(self.health, self.base_health + heal_amount)
            self.inventory.remove(item)
            print(f"You used {item} and healed to {self.base_health} HP.")
        else:
            print("You can't use that item.")



# ==== Inventory funcs ====
def battle_items(inventory):
    items_held = []
    for item in inventory:
        if item in items_battle:
            items_held.append(item)
    return items_held

def print_inv(inventory):
    counted = {}
    for item in inventory:
        if item in counted:
            counted[item] += 1
        else:
            counted[item] = 1

    for item, count in counted.items():
        print(f"{item} x{count}")





# === Monster Spawning ===
def create_monster(name, hp, attack, drop, rare_weapon):
    final_drop = rare_weapon if random.random() < 0.05 else drop
    return Monster(name, hp, attack, final_drop)

def spawn_monster(area):
    # All monsters defined here
    goblin = create_monster("Goblin", 30, 10, "GOBLIN EAR", "RUSTY SHIV")
    spider = create_monster("Spider", 40, 10, "SPIDER EYE", "SPIDER FANG SWORD")
    slime = create_monster("Slime", 35, 20, "SLIME BALL", "GOO BLADE")
    bat = create_monster("Bat", 25, 15, "BAT WING", "ECHOBLADE")
    skeleton = create_monster("Skeleton", 45, 18, "BONE SHARD", "BONE CRUSHER")
    orc = create_monster("Orc", 60, 25, "ORC TUSK", "ORC CLEAVER")
    werewolf = create_monster("Werewolf", 70, 28, "WOLF FUR", "FERAL CLAWBLADE")
    fire_lizard = create_monster("Fire Lizard", 65, 30, "FLAME SCALE", "BLAZING SCIMITAR")
    wraith = create_monster("Wraith", 55, 35, "CURSED CLOTH", "PHANTOM EDGE")
    dragonling = create_monster("Dragonling", 100, 40, "DRAGON SCALE", "SCALDFANG")
    corrupted_knight = create_monster("Corrupted Knight", 120, 45, "BLACK ARMOR", "VOIDBREAKER")
    demon = create_monster("Demon", 140, 50, "HELLSTONE", "HELLFORGED BLADE")
    hydra = create_monster("Hydra", 180, 55, "HYDRA FANG", "VENOM HYDRA FANG")
    death = create_monster("Death", 200, 65, "SOUL REAPER", "SOUL REAVER")
    devil = create_monster("Devil", 600, 60, "DEMONIC KEY", "SATAN'S BLADE")

    if area == 1:
        return random.choice([goblin, spider, slime])
    elif area == 2:
        return random.choice([spider, bat, skeleton])
    elif area == 3:
        return random.choice([goblin, orc, wraith])
    elif area == 4:
        return random.choice([orc, werewolf, fire_lizard, wraith])
    elif area == 5:
        return random.choice([fire_lizard, dragonling, demon])
    elif area == 6:
        return random.choice([corrupted_knight, hydra, demon, death])
    elif area == 7:
        return devil
    else:
        print("Invalid area! Defaulting to area 1...")
        return random.choice([goblin, spider, slime])


def enemy_turn(enemy, player_health):
    move = random.choice(["attack", "special", "miss"])
    if move == "attack":
        print(f"The {enemy.name} attacks!")
        return player_health - enemy.attack
    elif move == "special":
        print(f"The {enemy.name} uses a special attack! It deals double damage!")
        return player_health - (enemy.attack * 2)
    else:
        print(f"The {enemy.name} missed!")
        return player_health


# ==== Battle System ====

def battle(player):
    dot=0
    enemy = spawn_monster(area)
    player_health = player.base_health
    print(f"A wild {enemy.name} appears!")
    turn_count=0
    while True:
        print(f"\nPlayer HP: {player_health} | {enemy.name} HP: {enemy.hp}")
        move = input("1. Light Attack\n2. Heavy Attack (50% hit)\n3. Block\n4. Use item\n> ")
        if move == "1":
            weapon = weapons.get(player.equipped_weapon, None)
            if not weapon:
                print(f"⚠️ Error: Equipped weapon '{player.equipped_weapon}' not found in weapons dict!")
                return

            turn_count+=1
            if weapon:
                match weapon.effect:
                    case "dot":
                        dot += 10
                        print(f"The enemy is poisoned! +{dot} DOT per turn stacking.")
                    case "burn":
                        print("The enemy is burned for 5 damage!")
                        enemy.hp -= 5
                    case "multi_hit":
                        if random.random() < 0.05:
                            print("You strike twice with your Rusty Shiv!")
                            enemy.hp -= weapon.damage
                    case "slow":
                        if random.random() < 0.2:
                            print("Enemy is slowed and loses its next attack!")
                            skip_enemy_turn = True
                    case "echo":
                        if "last_dmg" in globals():
                            echoed = damage // 2
                            print(f"Echoblade deals {echoed} echo damage!")
                            enemy.hp -= echoed
                    case "execute":
                        if enemy.hp < 20:
                            print("Execution triggered! +25 bonus damage!")
                            enemy.hp -= 25
                    case "recoil":
                        print("The Orc Cleaver recoils! You take 5 self-damage.")
                        player.base_health -= 5
                    case "crit":
                        if random.random() < 0.1:
                            print("CRITICAL HIT! Double damage!")
                            enemy.hp -= weapon.damage
                    case "armor_pierce":
                        print("Phantom Edge ignores defenses. Full damage applied.")
                    case "fireburst":
                        if turn_count % 3 == 0:
                            print("SCALDFANG Fireburst explodes! 30 bonus damage.")
                            enemy.hp -= 30
                    case "purge":
                        print("VOIDBREAKER purges enemy buffs! (Effect optional)")
                    case "lifedrain":
                        print("Hellforged Blade drains your health by 5.")
                        player.base_health -= 5
                    case "stacked_poison":
                        dot += 20
                        print("Venom stacks DOUBLE poison! DOT is now", dot)
                    case "lifesteal":
                        print("Soul Reaver restores 10 health.")
                        player.base_health = min(player.health, player.base_health + 10)
                    case "doom":
                        if random.random() < 0.05:
                            print("The VOID PRINCE BLADE casts Doom! Enemy dies instantly!")
                            enemy.hp = 0
                    
            enemy.hp -= weapon.damage + dot
        elif move == "2":
            if random.random() < 0.5:
                print("You missed!")
            else:
                damage = player.attack + 10
                enemy.hp -= damage
        elif move == "3":
            print("You brace for the next attack.")
            blocking = True
        elif move == "4":
            usable_items = battle_items(player.inventory)
            if not usable_items:
                print("You have no usable items.")
                continue
            print("Available items:", usable_items)
            choice = input("Which item do you want to use? ").upper()
            if choice in usable_items:
                player.use_item(choice)
                player_health = player.base_health
            else:
                print("Invalid choice.")
                continue

        else:
            print("Invalid input.")
            continue

        if enemy.hp <= 0:
            print(f"You defeated the {enemy.name}!")
            print(f"You got a {enemy.drop}!")
            player.inventory.append(enemy.drop)
            return

        player_health = enemy_turn(enemy, player_health)

        if player_health <= 0:
            print("You were defeated...")
            return


# ==== Inventory Menu ====
def inventory_menu(player):
    global equipped_weapon,equipped_armor
    print("Inventory:")
    print_inv(player.inventory)

    print(f"Equipped Weapon: {player.equipped_weapon} Attack: {player.attack}, Equipped Armor: {player.equipped_armor} Health: {player.health}")
    gear_items = list(set(item for item in player.inventory if item in weapons or item in items_armor))
    if gear_items:
        print("Equippable gear:", gear_items)
        choice2=input("Equip item? \n1. Yes\n2. No\nEnter: ")
        if choice2=="1":
            choice = input("Enter item to equip: ").upper()
            if choice in gear_items:
                # Return old gear to inventory
                if choice in items_armor and player.equipped_armor:
                    player.inventory.append(player.equipped_armor)
                if choice in weapons and player.equipped_weapon:
                    player.inventory.append(player.equipped_weapon)

                player.equip(choice)
                player.inventory.remove(choice)

            else:
                print("Invalid item.")
        else:
            return

def shop(player):
    global area
    print("\n--- 🛒 WELCOME TO THE SHOP 🛒 ---")
    print(f"You have {player.gold} gold.\n")
        # === BUY TRAVEL PASS TO NEXT AREA ===
    if area < 7:
        print(f"\n🚪 Travel Pass to Area {area + 1} — 100 gold")
        pass_buy = input("Would you like to buy a Travel Pass? (yes/no): ").lower()
        if pass_buy == "yes":
            if player.gold >= 100:
                player.gold -= 100
                area += 1
                print(f"✅ You unlocked Area {area}!")
            else:
                print("❌ Not enough gold.")
    else:
        print("\n🌟 You are already in the final area!")

    # === SELL DROPS ===
    sellables = {}
    for item in player.inventory:
        if item in items_drops:
            sellables[item] = sellables.get(item, 0) + 1

    if sellables:
        print("You have the following sellable drops:")
        for item, count in sellables.items():
            price = items_drops[item]
            print(f"{item} x{count} — worth {price} gold each")
        
        sell_choice = input("\nWould you like to sell anything? (yes/no/sell all): ").lower()
        
        if sell_choice == "sell all":
            total_gold = 0
            for item, count in sellables.items():
                gold_earned = count * items_drops[item]
                total_gold += gold_earned
                for _ in range(count):
                    player.inventory.remove(item)
            player.gold += total_gold
            print(f"💰 Sold all drops for {total_gold} gold.")
        elif sell_choice == "yes":
            item_to_sell = input("Enter item name to sell: ").upper()
            if item_to_sell in sellables:
                try:
                    amount = int(input(f"How many {item_to_sell}s do you want to sell? "))
                    if amount > sellables[item_to_sell]:
                        print("You don't have that many!")
                    else:
                        total = amount * items_drops[item_to_sell]
                        player.gold += total
                        for _ in range(amount):
                            player.inventory.remove(item_to_sell)
                        print(f"Sold {amount} {item_to_sell}(s) for {total} gold.")
                except ValueError:
                    print("Invalid amount.")
            else:
                print("You don't have that item.")
        else:
            print("You chose not to sell anything.")
    else:
        print("You have no monster drops to sell.")

    # === BUY ARMOR ===
    print("\nAvailable Armor:")
    for name, stats in shop_armor.items():
        owned = "✅" if name in player.inventory or player.equipped_armor == name else ""
        print(f"{name}: {stats['defense']} DEF — {stats['price']} gold {owned}")

    choice = input("\nEnter armor name to buy (or 'exit'): ").upper()
    if choice == "EXIT":
        return
    
    if choice in shop_armor:
        cost = shop_armor[choice]["price"]
        defense = shop_armor[choice]["defense"]

        if player.gold < cost:
            print("You don't have enough gold.")
            return

        player.gold -= cost

        # Refund old equipped armor
        if player.equipped_armor:
            print(f"You unequipped {player.equipped_armor} and put it in your inventory.")
            player.inventory.append(player.equipped_armor)

        # Equip new armor
        player.equip(choice)
        print(f"You bought and equipped {choice}!")
    else:
        print("Invalid item.")



# ==== Main Game Loop ====
def main():
    running = True
    player = Player()
    while running:
        if "DEMONIC KEY" in player.inventory:
            print("YOU WON!!")
            print("Project made by Hazel :)")
            running = False
            return
        choice = input("\nChoose an action:\n1. Battle\n2. Inventory\n3. Quit\n4. Shop\n> ")
        
        if choice == "1":
            battle(player)
        elif choice == "2":
            inventory_menu(player)
        elif choice == "3":
            print("Thanks for playing!")
            break
        elif choice == "4":
            shop(player)
        else:
            print("Invalid choice.")


main()
