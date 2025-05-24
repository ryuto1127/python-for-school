ONE_TREE_APPLE = 480
APPLE_GRAM = 151
GRAM_KILO = 1000
APPLE_KG_COST = 3.80

def apple_profit(apple_trees):
    return(apple_trees * ONE_TREE_APPLE * APPLE_GRAM / GRAM_KILO * APPLE_KG_COST)
    
print(apple_profit(1))