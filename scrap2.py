import re

data = """"
Lakme
Forever Matte Liquid Lip
Rs. 297Rs. 450(34% OFF)
icon
4.4
|
106.9k
AD
Maybelline New York Color Sensational Creamy Matte Lipstick - Touch of Spice 660
TRENDING
Maybelline
660 Touch Of Spice Lipstick
Rs. 207Rs. 329(37% OFF)
icon
4.4
|
16.2k
ETUDE Dear Darling Water Tint 9g - Red Grapefruit Ade 4
ETUDE
Dear Darling Water Tint - 4
Rs. 382Rs. 450(15% OFF)
icon
4.5
|
173.8k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Pioneer 20
Maybelline
Super Stay Matte - Pioneer 20
Rs. 419Rs. 749(44% OFF)
icon
4.3
|
6.1k
AD
Mamaearth Moisture Matte 12 Hour Long Stay Mini Lipstick - 0.7 g - 03 Candyfloss Pink
Mamaearth
Moisture Matte Candyfloss Pink
Rs. 314Rs. 349(10% OFF)
icon
4.4
|
16.2k
ETUDE Dear Darling Water Gel Lip & Cheek Tint Lipstick 9 g - Cherry Ade 02
ETUDE
Dear Darling Water Tint - 02
Rs. 382Rs. 450(15% OFF)
icon
4.5
|
173.8k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Founder 115
Maybelline
Super Stay Matte - Founder 115
Rs. 449Rs. 749(40% OFF)
icon
4.3
|
17.1k
AD
Mamaearth Moisture Matte Longstay Lipstick with Avocado Oil & Vitamin E- Bubblegum Nude 05
Mamaearth
Moisture MatteBubblegum Nude
Rs. 299Rs. 599(50% OFF)
icon
4.5
|
54k
Maybelline New York Superstay Vinyl Ink Liquid Lipstick 4.5 ml - Lippy
Maybelline
Superstay Lipstick - Lippy
Rs. 517Rs. 849(39% OFF)
icon
4.4
|
9.1k
Earth Rhythm Lip & Cheek Tint With Pomegranate Flower Extracts & Jojoba Oil - Brandy 5 ml
Earth Rhythm
Lip & Cheek Tint - Brandy 5 ml
Rs. 299Rs. 499(40% OFF)
icon
4.2
|
13.3k
AD
Mamaearth Creamy Matte Long Stay Lipstick With Murumuru Butter - Apricot Taupe
Mamaearth
Creamy Matte Apricot Taupe
Rs. 239Rs. 399(40% OFF)
icon
4.5
|
173.6k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Globe Trotter 135
Maybelline
Super Stay Ink- Globe Trotter
Rs. 359Rs. 749(52% OFF)
icon
4.5
|
173.3k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Seeker 245
Maybelline
Super Stay Matte Ink - Seeker
Rs. 434Rs. 749(42% OFF)
icon
5
|
6
AD
Ruby's Organics OneStick Blurr & Lip & Cheek OneStick Crayon- Clay Pink
NEW
Ruby's Organics
OneStick Crayon- Clay Pink
Rs. 587Rs. 690(15% OFF)
4.5
|
173.7k
Maybelline New York Superstay Matte Ink Liquid Lipstick - 230 Transformer - 5ml
Maybelline
Super Stay Matte - Transformer
Rs. 441Rs. 749(41% OFF)
icon
3.6
|
5
Hilary Rhoda Match Maker Long Lasting Matte Lip Palette With Spatula & Brush - 12 g - 02
Hilary Rhoda
Matte Lip Palette - 12 g - 02
Rs. 271Rs. 339(20% OFF)
icon
4.5
|
173.5k
AD
Maybelline New York Superstay Matte Ink Matte Liquid Lipstick 5ml - Charmer
Maybelline
Liquid Lipstick - Charmer
Rs. 441Rs. 749(41% OFF)
icon
4.4
|
106.7k
Maybelline New York Color Sensational Creamy Matte Lipstick- Midtown Pink 673
Maybelline
Creamy Matte Lipstick- 673
Rs. 213Rs. 329(35% OFF)
icon
4.5
|
173.7k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Artist 120
Maybelline
Super Stay Matte Ink - Artist
Rs. 464Rs. 749(38% OFF)
icon
4.5
|
17.6k
AD
Maybelline New York SuperStay Matte Ink Crayon Lipstick - 25 Stay Exceptional
Maybelline
Superstay Matte Ink Crayon-25
Rs. 522Rs. 829(37% OFF)
icon
4.4
|
106.7k
Maybelline New York Color Sensational Creamy Matte Lipstick - Rich Ruby
Maybelline
Rich Ruby Sensational Lipstick
Rs. 207Rs. 329(37% OFF)
icon
4.4
|
79.4k
Maybelline New York Sensational Liquid Matte Lipstick 7 ml - Soft Wine 02
Maybelline
02 Soft Wine Matte Lipstick
Rs. 287Rs. 429(33% OFF)
icon
4.3
|
213.6k
AD
Lakme 9to5 Powerplay Priming Matte Lipstick With Vit E Lasts 16Hr 3.6g - MP6 Deep Wine
Lakme
Powerplay Priming Lipstick
Rs. 396Rs. 650(39% OFF)
icon
4.4
|
106.7k
Maybelline New York Color Sensational Creamy Matte Lipstick - Burgundy Blush
Maybelline
Creamy Matte - Burgundy Blush
Rs. 243Rs. 329(26% OFF)
icon
4.5
|
53.9k
Maybelline New York Superstay Vinyl Ink Liquid Lipstick 4.2ml - Extra
Maybelline
Superstay Vinyl Ink Lipstick
Rs. 517Rs. 849(39% OFF)
icon
5
|
5
AD
Ruby's Organics OneStick  Blurr- Lip and Cheek OneStick Crayon - 1 g - Beet
NEW
Ruby's Organics
OneStick Crayon- Beet
Rs. 587Rs. 690(15% OFF)
4.4
|
9.1k
Earth Rhythm Lip & Cheek Tint With Pomegranate Flower Extracts & Jojoba Oil - Cherry 5ml
Earth Rhythm
Lip & Cheek Tint - Cherry 5ml
Rs. 299Rs. 499(40% OFF)
icon
4.4
|
106.7k
Maybelline New York Color Sensational Creamy Matte Lipstick - East Village Rose 676
Maybelline
Lipstick-East Village Rose 676
Rs. 223Rs. 329(32% OFF)
icon
4.4
|
8.6k
AD
Maybelline New York Superstay Teddy Tint Lip & Cheek Color 5ml - Heart Locket
Maybelline
Superstay Teddy Tint LipColour
Rs. 614Rs. 749(18% OFF)
icon
4.5
|
173.8k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Ambitious 220
Maybelline
Super Stay Matte - Ambitious
Rs. 441Rs. 749(41% OFF)
icon
4.3
|
196
Hilary Rhoda Starlight Metallic Long Lasting Shine Glitter Lipstick 4 g - Cosmic Candy-01
Hilary Rhoda
Lipstick 4 g - Cosmic Candy-01
Rs. 194Rs. 229(15% OFF)
icon
4.4
|
18.9k
AD
MARS Set of 3 Matte Lipsticks Box - Reds and Maroons 01
MARS
Set of 3 Matte Lipsticks Box
Rs. 299Rs. 447(33% OFF)
icon
4.4
|
79.4k
Maybelline New York Sensational Liquid Matte Lipstick - 21 Nude Nuance - 7ml
Maybelline
Liquid Lipstick - Nude Nuance
Rs. 257Rs. 429(40% OFF)
icon
4.3
|
213.6k
Lakme 9to5 Powerplay Priming Matte Lipstick With Vit E Lasts 16Hr 3.6g - MR5 Berry Base
Lakme
Powerplay Priming Lipstick
Rs. 377Rs. 650(42% OFF)
icon
AD
Ruby's Organics OneStick Sculpt  Lip and Cheek OneStick Crayon- 1 g- Espresso
NEW
Ruby's Organics
OneStick Crayon- 1 g- Espresso
Rs. 587Rs. 690(15% OFF)
4.5
|
173.9k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Dancer 118
Maybelline
Super Stay Matte - Dancer 118
Rs. 419Rs. 749(44% OFF)
icon
4.4
|
106.8k
Maybelline New York Color Sensational Creamy Matte Lipstick - Bold Crimson 634
Maybelline
Creamy Matte Lipstick 634
Rs. 184Rs. 329(44% OFF)
icon
4.2
|
66.3k
AD
Lakme Cushion Matte Lipstick with French Rose Oil - Burgundy Bloom CB1
Lakme
Lipstick - Burgundy Bloom
Rs. 236Rs. 375(37% OFF)
icon
4.5
|
19.5k
Maybelline New York Color Sensational Creamy Matte Lipstick - 695 Divine Wine
Maybelline
Creamy Matte - 695 Divine Wine
Rs. 207Rs. 329(37% OFF)
icon
4.4
|
125.3k
Lakme Forever Matte Lightweight & Transferproof 16Hr Liquid Lipstick 5.6ml - Nude Latte
Lakme
Forever Matte Liquid Lip
Rs. 292Rs. 450(35% OFF)
icon
4.5
|
18.8k
AD
Maybelline New York Color Sensational Creamy Matte Lipstick - 657 Nude Nuance - 3.9g
Maybelline
Nude Nuance Matte Lipstick 657
Rs. 230Rs. 329(30% OFF)
icon
4.5
|
54k
Maybelline New York Superstay Vinyl Ink Liquid Lipstick 4.5 ml - Unrivaled
Maybelline
Superstay Vinyl Ink- Unrivaled
Rs. 568Rs. 849(33% OFF)
icon
4.4
|
107k
Maybelline New York Color Sensational Mesmerizing Magenta Creamy Matte Lipstick
Maybelline
Mesmerizing Magenta Lipstick
Rs. 190Rs. 329(42% OFF)
icon
4.5
|
173.3k
AD
Maybelline New York Super Stay Matte Ink Liquid Lipstick - 75 Fighter
Maybelline
Super Stay Matte - 75 Fighter
Rs. 546Rs. 749(27% OFF)
icon
4.3
|
6.2k
Pilgrim Matte Bullet Intense Colour Transferproof & Smudgeproof Lipstick - Alpha Brown 34
Pilgrim
Matte Bullet Lipstick - 34
Rs. 387Rs. 595(35% OFF)
icon
YUHME 1N5 Ultra Flawless Matte Liquid Lipstick- 6 ml - Terracotta
YUHME
1N5 Liquid Lipstick-Terracotta
Rs. 218Rs. 249(12% OFF)
icon
4.4
|
125k
AD
Lakme Forever Matte Lightweight & Transferproof 16Hr Liquid Lipstick 5.6ml - Nude Hue
Lakme
Forever Matte Lip Colour
Rs. 292Rs. 450(35% OFF)
icon
4.4
|
79.4k
Maybelline New York Sensational Liquid Matte Lipstick 7 ml - Sensationally Me 08
Maybelline
Liquid Matte Sensationally Me
Rs. 287Rs. 429(33% OFF)
icon
4.5
|
174k
Maybelline New York Super Stay Matte Ink Liquid Lipstick 5 ml - Lover 15
Maybelline
Super Stay Matte - 15 Lover
Rs. 471Rs. 749(37% OFF)
icon
4
|
34.5k
AD
Lakme
Sizes: 4-5 ML
Rs. 299Rs. 499(40% OFF)
Only Few Left!
"""""

# Pattern to extract prices and discount
price_pattern = re.compile(r"Rs\.\s*(\d+)\s*Rs\.\s*(\d+)\((\d+)% OFF\)")
# Pattern to extract rating and reviews
rating_pattern = re.compile(r"(\d\.\d)\s*\|\s*(\d+\.?\d*)k?")

for match in price_pattern.finditer(data):
    discounted, original, discount = match.groups()
    print(discounted, original, discount)

for match in rating_pattern.finditer(data):
    rating, reviews = match.groups()
    reviews = float(reviews) * 1000 if 'k' in match.group(0) else float(reviews)
    print(rating, int(reviews))