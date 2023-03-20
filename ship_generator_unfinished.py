import fileinput
from webbrowser import open as text_opener
### CORVETTE = 0 - 2000 PRODUCTION UNITS, FRIGATE 2001 - 4500, CRUISER 4501 - 8000, STAR DESTROYER, 8000 - ONWARDS
### CORVETTE, 3000 COST FRIGATES ARE LIGHT, over 3000 frigates and 6000 cost cruisers medium, star destroyers and other cruisers heavy
LIGHT_MAX_COST = 3000
MEDIUM_MAX_COST = 6000  
CORVETTE_MAX_COST = 2000
FRIGATE_MAX_COST = 4500
CRUISER_MAX_COST = 8000
#### This for setting interface files apart
MARKET_INITAL_POSITIONING = 0
MARKET_DIFFERENCE_IN_DISTENCE_X_VALUE = 0
MARKET_DIFFERENCE_IN_DISTENCE_Y_VALUE = 0




print("This is a python script for adding a new item to the ship market, run from the main file of the mod (where common, interface folders reside), firstly what is the production cost of the ship, this needs to be unique but will be checked by this script")
correct_input = False
while correct_input == False:
    price_of_equipment = input()
    price_of_equipment = int(price_of_equipment)
    if price_of_equipment > 0:
        correct_input = True
    else :
        print("Incorrect Input")
if price_of_equipment <= CORVETTE_MAX_COST:
    classifaction = 1
elif price_of_equipment <= FRIGATE_MAX_COST:
    classifaction = 2
elif price_of_equipment <= CRUISER_MAX_COST:
    classifaction = 3
else:
    classifaction = 4

if price_of_equipment <= LIGHT_MAX_COST:
    type_of_ship = 1
elif price_of_equipment <= MEDIUM_MAX_COST:
    type_of_ship = 2
else:
    type_of_ship = 3
print("Now what is the ship name, this is the user presented name and the name for equipment and technology. Uses spaces, underscore _ is added automatically where spaces are used")
name_of_equipment_user_name = input()
name_of_equipment_game_name = name_of_equipment_user_name.replace(' ','_')

print("Now what is the gfx key you want it to be (i.e. GFX_ship_1_destroyer). you will manually have to input the location of the ship gfx in corporation.gfx file, the new gfx text will be at the end of the file")
gfx_key = input()

print("Does this have a variant type, type 1 for yes, 2 for no")
correct_input = False
while correct_input == False:
    is_it_variant = input()
    if is_it_variant == "1" or is_it_variant == "2":
        correct_input = True
    else :
        print("Incorrect Input")

print("Republic or Imperial? 1 for Republic 2 for Imperial")
correct_input = False
while correct_input == False:
    imperial_or_republic = input()
    if imperial_or_republic == "1" or imperial_or_republic == "2":
        correct_input = True
    else :
        print("Incorrect Input")
