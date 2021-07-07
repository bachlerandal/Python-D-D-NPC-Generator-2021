import random

rng = random.SystemRandom()

strength = dexterity = constitution = intelligence = wisdom = charisma = 0
statArray = [0,0,0,0,0,0]
raceArray = []
classArray = []
characterNameArray = []
goldAmount = 0
characterRace = "Unknown"
characterClass = "Unknown"
characterName = "Unknown"
characterGear = "Unknown"


#function for standard 1-6 dice roll
def diceRoll():
    return rng.randint(1,6)



#function to collect 4 dice rolls and drop lowest value. Returns best 3 rolls of 4.
def bestOfFour():
    allRolls = [0,0,0,0]
    rollTotal = 0

    for x in range(len(allRolls)):
        allRolls[x] = diceRoll()
        rollTotal += allRolls[x]

    rollTotal -= min(allRolls)

    return rollTotal



#function to place generated stat rolls into array
def statAssignment():
    for x in range(len(statArray)):
        statArray[x] = bestOfFour()

    #re-rolls stats if roll values are too low
    if(max(statArray)) <= 13:
        statAssignment()



#function to open file and read lines into array
def readFromFile(x):
    fileObj = open(x, "r")
    fileArray = fileObj.read().splitlines()
    fileObj.close()
    return fileArray


#function to open file and write lines to it
def writeToFile(x):
    fileObj = open("NPCGeneratorOutput.txt", "a")
    fileObj.write(x)
    fileObj.write("\n")
    fileObj.close()


#function to make adjustments to stats based on race
def racialStatAdjustment(x):
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma

    if(x == "Dwarf"):
        constitution += 2
        charisma -= 2
    if(x == "Elf"):
        dexterity += 2
        constitution -= 2
    if(x == "Gnome"):
        constitution += 2
        strength -= 2
    if(x == "Half-Orc"):
        strength += 2
        intelligence -= 2
        charisma -= 2
    if(x == "Halfling"):
        dexterity += 2
        strength -= 2



#function to calculate NPC gold amount
def goldAmountFunction():
    return rng.randint(1, 100)



#function opens specific name file to read in character names based on race and returns all file contents as array
def characterName(characterRace):
    if(characterRace == "Elf"):
        characterNameArray = readFromFile("ElfNames.txt")
    if(characterRace == "Dwarf"):
        characterNameArray = readFromFile("DwarfNames.txt")
    if(characterRace == "Gnome"):
        characterNameArray = readFromFile("GnomeNames.txt")
    if(characterRace == "Half-Orc"):
        characterNameArray = readFromFile("HalfOrcNames.txt")
    if(characterRace == "Halfling"):
        characterNameArray = readFromFile("HalflingNames.txt")
    if(characterRace == "Half-Elf"):
        characterNameArray = readFromFile("HalfElfNames.txt")
    if(characterRace == "Human"):
        characterNameArray = readFromFile("HumanNames.txt")
        
    return characterNameArray



#Function for generating equipment for the NPC based on class
def characterEquipment(characterClass):
    characterGearArray = []
    if(characterClass == "Fighter" or characterClass == "Ranger"):
        characterGearArray = readFromFile("FighterRangerGear.txt")
    elif(characterClass == "Rogue"):
        characterGearArray = readFromFile("RogueGear.txt")
    elif(characterClass == "Monk"):
        characterGearArray = readFromFile("MonkGear.txt")
    elif(characterClass == "Barbarian"):
        characterGearArray = readFromFile("BarbarianGear.txt")
    elif(characterClass == "Wizard" or characterClass == "Sorcerer" or characterClass == "Warlock"):
        characterGearArray = readFromFile("CasterGear.txt")
    elif(characterClass == "Cleric" or characterClass == "Paladin"):
        characterGearArray = readFromFile("HolyGear.txt")
    elif(characterClass == "Bard"):
        characterGearArray = readFromFile("BardGear.txt")
    else:
        characterGearArray = readFromFile("FighterRangerGear.txt")
    
    characterGear = random.choice(characterGearArray)

    return characterGear



###############################################################################################
# Main Method #
###############################################################################################
raceArray = readFromFile("Races.txt")
characterRace = random.choice(raceArray)
characterNameArray = characterName(characterRace)
characterName = random.choice(characterNameArray)
print("\nCharacter Name: ", characterName)
print("\nCharacter Race: ", characterRace)
classArray = readFromFile("Classes.txt")
characterClass = random.choice(classArray)
print("Character Class: ", characterClass, "\n")
goldAmount = goldAmountFunction()
print("Character Gold: ", goldAmount)
characterGear = characterEquipment(characterClass)
print("Character Equipment: ", characterGear)


statAssignment()
strength = statArray[0]
dexterity = statArray[1]
constitution = statArray[2]
intelligence = statArray[3]
wisdom = statArray[4]
charisma = statArray[5]

racialStatAdjustment(characterRace)

print("\nCharacter Stats \n---------------")
print('Str', strength)
print('Dex', dexterity)
print('Con', constitution)
print('Int', intelligence)
print('Wis', wisdom)
print('Cha', charisma, '\n')

#writeToFile("Character Name: ")
writeToFile(characterName)
writeToFile("Character Race: ")
writeToFile(characterRace)
writeToFile("Character Class: ")
writeToFile(characterClass)
writeToFile("Character Gear: ")
writeToFile(characterGear)
writeToFile("Character Gold: ")
#writeToFile(goldAmount)
writeToFile("\n")


input('Press ENTER to exit')
