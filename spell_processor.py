'''                                              SPELL PROCESSOR                                                     '''
''' This file takes spells from spells.txt and spell names from spell_list.txt and splits them into individual spells'''

''' IMPORTS '''
import re

''' SPELLS CLASS '''

class SpellList:
    def __init__(self, name):
        self.name = name
        self.spells = []
        self.spell_list = []
        self.spell_levels = ["cantrip"] + [str(i) for i in range(1,10)]
        self.classes = []
        self.components = ["V","S","M",[]]
        self.range = []
        self.duration = []
        self.casting_time = []
        self.school = []
        self.ritual = [True, False]
        self.desc_dict = {}
        self.class_dict = {}
        self.level_dict = {}


    def readIn(self, spells_file, spell_list_file):
        self.spells = [line.strip() for line in open(spells_file)]
        self.spell_list = [line.strip() for line in open(spell_list_file)]

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

        self.desc_dict = {name:"\n".join(desc[7:]) for name,desc in list(zip(self.spell_list,self.spells))}

        classes = [line.strip() for line in open(spell_list_file)]
        classes = " ".join([" ".join(c.split(", ")) for c in classes])
        classes = list(set(classes.split(" ")))
        self.classes = classes


spells = SpellList("spells")
spells.readIn("spells.txt", "spell_list.txt")

print(spells.classes)