### WRITING PRODUCTION SHIP CODE ###
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
        if line.startswith('	###BBB###'):
            print("	text = {\n		trigger = {\n			medium_ship_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###BBB###")
        elif line.startswith('	###BBC###'):
            print("	text = {\n		trigger = {\n			medium_ship_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###BBC###")
        elif line.startswith('	###BCC###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+price_of_equipment+"}\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###BCC###")
        else:
            print(line, end ="")
elif type_of_ship == 3:
    for line in fileinput.input('test.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###CCC###'):
            print("	text = {\n		trigger = {\n			heavy_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###CCC###")
        elif line.startswith('	###CCD###'):
            print("	text = {\n		trigger = {\n			heavy_production_array = "+price_of_equipment+"\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###CCD###")
        elif line.startswith('	###CDD###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+price_of_equipment+"}\n		}\n		localization_key = \""+name_of_equipment+"\" \n	}")
            print("	###CDD###")
        else:
            print(line, end ="")
#### WRITING BUYING MARKET CODE ###
if imperial_or_republic == 1:
    if classifaction == "1":
        for line in fileinput.input('test.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAA###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("		###AAA###")
            else:
                print(line, end ="")
    elif classifaction == "2":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###BBB###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###BBB###")
            else:
                print(line, end ="")
    elif classifaction == "3":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###CCC###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###CCC###")
            else:
                print(line, end ="")
    elif classifaction == "4":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###DDD###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###DDD###")
            else:
                print(line, end ="")
elif imperial_or_republic == 2:
    if classifaction == "1":
        for line in fileinput.input('test.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAB###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("		###AAB###")
            else:
                print(line, end ="")
    elif classifaction == "2":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###BBC###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###BBC###")
            else:
                print(line, end ="")
    elif classifaction == "3":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###CCD###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###CCD###")
            else:
                print(line, end ="")
    elif classifaction == "4":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###DDE###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###DDE###")
            else:
                print(line, end ="")
elif imperial_or_republic == 3:
    if classifaction == "1":
        for line in fileinput.input('test.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###ABB###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("		###ABB###")
            else:
                print(line, end ="")
    elif classifaction == "2":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###BCC###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###BCC###")
            else:
                print(line, end ="")
    elif classifaction == "3":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###CDD###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###CDD###")
            else:
                print(line, end ="")
    elif classifaction == "4":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###DEE###'):
                print('''
            iconType = {
                name = "product_background_box_'''+price_of_equipment+'''"
                spriteType = "GFX_circle_button"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+price_of_equipment+'''"
                position = {x = 0 y = 0}
                text = "'''+price_of_equipment+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                if is_it_variant == "1":
                    print('''            buttonType = {
                name = "product_variant_type_'''+price_of_equipment+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_circle_button"
            }''')
                print("	###DEE###")
            else:
                print(line, end ="")               
fileinput.close()
if imperial_or_republic == 1:
    if classifaction == "1":
        for line in fileinput.input('test.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAA###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("		###AAA###")
            else:
                print(line, end ="")
    elif classifaction == "2":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###BBB###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###BBB###")
            else:
                print(line, end ="")
    elif classifaction == "3":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###CCC###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###CCC###")
            else:
                print(line, end ="")
    elif classifaction == "4":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###DDD###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###DDD###")
            else:
                print(line, end ="")
elif imperial_or_republic == 2:
    if classifaction == "1":
        for line in fileinput.input('test.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAB###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("		###AAB###")
            else:
                print(line, end ="")
    elif classifaction == "2":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###BBC###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###BBC###")
            else:
                print(line, end ="")
    elif classifaction == "3":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###CCD###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###CCD###")
            else:
                print(line, end ="")
    elif classifaction == "4":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###DDE###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###DDE###")
            else:
                print(line, end ="")
elif imperial_or_republic == 3:
    if classifaction == "1":
        for line in fileinput.input('test.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###ABB###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("		###ABB###")
            else:
                print(line, end ="")
    elif classifaction == "2":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###BCC###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###BCC###")
            else:
                print(line, end ="")
    elif classifaction == "3":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###CDD###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###CDD###")
            else:
                print(line, end ="")
    elif classifaction == "4":
        for line in fileinput.input('test.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('	###DEE###'):
                print('''		buy_one_'''+price_of_equipment+'''_product_number = {
			if = {
				limit = {
					NOT = {
						has_tech = '''+name_of_equipment_game_name+'''_tech
					}
					check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
				}
				set_technology = {
					'''+name_of_equipment_game_name+'''_tech = 1
				}
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}else = {
				add_equipment_production = {
					equipment = {
						type = '''+name_of_equipment_game_name+'''_1
					}
					requested_factories = 1
					progress = 1.00
					amount = 1
				}
			}
		}
		auto_buy_'''+price_of_equipment+'''_product_number = {
			set_country_flag = "'''+price_of_equipment+'''_auto_buy_enabled
		}''')
            if is_it_variant == 1:
                print('''		buy_as_variant_product_number = {
                    if = {
                        limit = {
                            NOT = {
                                has_tech = '''+name_of_equipment_game_name+'''_tech
                            }
                            check_variable = {global.market_ship_holder@'''+price_of_equipment+''' > 0}
                        }
                        set_technology = {
                            '''+name_of_equipment_game_name+'''_variant_tech = 1
                        }
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }else = {
                        add_equipment_production = {
                            equipment = {
                                type = '''+name_of_equipment_game_name+'''_1_variant
                            }
                            requested_factories = 1
                            progress = 1.00
                            amount = 1
                        }
                    }
                }''')
                print("	###DEE###")
            else:
                print(line, end ="")
fileinput.close()

f = open("test.gfx", "a")
f.write("	spriteType = {\n		name = \""+gfx_key+"\"		texturefile = ""	}")
f.close()

input("The program has completed all of its tasks, it will now open the files you will need to edit manually with your native text editor, press enter to acknowledge this")
text_opener.open("test.gfx") ## GFX SPRITE