from typing import Optional, List
import random
import re
from app.song_title_data import song_title_data

def apply_mood_filter(pool: List[str], mood: Optional[str]) -> List[str]:
    """Filter words based on the given mood."""
    if not mood:
        return pool
    
    # filter words that match the mood
    filtered = [word for word in pool if mood.lower() in word.lower()]
    if not filtered:
        return pool
    
    combined = filtered + random.sample(pool, min(len(pool), 3))
    return list(set(combined))  # remove duplicates

def smart_merge(original_pool: List[str], custom_words: List[str], weight: float = 0.5) -> List[str]:
    """Merge original words with custom words based on the given weight."""
    merged = original_pool.copy()
    
    # Add some custom words based on weight
    num_to_add = max(1, int(len(original_pool) * weight))
    for _ in range(num_to_add):
        word = random.choice(custom_words)
        if word not in merged:
            merged.append(word)
    
    return merged

def check_title_makes_sense(title: str, genre: str) -> bool:
    
    # Check if title is empty
    words = title.lower().split()
    
    # No duplicate words
    if len(words) != len(set(words)):
        return False
    
    # No contradictory adjectives
    contradictions = [
        ("dark", "bright"), ("sad", "happy"), ("fast", "slow"),
        ("loud", "quiet"), ("big", "small"), ("deep", "shallow"),
        ("hard", "soft"), ("heavy", "light"), ("hot", "cold")
    ]
    
    for word1, word2 in contradictions:
        if word1 in words and word2 in words:
            return False
    
    # Genre consistency
    genre_conflicts = {
        "ambient": ["aggressive", "brutal", "violent", "harsh", "loud"],
        "hardcore": ["peaceful", "calm", "gentle", "soft", "quiet"],
        "classical": ["brutal", "harsh", "aggressive", "violent"],
        "chillout": ["aggressive", "brutal", "violent", "harsh"],
        "jazz": ["brutal", "violent", "aggressive"]
    }
    
    if genre in genre_conflicts:
        if any(conflict in words for conflict in genre_conflicts[genre]):
            return False
    
    return True

def generate_basic_title(
    genre: str,
    mood: Optional[str] = None,
    custom_words: Optional[List[str]] = None
) -> str:
    
    # Generate a basic song title based on genre, mood, and custom words.
    data = song_title_data.get(genre)
    if not data:
        return "Genre not found"

    template = random.choice(data["templates"])
    placeholders = re.findall(r"\{(.*?)\}", template)

    word_map = {}
    used_words = {}
    
    for key in placeholders:
        key_plural = key + "s" if key[-1] != "s" else key
        pool = data.get(key) or data.get(key_plural)

        if pool:
            pool = apply_mood_filter(pool, mood)
            if custom_words:
                pool = smart_merge(pool, custom_words, weight=0.4)
            
            if key in used_words:
                # Exclude already used words for this category
                available_pool = [word for word in pool if word not in used_words[key]]

                # If no words left, fallback to original pool
                if not available_pool:
                    available_pool = pool
            else:
                available_pool = pool
                used_words[key] = set()
            
            selected_word = random.choice(available_pool)
            word_map[key] = selected_word
            used_words[key].add(selected_word)
            
        else:
            fallback_words = ["Sound", "Beat", "Rhythm", "Melody", "Harmony", "Vibe", "Flow"]
            
            # Avoid duplicates in fallback words
            if key in used_words:
                available_fallback = [word for word in fallback_words if word not in used_words[key]]
                if not available_fallback:
                    available_fallback = fallback_words
            else:
                available_fallback = fallback_words
                used_words[key] = set()
            
            selected_word = random.choice(available_fallback)
            word_map[key] = selected_word
            used_words[key].add(selected_word)

    title = template.format(**word_map)
    title = " ".join([w.capitalize() for w in title.split()])
    return title

def generate_song_title(
    genre: str,
    mood: Optional[str] = None,
    custom_words: Optional[List[str]] = None,
    quality_check: bool = True,
    max_attempts: int = 5
) -> str:
    # Generate a song title with optional quality checks.

    for attempt in range(max_attempts if quality_check else 1):
        title = generate_basic_title(genre, mood, custom_words)
        
        if not quality_check:
            return title
        
        if check_title_makes_sense(title, genre):
            return title

    # fallback without checks, after max_attempts is reached
    return generate_basic_title(genre, mood, custom_words)