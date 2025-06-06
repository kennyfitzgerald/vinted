from vinted_api import VintedApi
from send_to_telegram import send_to_telegram, item_to_html
from logging_listings import log_seen_listings, read_seen_listings
import os

# Configuration
search_texts = [
    {
        'search_text': 'carhartt+chase', 
        'catalog_ids':"", 
        'color_ids':"",
        'brand_ids':"", 
        'size_ids':"211", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"", 
        'price_to':"40", 
        'currency':"GBP", 
        'order':"newest_first"
    },
    {
        'search_text': 'Nike+ACG', 
        'catalog_ids':"34", 
        'color_ids':"",
        'brand_ids':"53", 
        'size_ids':"209", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"", 
        'price_to':"60", 
        'currency':"GBP", 
        'order':"newest_first"
    },
    {
        'search_text': 'Bronze+56k', 
        'catalog_ids':"34", 
        'color_ids':"",
        'brand_ids':"", 
        'size_ids':"209", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"3", 
        'price_to':"60", 
        'currency':"GBP", 
        'order':"newest_first"
    },
    {
        'search_text': 'Polar', 
        'catalog_ids':"257", 
        'color_ids':"",
        'brand_ids':"", 
        'size_ids':"209", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"3", 
        'price_to':"80", 
        'currency':"GBP", 
        'order':"newest_first"
    },
    {
        'search_text': 'parra', 
        'catalog_ids':"76", 
        'color_ids':"",
        'brand_ids':"", 
        'size_ids':"210,211", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"3", 
        'price_to':"35", 
        'currency':"GBP", 
        'order':"newest_first"
    },
    {
        'search_text': 'acg', 
        'catalog_ids':"287", 
        'color_ids':"",
        'brand_ids':"", 
        'size_ids':"", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"3", 
        'price_to':"30", 
        'currency':"GBP", 
        'order':"newest_first"
    },
    {
        'search_text': 'stussy birds', 
        'catalog_ids':"76", 
        'color_ids':"",
        'brand_ids':"", 
        'size_ids':"210,211", 
        'material_ids':"",
        'video_game_rating_ids':"", 
        'status_ids':"", 
        'is_for_swap':0,
        'page':1, 
        'per_page':24, 
        'price_from':"3", 
        'price_to':"45", 
        'currency':"GBP", 
        'order':"newest_first"
    }
]

chatID = 5710102700

apiToken = os.environ['API_KEY']

# Initialise Vinted object
Vinted = VintedApi()

# Create empty list for storing results
items = []

# Loop through searches and append results to items list
for search_text in search_texts:
    items = items + Vinted.searchProducts(**search_text)

# Extract relevant data and store in a dictionary
keys = [item['id'] for item in items]
values = [item_to_html(item) for item in items]
item_dict = dict(zip(keys, values))

# Load already seen listings
seen_listings = read_seen_listings()

# Filter out IDs that have already been seen
new_item_dict = { key:value for (key,value) in item_dict.items() if key not in seen_listings}

# Send results to telegram one by one
for item in new_item_dict.values():
    send_to_telegram(item, chatID, apiToken)

# Write seen listings to file 
log_seen_listings(list(new_item_dict.keys()))
