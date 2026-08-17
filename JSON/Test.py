# Import json
import json

# Create a JSON string
x = {
"Name" : "Emily",
"Age" : 30
}

# Parse the JSON string
y = json.loads(x)

# Print the age
print(x["Age"])