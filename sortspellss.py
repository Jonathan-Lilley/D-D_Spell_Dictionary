spell_list = [line.strip() for line in open("spell_list.txt")]
spells = [line.strip() for line in open("spells.txt")]

spells_temp = []
templines = []
for line in spells:
    if line not in spell_list:
        templines.append(line)
    else:
        spells_temp.append(templines)
        templines = []
        templines.append(line)
spells = sorted(spells_temp[1:])

spells = "\n".join(["\n".join(spell) for spell in spells])

f = open("spells.txt","w")
f.write(spells)
f.close()