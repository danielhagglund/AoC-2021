input_data = open("./course.txt").read().splitlines()

course_steps = []
final_course = {"horizontal": 0, "depth": 0}

for line in input_data:
    step = line.split(' ')
    course_steps.append({"direction": step[0], "distance": int(step[1]) })

for step in course_steps:
    if step["direction"] == "down":
        final_course["depth"] = final_course["depth"] + step["distance"]
    elif step["direction"] == "forward":
        final_course["horizontal"] = final_course["horizontal"] + step["distance"]
    elif step["direction"] == "up":
        final_course["depth"] = final_course["depth"] - step["distance"]
    

print(f"Total horizontal: {final_course['horizontal']}, total depth: {final_course['depth']}")
print("Product:", final_course["depth"]*final_course["horizontal"])
