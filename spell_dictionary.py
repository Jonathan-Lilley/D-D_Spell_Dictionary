'''                                              SPELL PROCESSOR                                                     '''
'''  This is the main spell processor. It combines everything and sets up the whole dictionary and search methods.   '''

''' IMPORTS '''

''' SPELLS CLASS '''

class SpellList:
    def __init__(self, name):
        # BASE DATA
        self.name = name
        self.spells = []
        self.spell_list = []
        self.spell_levels = ["cantrip"] + [str(i) for i in range(1,10)]
        self.classes = ["bard","cleric","druid","paladin","ranger","sorcerer","warlock","wizard"]
        self.components = ["V","S","M",[]]
        self.range = []
        self.duration = []
        self.casting_time = []
        self.schools = ["abjuration","conjuration","divination","enchantment","evocation","illusion","necromancy",
                       "transmutation"]
        #DICTIONARIES
        self.desc_dict = {} # COMPLETE
        self.spell2class = {} # COMPLETE
        self.class2spell = {} # COMPLETE
        self.spell2level = {} # COMPLETE
        self.level2spell = {} # COMPLETE
        self.spell2school = {} # COMPLETE
        self.school2spell = {} # COMPLETE
        self.spell2ritual = {}
        self.spell2duration = {}
        self.spell2range = {}
        self.spell2components = {}
        self.spell2all = {}

    # Reads in data and processes it into its final format
    def readIn(self, spells_file, spell_list_file):
        self.spells = [line.strip().lower() for line in open(spells_file)]
        self.spell_list = [line.strip().lower() for line in open(spell_list_file)]
        for spell in range(len(self.spells)):
            if " (r" in self.spells[spell]:
                self.spells[spell] = self.spells[spell][:self.spells[spell].index(" (r")]
        for spell in range(len(self.spell_list)):
            if " (r" in self.spell_list[spell]:
                self.spell_list[spell] = self.spell_list[spell][:self.spell_list[spell].index(" (r")]


        # Formatting the spells in order to process them
        spells_temp = []
        templines = []
        for l in range(len(self.spells)):
            line = self.spells[l]
            if line == "divination" and self.spells[l+1] == "divination":
                spells_temp.append(templines)
                templines = []
                templines.append(line)
            elif line not in self.spell_list or line == "divination":
                templines.append(line)
            elif line == "zone of truth":
                spells_temp.append(templines)
                templines = self.spells[l:]
                spells_temp.append(templines)
                break
            else:
                spells_temp.append(templines)
                templines = []
                templines.append(line)
        self.spells = spells_temp[1:]

        # Collects durations


        # Collects casting times


        # Collects ranges


        # Collects material components


        # Creates a dictionary from spell name to spell description
        self.desc_dict = {name:"\n".join(desc[7:]) for name,desc in list(zip(self.spell_list,self.spells))}

        # Creates a dictionary from spell name to classes
        for class_name in self.classes:
            spells = [line.strip().lower() for line in open("spell_lists/"+class_name+".txt")]
            for spell in spells:
                self.spell2class[spell] = self.spell2class.get(spell, []) + [class_name]

        # Creates a dictionary from classes to spell name
        for class_name in self.classes:
            for spell in self.spell2class:
                if class_name in self.spell2class[spell]:
                    self.class2spell[class_name] = self.class2spell.get(class_name, []) + [spell]

        # Creates a dictionary from spell to level
        for spell in range(len(self.spells)):
            self.spell2level[self.spell_list[spell]] = self.spells[spell][2][7:].lower()

        # Creates a dictionary from level to spell
        for level in self.spell_levels:
            for spell in self.spell2level:
                if level in self.spell2level[spell]:
                    self.level2spell[level] = self.level2spell.get(level, []) + [spell]

        # Creates a dictionary from spell name to school
        for spell in range(len(self.spell_list)):
            self.spell2school[self.spell_list[spell]] = self.spells[spell][1].lower()

        # Creates a dictionary from school to spell names
        for school in self.schools:
            for spell in self.spell2school:
                if school in self.spell2school[spell]:
                    self.school2spell[school] = self.school2spell.get(school, []) + [spell]

        # Creates a dictionary from spell name to duration


        # Creates a dictionary from spell name to casting time


        # Creates a dictionary from spell name to range


        # Creates a dictionary from spell name to full info
        for spell in range(len(self.spell_list)):
            self.spell2all[self.spell_list[spell]] = self.spells[spell][1:]



    # INTERFACE

    # Main menu
    def getInfo(self):
        print("Welcome to the D&D spell info dictionary.")
        while True:
            print("Please enter desired information type")
            print("Options: FULL SPELL LIST | SPELL DESCRIPTION | SPELLS BY LEVEL | SPELLS BY CLASS | SPELLS BY SCHOOL"
                  " | FULL SPELL INFO | EXIT")
            INPUT = input().lower()

            if INPUT == "exit":
                break
            elif INPUT == "full spell list":
                for spell in self.spell_list:
                    print(spell)
            elif INPUT == "spell description":
                self.getSpellDesc()
            elif INPUT == "spells by level":
                self.getSpellbyLevel()
            elif INPUT == "spells by class":
                self.getSpellbyClass()
            elif INPUT == "spells by school":
                self.getSpellbySchool()
            elif INPUT == "full spell info":
                self.getSpellInfo()
            else:
                print("That is not an option.")

    # Spells by description menu
    def getSpellDesc(self):
        while True:
            print("Please enter spell or EXIT")
            INPUT = input().lower()
            if INPUT == "exit":
                break
            elif INPUT in self.spell_list:
                print(self.desc_dict[INPUT])
            else:
                print("That is not a spell")

    # Spells by level menu
    def getSpellbyLevel(self):
        while True:
            print("Please enter spell or level or EXIT")
            INPUT = input().lower()
            if INPUT == "exit":
                break
            elif INPUT in "123456789" or INPUT == "cantrip":
                for spell in self.level2spell[INPUT]:
                    print(spell)
            elif INPUT in self.spell_list:
                print(self.spell2level[INPUT])
            else:
                print("That is not an option")

    # Spells by class menu
    def getSpellbyClass(self):
        while True:
            print("Please enter spell or class or EXIT")
            INPUT = input().lower()
            if INPUT == "exit":
                break
            elif INPUT in self.classes:
                for spell in self.class2spell[INPUT]:
                    print(spell)
            elif INPUT in self.spell_list:
                print(self.spell2class[INPUT])
            else:
                print("That is not an option")

    # Spells by school menu
    def getSpellbySchool(self):
        while True:
            print("Please enter spell or school or EXIT")
            INPUT = input().lower()
            if INPUT == "exit":
                break
            elif INPUT in self.schools:
                for spell in self.school2spell[INPUT]:
                    print(spell)
            elif INPUT in self.spell_list:
                print(self.spell2school[INPUT])
            else:
                print("That is not an option")

    # Full info for spell
    def getSpellInfo(self):
        while True:
            print("Please enter spell or EXIT")
            INPUT = input().lower()
            if INPUT == "exit":
                break
            elif INPUT in self.spell_list:
                for line in self.spell2all[INPUT]:
                    print(line)
            else:
                print("That is not an option")


########################################################################################################################
'''                                                  Tests                                                           '''

if __name__ == "__main__":

    spells = SpellList("spells")
    spells.readIn("spell_lists/spells.txt", "spell_lists/spell_list.txt")

    spells.getInfo()