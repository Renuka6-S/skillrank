import json

# Step 1: Write Example 5 JSON to ex5.json
example_5_json = {
  "id": "0005",
  "type": "donut",
  "name": "Old Fashioned",
  "ppu": 0.55,
  "batters": {
    "batter": [
      { "id": "1001", "type": "Regular" },
      { "id": "1002", "type": "Chocolate" },
      { "id": "1003", "type": "Blueberry" },
      { "id": "1004", "type": "Devil's Food" }
    ]
  },
  "topping": [
    { "id": "5001", "type": "None" },
    { "id": "5002", "type": "Glazed" },
    { "id": "5005", "type": "Sugar" },
    { "id": "5007", "type": "Powdered Sugar" },
    { "id": "5006", "type": "Chocolate with Sprinkles" },
    { "id": "5003", "type": "Chocolate" },
    { "id": "5004", "type": "Maple" }
  ]
}

with open('ex5.json', 'w') as file:
    json.dump(example_5_json, file, indent=2)

# Step 2: Read the JSON from ex5.json and store it in a dictionary named ex5
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Step 3: Add a new batter named "Tea" for the donut with the name "Old Fashioned"
new_batter = {"id": "1005", "type": "Tea"}
ex5["batters"]["batter"].append(new_batter)

# Step 4: Update the ex5.json file with the modified dictionary
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=2)

print("ex5.json file updated successfully.")
