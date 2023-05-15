import fileinput
import webbrowser
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
name_of_equipment_game_name = name_of_equipment_user_name.replace(' ','_').lower()

gfx_key = name_of_equipment_game_name+'_icon'

print("Does this have a variant type, type 1 for yes, 2 for no")
correct_input = False
while correct_input == False:
    is_it_variant = input()
    is_it_variant = int(is_it_variant)
    if is_it_variant == 1 or is_it_variant == 2:
        correct_input = True
    else :
        print("Incorrect Input")

print("Republic or Imperial? 1 for Republic 2 for Imperial")
correct_input = False
while correct_input == False:
    imperial_or_republic = input()
    imperial_or_republic = int(imperial_or_republic)
    if imperial_or_republic == 1 or imperial_or_republic == 2:
        correct_input = True
    else :
        print("Incorrect Input")
### WRITING PRODUCTION SHIP CODE ###
if type_of_ship == 1:
    for line in fileinput.input('00_scripted_localisation_market.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###AAA###'):
            print('	text = {\n		trigger = {\n			light_ship_production_array = '+str(price_of_equipment)+'\n		}\n		localization_key = '+gfx_key+' \n	}') 
            print("	###AAA###")
        elif line.startswith('	###AAB###'):
            print("	text = {\n		trigger = {\n			light_ship_production_array = "+str(price_of_equipment)+"\n		}\n		localization_key = \""+name_of_equipment_game_name+"\" \n	}")
            print("	###AAB###")
        elif line.startswith('	###AAC###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+str(price_of_equipment)+"}\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###ABB###")
        else:
            print(line, end ="")
elif type_of_ship == 2:
    for line in fileinput.input('00_scripted_localisation_market.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###BBB###'):
            print("	text = {\n		trigger = {\n			medium_ship_production_array = "+str(price_of_equipment)+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###BBB###")
        elif line.startswith('	###BBC###'):
            print("	text = {\n		trigger = {\n			medium_ship_production_array = "+str(price_of_equipment)+"\n		}\n		localization_key = \""+name_of_equipment_game_name+"\" \n	}")
            print("	###BBC###")
        elif line.startswith('	###BCC###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+str(price_of_equipment)+"}\n		}\n		localization_key = \""+name_of_equipment_game_name+"\" \n	}")
            print("	###BCC###")
        else:
            print(line, end ="")
elif type_of_ship == 3:
    for line in fileinput.input('00_scripted_localisation_market.txt', inplace=1): #common\scripted_localisation\00_scripted_localisation_market.txt
        if line.startswith('	###CCC###'):
            print("	text = {\n		trigger = {\n			heavy_ship_production_array = "+str(price_of_equipment)+"\n		}\n		localization_key = \""+gfx_key+"\" \n	}")
            print("	###CCC###")
        elif line.startswith('	###CCD###'):
            print("	text = {\n		trigger = {\n			heavy_ship_production_array = "+str(price_of_equipment)+"\n		}\n		localization_key = \""+name_of_equipment_game_name+"\" \n	}")
            print("	###CCD###")
        elif line.startswith('	###CDD###'):
            print("	text = {\n		trigger = {\n			check_variable = {selected_ship_production_cost = "+str(price_of_equipment)+"}\n		}\n		localization_key = \""+name_of_equipment_game_name+"\" \n	}")
            print("	###CDD###")
        else:
            print(line, end ="")
fileinput.close()
#### WRITING BUYING MARKET CODE ###
if imperial_or_republic == 1:
    if classifaction == 1:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAA###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###AAA###")
            else:
                print(line, end ="")
    elif classifaction == 2:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###BBB###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###BBB###")
            else:
                print(line, end ="")
    elif classifaction == 3:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###CCC###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###CCC###")
            else:
                print(line, end ="")
    elif classifaction == 4:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###DDD###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###DDD###")
            else:
                print(line, end ="")
elif imperial_or_republic == 2:
    if classifaction == 1:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAB###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###AAB###")
            else:
                print(line, end ="")
    elif classifaction == 2:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###BBC###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###BBC###")
            else:
                print(line, end ="")
    elif classifaction == 3:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###CCD###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###CCD###")
            else:
                print(line, end ="")
    elif classifaction == 4:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###DDE###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###DDE###")
            else:
                print(line, end ="")
elif imperial_or_republic == 3:
    if classifaction == 1:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###ABB###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###ABB###")
            else:
                print(line, end ="")
    elif classifaction == 2:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###BCC###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###BCC###")
            else:
                print(line, end ="")
    elif classifaction == 3:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###CDD###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###CDD###")
            else:
                print(line, end ="")
    elif classifaction == 4:
        for line in fileinput.input('buying_market.gui', inplace=1): #interface\buying_market.gui
            if line.startswith('		###DEE###'):
                print('''
            iconType = {
                name = "product_background_box_'''+str(price_of_equipment)+'''"
                spriteType = "GFX_market_product_background_box"
                position = { x = 120 y = 120 }
                orientation = UPPER_LEFT
            }
            instantTextBoxType = {
                name = "product_name_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_name"
            }
            iconType = {
                name = "product_image_display_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "'''+gfx_key+'''"
            }
            instantTextBoxType = {
                name = "product_quantity_'''+str(price_of_equipment)+'''"
                position = {x = 0 y = 0}
                text = "'''+str(price_of_equipment)+'''_marketplace_quantity"
            }
            buttonType = {
                name = "product_buy_one_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_buy_one_button"
            }
            buttonType = {
                name = "product_auto_buy_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_auto_buy_button"
            }''')
                if is_it_variant == 1:
                    print('''            buttonType = {
                name = "product_variant_type_'''+str(price_of_equipment)+'''"
                position = { x = 530 y = 488 }
                spriteType = "GFX_market_variant_button"
            }''')
                print("		###DEE###")
            else:
                print(line, end ="")               
fileinput.close()
if imperial_or_republic == 1:
    if classifaction == 1:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAA###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###AAA###")
            else:
                print(line, end ="")
    elif classifaction == 2:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###BBB###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###BBB###")
            else:
                print(line, end ="")
    elif classifaction == 3:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###CCC###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###CCC###")
            else:
                print(line, end ="")
    elif classifaction == 4:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###DDD###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###DDD###")
            else:
                print(line, end ="")
elif imperial_or_republic == 2:
    if classifaction == 1:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###AAB###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###AAB###")
            else:
                print(line, end ="")
    elif classifaction == 2:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###BBC###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###BBC###")
            else:
                print(line, end ="")
    elif classifaction == 3:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###CCD###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###CCD###")
            else:
                print(line, end ="")
    elif classifaction == 4:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###DDE###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###DDE###")
            else:
                print(line, end ="")
elif imperial_or_republic == 3:
    if classifaction == 1:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###ABB###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###ABB###")
            else:
                print(line, end ="")
    elif classifaction == 2:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###BCC###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###BCC###")
            else:
                print(line, end ="")
    elif classifaction == 3:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###CDD###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###CDD###")
            else:
                print(line, end ="")
    elif classifaction == 4:
        for line in fileinput.input('buying_market.txt', inplace=1): #interface\buying_market.gui
            if line.startswith('		###DEE###'):
                print('''		product_buy_one_'''+str(price_of_equipment)+''' = {
			if = {
				limit = {
					check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
				}
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
		}
		product_auto_buy_'''+str(price_of_equipment)+''' = {
			set_country_flag = "'''+str(price_of_equipment)+'''_auto_buy_enabled"
		}''')
                if is_it_variant == 1:
                    print('''		product_variant_type_'''+str(price_of_equipment)+''' = {
            if = {
                limit = {
                    check_variable = {global.market_ship_holder@'''+str(price_of_equipment)+''' > 0}
                }
                if = {
                    limit = {
                        NOT = {
                            has_country_flag = brought_out
                        }
                    }
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = EMP
                    }
                }else = {
                    create_ship = {
                        type = '''+name_of_equipment_game_name+'''_variant
                        equipment_variant = "'''+name_of_equipment_user_name+'''"
                        creator = var:global.'''+name_of_equipment_game_name+'''_holder
                    }
                }
            }
        }''')
                print("		###DEE###")
            else:
                print(line, end ="")
fileinput.close()

f = open("test.gfx", "a")
f.write('\n	spriteType = {\n		name = \''+gfx_key+'\'		texturefile = ""	\n	}')
f.close()
f = open("localisation.yml", "a")
f.write('\n'+str(price_of_equipment)+'_marketplace_quantity:0 "[global.market_ship_holder@'+str(price_of_equipment)+']"\n'+str(price_of_equipment)+'_marketplace_name:0 "'+name_of_equipment_user_name+'"')
f.write('\n'+name_of_equipment_game_name+'_unit:0 ""\n'+name_of_equipment_game_name+'_unit_desc:0 ""')
f.write('\n'+name_of_equipment_game_name+':0 ""\n'+name_of_equipment_game_name+'_desc:0 ""\n'+name_of_equipment_game_name+'_short:0 ""')
f.close()
#input("The program has completed all of its tasks, it will now open the files you will need to edit manually with your native text editor, press enter to acknowledge this")
#webbrowser.open("test.gfx") ## GFX SPRITE