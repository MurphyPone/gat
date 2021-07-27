#!/usr/bin/env python3
from rich.console import Console
import random
import sys

console = Console(highlight=False)

LOOKUP = {
    "type": {
        "Pistol": {
            "range":    (9,  21),
            "accuracy": (1.9, 2.4),
            "variants": ["Revolver", "Pistol"]
        },
        "Assualt Rifle": {
            "range":    (19, 31),
            "accuracy": (1.2, 1.7),
            "variants": ["DMR", "Automatic AR", "Semi-Automatic AR"]
        },
        "Sub Machine Gun": {
            "range":     (15, 28),
            "accuracy":  (2.5, 3.5),
            "variants": ["Lil Uzi Vertical",]
        },
        "Sniper Rifle": {
            "range":    (60, 100),
            "accuracy": (0.0, 1.0),
            "variants": ["Bolt Action"]
        },
        "Light Machine Gun":  {
            "range":    (27, 35),
            "accuracy": (2.4, 2.8),
            "variants": None
        },
        "Rocket Launcher": {
            "range":    (65, 100),
            "accuracy": (3.8, 4.1),
            "variants": ["Bazooka", "RPG"]
        },
        "Special": {
            "range":    (0,  100),
            "accuracy": (0.0, 5.0), 
            "variants": ["Ballistic Knife", "Sword"]
        },
    },
    "rarity": [ # name, color, dmg dmg_modifier
        # ("Common",          "#fff",     -4, -2),
        # ("Uncommon",        "#aeff51",  -2, -0),
        # ("Unusual",         "#520061",   0, 0), 
        # ("Different",       "#1e91f5",   0, 3), 
        # ("Rare",            "#ee0000",   3, 5), 
        # ("Spectacular",     "#ff6600",   5, 7), 
        # ("Inter Galactic Trans-Dimentional Relic",
        #                     "#646464",   0, 0), 
        ("Common",          "bright_white",     -4, -2),
        ("Uncommon",        "bright_green",     -2, -0),
        ("Unusual",         "purple",           0, 0), 
        ("Different",       "slate_blue1",      0, 3), 
        ("Rare",            "red",              3, 5), 
        ("Spectacular",     "orange1",          5, 7), 
        ("Inter Galactic Trans-Dimentional Relic",
                            "bright_black",            0, 0), 
    ],
    "manufacturer": [
        ("Alien", "The only other known creatures of 'our' universe."),
        ("Imperial", "After the Great War Galactic Imperium established remote governance of Earth and the surrounding colonies"),
        ("Rebellion", "Large opposer of the Imperium, well equiped"),
        ("Elite", "Small group of extremely wealthy researchers who dedicate their surplus towards development of experimental weapons"),
        ("Native", "The less fortunate survivors of the Great War"),
        ("Arch-Tech", "Weapons fueled by the leptonian-anomalous element which appeared after the Great Bomb :tm: was used to end the Great War"),
        ("THE 7", "Other beings not much known about them...")
    ],
}

def show_help():
    gat_width = max([len(key) for key in LOOKUP["type"]])
    res = "[bold]" + "Type".ljust(gat_width) + " Damage" + "\tAccuracy".ljust(9) + "[/bold]\n"
    for key in LOOKUP["type"].keys():
        gat_type = LOOKUP["type"][key]
        dmg_lo, dmg_hi = gat_type['range'][0], gat_type['range'][1]
        acc_lo, acc_hi = gat_type['accuracy'][0], gat_type['accuracy'][1]
        
        res += f"{key.ljust(gat_width)} [{str(dmg_lo).rjust(2)}, {str(dmg_hi).rjust(3)}]\t[{str(acc_lo).rjust(2)}, {str(acc_hi).rjust(2)}]\n"

    rarity_width = len("Inter Galactic Trans-Dimentional Relic")    
    res += "\n[bold]" + "Rarity".ljust(rarity_width) + " Damage Modifier[/bold]\n"
    for t in LOOKUP["rarity"]:
        name = t[0]
        color = t[1]
        mod_lo, mod_hi = t[2], t[3]
        res += f"[{color}]{name.ljust(rarity_width)}[/{color}] [{str(mod_lo).rjust(2)}, {str(mod_hi).rjust(2)}]\n"

    man_width = len("Rebellion")    
    res += "\n[bold]" + "Manufacturer".ljust(rarity_width) + "[/bold]\n"
    for t in LOOKUP["manufacturer"]:
        res += f"{t[0].ljust(man_width)}\t{t[1]}\n"
    

    
    console.print(res)

