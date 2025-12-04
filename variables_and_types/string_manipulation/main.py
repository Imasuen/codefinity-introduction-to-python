grocery_items = "milk cheese bread apples oranges chicken"

# 1) Assign slices directly, don’t wrap in print()
dairy1  = grocery_items[0:4]   # "milk"
dairy2  = grocery_items[5:11]  # "cheese"
bakery1 = grocery_items[12:17] # "bread"

# 2) Concatenate into one sentence
message = (
    "We have dairy : "
    + dairy1 + ", "
    + dairy2 + ", and "
    + bakery1
)
print(message)