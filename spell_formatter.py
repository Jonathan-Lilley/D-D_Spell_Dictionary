''' SPELL FORMATTER'''
''' Formats spells so they are usable by spell_dictionary.py '''

classes = ["bard","cleric","druid","paladin","ranger","sorcerer","warlock","wizard"]

for c in classes:
    lines = [line.strip()[:line.strip().index(" (")] for line in open("spell_lists/"+c+".txt")
             if line.strip() != "" and line.strip()[0] not in "123456789"]
    lines = "\n".join(lines)
    f = open("spell_lists/"+c+".txt","w")
    f.write(lines)
    f.close()