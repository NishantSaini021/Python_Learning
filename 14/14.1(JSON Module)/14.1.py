# import json

# video = {
#     "name": "Python",
#     "time": "10 min"
# }

# with open("test.json", "w") as file:
#     json.dump(video, file)

# with open("test.json", "r") as file:
#     data = json.load(file)

# print(data)
# print(type(data))


import json

videos = [
    {"name": "Python", "time": "10 min"},
    {"name": "Java", "time": "15 min"}
]

with open("videos.json", "w") as file:
    json.dump(videos, file)

with open("videos.json", "r") as file:
    data = json.load(file)

print(data)
print(type(data))