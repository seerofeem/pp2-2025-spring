import json

file_path = "C:/Users/Arsen/Desktop/pp2/lab4/sample-data.json"


with open(file_path, "r") as file:
    data = json.load(file)

interface_data = data["imdata"]

output = []
output.append("Interface Status")
output.append("=" * 80)
output.append(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
output.append("-" * 80)

for entry in interface_data:
    attributes = entry["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "" 
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    output.append(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")

formatted_output = "\n".join(output)
print(formatted_output)
