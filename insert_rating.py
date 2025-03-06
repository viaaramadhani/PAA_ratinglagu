#Kelompok 2 (Insertion Sort)
# Deskripsi: Program ini akan mengurutkan data lagu berdasarkan popularitas secara ascending (dari yang terkecil ke terbesar) menggunakan algoritma Insertion Sort.

#array yang menampung data lagu
data_lagu = [
    {"track_name": "Blinding Lights", "artist": "The Weeknd", "popularity": 100},
    {"track_name": "Dance Monkey", "artist": "Tones and I", "popularity": 98},
    {"track_name": "Shape of You", "artist": "Ed Sheeran", "popularity": 97},
    {"track_name": "Someone You Loved", "artist": "Lewis Capaldi", "popularity": 95},
    {"track_name": "Stay", "artist": "The Kid LAROI, Justin Bieber", "popularity": 94},
    {"track_name": "Bad Guy", "artist": "Billie Eilish", "popularity": 93},
    {"track_name": "Sunflower", "artist": "Post Malone, Swae Lee", "popularity": 92},
    {"track_name": "Watermelon Sugar", "artist": "Harry Styles", "popularity": 90},
    {"track_name": "Levitating", "artist": "Dua Lipa", "popularity": 89},
    {"track_name": "Happier", "artist": "Marshmello, Bastille", "popularity": 88},
    {"track_name": "Shallow", "artist": "Lady Gaga, Bradley Cooper", "popularity": 87},
    {"track_name": "Perfect", "artist": "Ed Sheeran", "popularity": 86},
    {"track_name": "Rockstar", "artist": "Post Malone, 21 Savage", "popularity": 85},
    {"track_name": "Goosebumps", "artist": "Travis Scott", "popularity": 84},
    {"track_name": "Lucid Dreams", "artist": "Juice WRLD", "popularity": 83},
    {"track_name": "Girls Like You", "artist": "Maroon 5, Cardi B", "popularity": 82},
    {"track_name": "Don't Start Now", "artist": "Dua Lipa", "popularity": 81},
    {"track_name": "Senorita", "artist": "Shawn Mendes, Camila Cabello", "popularity": 80},
    {"track_name": "Drivers License", "artist": "Olivia Rodrigo", "popularity": 79},
    {"track_name": "Save Your Tears", "artist": "The Weeknd", "popularity": 78},
    {"track_name": "Heat Waves", "artist": "Glass Animals", "popularity": 77},
    {"track_name": "Peaches", "artist": "Justin Bieber, Daniel Caesar, Giveon", "popularity": 76},
    {"track_name": "Sicko Mode", "artist": "Travis Scott", "popularity": 75},
    {"track_name": "Circles", "artist": "Post Malone", "popularity": 74},
    {"track_name": "7 Rings", "artist": "Ariana Grande", "popularity": 73},
    {"track_name": "Industry Baby", "artist": "Lil Nas X, Jack Harlow", "popularity": 72},
    {"track_name": "Montero (Call Me By Your Name)", "artist": "Lil Nas X", "popularity": 71},
    {"track_name": "Without Me", "artist": "Halsey", "popularity": 70},
    {"track_name": "Memories", "artist": "Maroon 5", "popularity": 69},
    {"track_name": "No Tears Left to Cry", "artist": "Ariana Grande", "popularity": 68}
]

#Menggunakan algoritma insertion sort untuk mengurutkan data lagu berdasarkan popularitas
def insertion_sort(data_lagu):
    for i in range(1, len(data_lagu)):
        key = data_lagu[i]
        j = i - 1
        while j >= 0 and data_lagu[j]["popularity"] > key["popularity"]:
            data_lagu[j + 1] = data_lagu[j]
            j -= 1
        data_lagu[j + 1] = key

# Urutkan berdasarkan popularitas secara ascending (dari yang terkecil ke terbesar)
insertion_sort(data_lagu)
print("\nLagu setelah diurutkan berdasarkan popularitas (ascending)):")
for lagu in data_lagu:
    print(f"{lagu['track_name']} - {lagu['artist']} (Popularity: {lagu['popularity']})")