def get_rarity():
    """returns the name and color tuple of a rarity class"""

    rng = random.randint(0, 10000)
    if rng <= 3500:
        return 0
    elif rng <= 6000:
        return 1
    elif rng <= 8000:
        return 2
    elif rng <= 9000:
        return 3
    elif rng <= 9750:
        return 4
    elif rng <= 9999:
        return 5
    else:
        return 6
    # if rng <= 3500:
    #     rarity = LOOKUP["rarity"][0][0]
    #     color  = LOOKUP["rarity"][0][1]
    # elif rng <= 6000:
    #     rarity = LOOKUP["rarity"][1][0]
    #     color  = LOOKUP["rarity"][1][1]
    # elif rng <= 8000:
    #     rarity = LOOKUP["rarity"][2][0]
    #     color  = LOOKUP["rarity"][2][1]
    # elif rng <= 9000:
    #     rarity = LOOKUP["rarity"][3][0]
    #     color  = LOOKUP["rarity"][3][1]
    # elif rng <= 9750:
    #     rarity = LOOKUP["rarity"][4][0]
    #     color  = LOOKUP["rarity"][4][1]
    # elif rng <= 9999:
    #     rarity = LOOKUP["rarity"][5][0]
    #     color  = LOOKUP["rarity"][5][1]
    # else:
    #     rarity = LOOKUP["rarity"][6][0]
    #     color  = LOOKUP["rarity"][6][1]
    
    # return rarity, color


class Gat():
    def __init__(self):
        # print(LOOKUP["manufacturer"][:6])

        # step 1 calculat rarity as that can influence type 
        gat_rarity_num = get_rarity()

        # if special, assign the hard coded values
        if gat_rarity_num == 6:
            gat_type = "Special"
            gat_dict = LOOKUP["type"]["Special"]
            self.manufacturer = LOOKUP["manufacturer"][6][0]
        else: # just look em up
            gat_type = random.choice(list(LOOKUP["type"].keys())[:6])
            gat_dict = LOOKUP["type"][gat_type]
            self.manufacturer = random.choice(LOOKUP["manufacturer"][:6])[0]
            
        self.type = gat_type
        self.rarity = LOOKUP["rarity"][gat_rarity_num][0]
        self.color = LOOKUP["rarity"][gat_rarity_num][1]

        dmg_lo, dmg_hi = gat_dict['range'][0], gat_dict['range'][1]
        dmg_mid = (dmg_lo + dmg_hi) / 2
        dmg_mod_lo, dmg_mod_hi = LOOKUP["rarity"][gat_rarity_num][2], LOOKUP["rarity"][gat_rarity_num][3]
        
        self.dmg_mod = random.randint(dmg_mod_lo, dmg_mod_hi)
        self.raw_dmg = random.randint(dmg_lo, dmg_hi)
        self.damage = self.raw_dmg + self.dmg_mod
        
        if self.damage < dmg_mid:
            self.roll_quality = "red"
        elif self.damage == dmg_mid:
            self.roll_quality = "bright_yellow"
        else:
            self.roll_quality = "bright_green"

        acc_lo, acc_hi = gat_dict['accuracy'][0], gat_dict['accuracy'][1]

        self.accuracy = random.uniform(acc_lo, acc_hi)
        
        if gat_dict["variants"]:
            self.variant = random.choice(gat_dict["variants"])
        else:
            self.variant = self.type
        

    def verbose(self):
        if self.dmg_mod > 0:
            sign = "+"
        else: 
            sign = ""

        dmg_lo, dmg_hi = LOOKUP["type"][self.type]['range'][0], LOOKUP["type"][self.type]['range'][1]
        width = len("Manufacturer")
        res = f"[bold]{'Rarity:'.ljust(width)}[/bold]\t[{self.color}]{self.rarity}[/{self.color}]\n"
        res += f"[bold]{'Type:'.ljust(width)}[/bold]\t{self.type}\n"
        res += f"[bold]{'Damage:'.ljust(width)}[/bold]\t[{self.roll_quality}]{self.damage} [/{self.roll_quality}]({sign}{self.dmg_mod})\t[{dmg_lo}, {dmg_hi}]\n"
        res += f"[bold]Manufacturer:[/bold]\t{self.manufacturer}\n"

        return res


    def __rich__(self):
        if self.dmg_mod > 0:
            sign = "+"
        else: 
            sign = ""

        return f"[{self.color}]{self.rarity}[/{self.color}] | {self.manufacturer} | {self.variant} | [{self.roll_quality}]{self.damage} [/{self.roll_quality}]({sign}{self.dmg_mod})" 

if __name__ == '__main__':
    if len(sys.argv) < 2:
        console.print(Gat())
    elif sys.argv[1].lower() == "-h":
        show_help()
    elif sys.argv[1].lower() == "-v":
        console.print(Gat().verbose())
    elif sys.argv[1].lower() == "-seven":
        g = Gat()
        while g.type != "Special":
            g = Gat()
        console.print(g)
    elif sys.argv[1].isnumeric():
        for i in range(int(sys.argv[1])):
            console.print(f"{i+1}: {Gat().__rich__()}")
