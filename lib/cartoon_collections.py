def roll_call_dwarves(arr):
    for index,dwarf in enumerate(arr, start=1):
        print(f'{index}. {dwarf}')
dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarves)

def summon_captain_planet(arr):
    return [call.capitalize() + '!' for call in arr]

def long_planeteer_calls(arr):
    for planeteer in arr:
        if len(planeteer) > 4:
            return True
    return False

def find_the_cheese(arr):
    cheeses = ["cheddar", "gouda","camembert"]
    for cheese in cheeses:
        if cheese in arr:
            return cheese
    return None
 
snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks))
#=> "gouda"

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
print(find_the_cheese(soup))
#=> "cheddar"   

ingredients = ["garlic", "rosemary", "bread"]
print(find_the_cheese(ingredients))
#=> None    
