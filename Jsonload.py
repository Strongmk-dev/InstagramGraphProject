from collections import Counter
import pandas
import json
import matplotlib.pyplot as plt
import numpy as np

hashtag_string = '''
{
    "Posts": [
    {
        "Link to post": "https://www.instagram.com/p/CShY8AIK5xy/?utm_source=ig_web_copy_link",
        "Post caption": "Please Enjoy These Pictures Of Bonnie To Pad Out My Instagram Page #Cute #Dog",
        "Media Type": "IMAGE"
    },
    {
        "Link to post": "https://www.instagram.com/p/CSha7qLq8C4/?utm_source=ig_web_copy_link",
        "Post caption": "When your dice have more personality than you. #DnD #ToooCoool",
        "Media Type": "IMAGE"
        
    },
    {
        "Link to post": "https://www.instagram.com/p/B1EQK0sAVyg/?utm_source=ig_web_copy_link",
        "Post caption": "The Loxwood Joust was pretty fun. #DnD #Vibin",
        "Media Type": "VIDEO"
    },
    {
        "Link to post": "https://www.instagram.com/p/CAV-uFyhIqK/?utm_source=ig_web_copy_link",
        "Post caption": "Maybe a bit too hyped to be back, been watching nothing but DnD TikToks all day... #DnD #Nostalgia",
        "Media Type": "IMAGE"
    }
    ]
}
'''


def extract_hashtags(text):
    hashtag_list2 = []
    for word in text.split():
        if word[0] == "#":
            hashtag_list2.append(word[1:])
    return hashtag_list2


data = json.loads(hashtag_string)  # Takes json file and loads it into dict variable
f = open('D:/PhyCharm/InstagramProject/Hashtags.json')
data = json.load(f)

for posts in data['Posts']:
    print(posts['Post caption'])

captions = []  # defining different list variables
hashtags = []

for posts in data['Posts']:  # separates each post caption into separate list variable. Dict --> List.
    captions.append(posts['Post caption'])

print(captions)

for interface in captions:  # Takes each entry in the captions list, runs it through the extract hashtags function.
    for word in interface.split():
        if word[0] == '#':
            hashtags.append(word[1:])

print(hashtags)

counts = Counter(hashtags)
common = counts.most_common()
labels = [item[0] for item in common]
number = [item[1] for item in common]
nbars = len(common)

plt.bar(np.arange(nbars), number, tick_label=labels)
plt.show()
