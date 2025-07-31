from app.core.title_generator import generate_song_title, check_title_makes_sense
import pytest
from unittest.mock import patch

class TestTitleGenerator:
    
    def test_generate_basic_title(self):
        """Test basic title generation functionality."""
        title = generate_song_title(genre="techno", mood="happy", custom_words=["Neuro", "Glitchstorm"])
        assert isinstance(title, str)
        assert len(title) > 0
    
    def test_title_uniqueness(self):
        """Test that multiple generations produce different titles."""
        titles = set()
        for _ in range(20):
            title = generate_song_title(genre="techno", mood="dark")
            titles.add(title)
        
        # Should have at least 70% unique titles
        assert len(titles) >= 14, f"Only {len(titles)} unique titles out of 20"
    
    def test_duplicate_word_prevention(self):
        """Test that duplicate words are prevented in same category."""
        # Generate many titles to check for duplicates
        for _ in range(50):
            title = generate_song_title(genre="idm", mood="psychedelic")
            words = title.lower().split()
            
            # No duplicate words should exist
            assert len(words) == len(set(words)), f"Duplicate words found in: {title}"
    
    def test_custom_words_integration(self):
        """Test that custom words appear in generated titles."""
        custom_words = ["Cyber", "Neural", "Quantum"]
        titles_with_custom = 0
        
        for _ in range(30):
            title = generate_song_title(genre="techno", custom_words=custom_words)
            title_lower = title.lower()
            
            if any(word.lower() in title_lower for word in custom_words):
                titles_with_custom += 1
        
        # At least 25% should contain custom words
        assert titles_with_custom >= 8, f"Only {titles_with_custom} titles contained custom words"
    
    def test_genre_validation(self):
        """Test invalid genre handling."""
        title = generate_song_title(genre="nonexistent_genre")
        assert title == "Genre not found"
    
    def test_mood_filtering(self):
        """Test that mood filtering affects word selection."""
        dark_titles = [generate_song_title(genre="ambient", mood="dark") for _ in range(10)]
        bright_titles = [generate_song_title(genre="ambient", mood="bright") for _ in range(10)]
        
        # Dark titles should be different from bright titles
        assert set(dark_titles) != set(bright_titles)
    
    def test_quality_check_enabled(self):
        """Test quality check functionality."""
        for _ in range(20):
            title = generate_song_title(genre="ambient", quality_check=True)
            assert check_title_makes_sense(title, "ambient"), f"Quality check failed for: {title}"
    
    def test_quality_check_disabled(self):
        """Test that quality check can be disabled."""
        # This should be faster and may produce lower quality titles
        title = generate_song_title(genre="ambient", quality_check=False)
        assert isinstance(title, str)
        assert len(title) > 0
    
    def test_contradiction_detection(self):
        """Test that contradictory adjectives are detected."""
        # Mock a title with contradictions
        assert not check_title_makes_sense("Dark Bright Machine", "techno")
        assert not check_title_makes_sense("Happy Sad Vibes", "ambient")
        assert not check_title_makes_sense("Fast Slow Rhythm", "idm")
        
        # Valid titles should pass
        assert check_title_makes_sense("Dark Deep Machine", "techno")
        assert check_title_makes_sense("Happy Bright Melody", "ambient")
    
    def test_genre_conflict_detection(self):
        """Test genre-specific conflict detection."""
        # Ambient shouldn't have aggressive words
        assert not check_title_makes_sense("Aggressive Ambient Sound", "ambient")
        assert not check_title_makes_sense("Brutal Peaceful Waves", "ambient")
        
        # Hardcore shouldn't have peaceful words
        assert not check_title_makes_sense("Peaceful Hardcore Beat", "hardcore")
        assert not check_title_makes_sense("Calm Gentle Rage", "hardcore")
        
        # Valid combinations should pass
        assert check_title_makes_sense("Deep Ambient Waves", "ambient")
        assert check_title_makes_sense("Aggressive Hardcore Beat", "hardcore")
    
    def test_empty_parameters(self):
        """Test behavior with empty/None parameters."""
        title = generate_song_title(genre="techno", mood=None, custom_words=None)
        assert isinstance(title, str)
        assert len(title) > 0
        
        title = generate_song_title(genre="techno", mood="", custom_words=[])
        assert isinstance(title, str)
        assert len(title) > 0
    
    def test_max_attempts_fallback(self):
        """Test that fallback works when max attempts is reached."""
        # Mock scenario where quality check always fails
        with patch('app.core.title_generator.check_title_makes_sense', return_value=False):
            title = generate_song_title(genre="techno", quality_check=True, max_attempts=3)
            # Should still return a title (fallback)
            assert isinstance(title, str)
            assert len(title) > 0
    
    def test_title_capitalization(self):
        """Test that titles are properly capitalized."""
        title = generate_song_title(genre="techno")
        words = title.split()
        
        # Each word should start with capital letter
        for word in words:
            assert word[0].isupper(), f"Word '{word}' not capitalized in: {title}"
    
    def test_performance_benchmark(self):
        """Test generation performance."""
        import time
        
        start_time = time.time()
        for _ in range(100):
            generate_song_title(genre="techno", quality_check=True)
        end_time = time.time()
        
        # Should generate 100 titles in under 5 seconds
        total_time = end_time - start_time
        assert total_time < 5.0, f"Performance too slow: {total_time:.2f}s for 100 titles"
    
    @pytest.mark.parametrize("genre", ["techno", "ambient", "idm", "trance"])
    def test_all_genres(self, genre):
        """Test title generation for all supported genres."""
        title = generate_song_title(genre=genre)
        assert isinstance(title, str)
        assert len(title) > 0
        assert title != "Genre not found"
    
    @pytest.mark.parametrize("mood", ["dark", "bright", "happy", "sad", "energetic", "calm"])
    def test_all_moods(self, mood):
        """Test title generation with different moods."""
        title = generate_song_title(genre="techno", mood=mood)
        assert isinstance(title, str)
        assert len(title) > 0
    
    def test_stress_test(self):
        """Stress test with many rapid generations."""
        titles = []
        for _ in range(100):
            title = generate_song_title(genre="techno", quality_check=True)
            titles.append(title)
            assert isinstance(title, str)
            assert len(title) > 0
        
        # Check diversity
        unique_titles = set(titles)
        diversity_ratio = len(unique_titles) / len(titles)
        assert diversity_ratio > 0.5, f"Low diversity: {diversity_ratio:.2f}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])