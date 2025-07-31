from fastapi import FastAPI
from app.routes import generate
from app.song_title_data import song_title_data
from app.core.title_generator import generate_song_title
import random

app = FastAPI()

app.include_router(generate.router, prefix="/generate")

# Get available genres (excluding 'extended_mood_map')
available_genres = [key for key in song_title_data if key != "extended_mood_map"]

# Default moods
default_moods = ["happy", "sad", "energetic", "calm", "dark", "bright"]

# Example custom words to randomly select from
custom_word_options = [
    "Neuro", "Glitchstorm", "Cosmic", "Dream", "Ocean", "Fire", "Wind", 
    "Earth", "Digital", "Analog", "Retro", "Future", "Crystal", "Shadow", 
    "Light", "Space", "Urban", "Jungle", "Desert", "Mountain", "Sky", 
    "Heart", "Mind", "Soul", "Spirit", "Electric", "Acoustic", "Sonic", 
    "Lunar", "Solar", "Stellar", "Astral", "Quantum", "Cyber", "Virtual"
]

print("🎶 Generating 100 Example Song Titles:")
print()

def generate_and_print_titles(num_titles, print_metadata=False):
    demo_title_no_sub = None
    for i in range(num_titles):
        # Select random genre
        genre = random.choice(available_genres)
        
        # Select random mood
        mood = random.choice(default_moods)
        
        # Select 1-3 random custom words
        num_custom_words = random.randint(1, 3)
        custom_words = random.sample(custom_word_options, num_custom_words)
        
        # Generate the song title
        title = generate_song_title(
            genre=genre,
            mood=mood,
            custom_words=custom_words
        )
        
        # Print the title with or without metadata
        if print_metadata:
            print(f"{i+1}. Genre: {genre}, Mood: {mood}")
            print(f"   Custom Words: {', '.join(custom_words)}")
            print(f"   Title : {title}")
            print()
        else:
            print(f"{i+1}. {title}")
        
        # Keep track of the last title
        demo_title_no_sub = title
    return demo_title_no_sub

print("🎶 Generating 100 Example Song Titles:")
print()
demo_title_no_sub = generate_and_print_titles(100, print_metadata=True)

print("🎶 Generating 100 Example Song Titles (Titles Only):")
print()
demo_title_no_sub = generate_and_print_titles(100, print_metadata=False)

# print("🎶 Generated Song Title:" )
# print(demo_title_no_sub)