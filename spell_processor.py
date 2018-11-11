'''                                              SPELL PROCESSOR                                                     '''
'''  This is the main spell processor. It combines everything and sets up the whole dictionary and search methods.   '''

''' IMPORTS '''
from os import listdir

''' SPELLS CLASS '''

class SpellList:
    def __init__(self, name):
        self.name = name
        self.spells = []
        self.spell_list = []
        self.spell_levels = ["cantrip"] + [str(i) for i in range(1,10)]
        self.classes = ["bard","cleric","druid","paladin","ranger","sorcerer","warlock","wizard"]
        self.components = ["V","S","M",[]]
        self.range = []
        self.duration = []
        self.casting_time = []
        self.school = ["abjuration","conjuration","divination","enchantment","evocation","illusion","necromancy",
                       "transmutation"]
        self.ritual = [True, False]
        self.desc_dict = {}
        self.class_dict = {}
        self.level_dict = {}
        self.school_dict = {}
        self.duration_dict = {}
        self.range_dict = {}
        self.components_dict = {}

    # Reads in data and processes it into its final format
    def readIn(self, spells_file, spell_list_file):
        self.spells = [line.strip() for line in open(spells_file)]
        self.spell_list = [line.strip() for line in open(spell_list_file)]

        # Formatting the spells in order to process them
        spells_temp = []
        templines = []
        for line in self.spells:
            if line not in self.spell_list:
                templines.append(line)
            elif line == "Zone of Truth":
                spells_temp.append(templines)
                templines = [self.spells[self.spells.index(line):]]
                spells_temp.append(templines)
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
            spells = [line.strip()[:line.strip().index(" (")] for line in open("spell_lists/"+class_name+".txt") if line.strip() != "" and "Level" not in line.strip()]
            for spell in spells:
                self.class_dict[spell] = self.class_dict.get(spell, []) + [class_name]

        # Creates a dictionary from spell name to duration


        # Creates a dictionary from spell name to casting time


        # Creates a dictionary from spell name to school


        # Creates a dictionary from spell name to range




########################################################################################################################
'''                                                      Tests                                                       '''

if __name__ == "__main__":

    spells = SpellList("spells")
    spells.readIn("spell_lists/spells.txt", "spell_lists/spell_list.txt")

    print(spells.spell_list)