import fileinput
print("This is a python script for adding a new item to the ship market, run from the main file of the mod (where common, interface folders reside), firstly what is the production cost of the ship, this needs to be unique but will be checked by this script")
price_of_equipment = input()
print("Now what is the ship name, this is the user presented name")
name_of_equipment = input()
print("Now what is the gfx key you want it to be (i.e. GFX_ship_1_destroyer). you will manually have to input the location of the ship gfx in corporation.gfx file, the new gfx text will be at the end of the file")
gfx_key = input()
print("Lastly is this a light ship, medium ship or heavy ship. Type 1 for light, 2 for medium and 3 for heavy.")
correct_input = False
while correct_input == False:
    type_of_ship = input()
    if type_of_ship == 1 or type_of_ship == 2 or type_of_ship == 3:
        correct_input = True
if type_of_ship == 1:
    for line in fileinput.input('test.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###AAA###'):
            print("	text = {\n		trigger = {\n			light_ship_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}") 
            print("	###AAA###")
        elif line.startswith('	###AAB###'):
            print("	text = {\n		trigger = {\n			light_ship_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###AAB###")
        elif line.startswith('	###AAC###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+price_of_equipment+"}\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###ABB###")
        else:
            print(line, end ="")
elif type_of_ship == 2:
    for line in fileinput.input('test.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###AAA###'):
            print("	text = {\n		trigger = {\n			medium_ship_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###BBB###")
        elif line.startswith('	###BBC###'):
            print("	text = {\n		trigger = {\n			medium_ship_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###BBC###")
        elif line.startswith('	###AAC###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+price_of_equipment+"}\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###BCC###")
        else:
            print(line, end ="")
elif type_of_ship == 3:
    for line in fileinput.input('test.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###AAA###'):
            print("	text = {\n		trigger = {\n			heavy_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###CCC###")
        elif line.startswith('	###CCD###'):
            print("	text = {\n		trigger = {\n			heavy_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###CCD###")
        elif line.startswith('	###AAC###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+price_of_equipment+"}\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###CDD###")
        else:
            print(line, end ="")
fileinput.close()
f = open("test.gfx", "a")
f.write("	spriteType = {\n		name = \""+gfx_key+"\"		texturefile = ""	}")

