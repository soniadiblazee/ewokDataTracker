ewok_data = {
    "name": "richard benson",
    "age": 67,
    "weapon": "spear",
 "rank": "warrior"
}

print("ewok name:", ewok_data["name"])
print("ewok age:", ewok_data["age"])
print("ewok weapon:", ewok_data["weapon"])
print("ewok Rank:", ewok_data["rank"])

ewok_data["weapon"] = "boww and arrow"  # update weapon, update rank, add new homeworld attribute
ewok_data["rank"] = "chief" 
ewok_data["homeworld"] = "endor"
print("\nUpdated Ewok Data:")
for key, value in ewok_data.items():
    print(f"{key}: {value}")

ewok_tribe = {
    "richard benson": ewok_data,
    "Chief Chirpa": {
        "name": "chief chirpa",
        "age": 30,
        "weapon": "staff",
        "rank": "chief",
        "homeworld": "endor"
    }
}

print("\newok tribe data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\newok: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")