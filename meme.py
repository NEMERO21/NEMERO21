import json

# Load existing meme data from the JSON file
with open("data/data.json", encoding="utf-8") as file:
    data = json.load(file)

# Gather information about the new meme
title = input("What is the title of the meme: ")
url = input("What is the URL of the meme? NOTE: Add ./ if it is a local file: ")

hashtags = ["#programming", "#programminghumor", "#programmingmemes"]

while True:
    hashtag = input("Enter hashtag (press 'q' to quit): ")
    if hashtag.lower() == 'q':
        break
    hashtags.append(hashtag)

# Append the new meme data to the existing JSON data
data.append({
    "title": title,
    "url": url,
    "twitter_hashtags": hashtags
})

# Write the updated meme data back to the JSON file
with open("data/data.json", 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
