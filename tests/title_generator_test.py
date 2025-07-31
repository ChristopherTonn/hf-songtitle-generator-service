from app.core.title_generator import generate_song_title

def test_generate_basic_title():
    title = generate_song_title(genre="techno", mood="happy", custom_words=["Neuro", "Glitchstorm"])
    assert isinstance(title, str)
    assert len(title) > 0