# 🎵 Songtitle Generator Service

A modular, production-ready microservice for generating creative German song titles based on mood, theme, and musical style – built with **FastAPI** and a custom rule-based algorithm (no AI required).

---

## 🚀 Features

- 🎛️ Rule-based title generator using mood, theme, and style
- 🧠 Rich word templates with poetic structure
- ⚡️ Lightweight FastAPI server with one clean endpoint
- 🧪 Includes unit tests for core logic
- 🧩 Designed for separation into microservices and frontend component usage

---

## 🧠 Example Output

```text
💿 House:
  - Groove Your Soul
  - Bright Emotion

🔊 Techno:
  - Crush The Circuit
  - Silent Frequency Shift

🔥 Garage:
  - Velvet Nights
  - Ride The Drive

🌿 Dub / Reggae:
  - Mystic Dubplate
  - Heavy Roots Vibration
```

## ⚙️ Usage

```bash
make start    # Start server (Development)
make dev      # Server with all hosts
make prod     # Production server
pytest        # Run tests
make install  # Install dependencies
make clean    # Delete cache files
```

---

## 📖 API Documentation

### Base URL
When running locally: `http://localhost:8000`

### Authentication
No authentication required.

### Endpoints

#### 1. Get Metadata
Get all available genres and moods for frontend UI elements.

**Endpoint:** `GET /metadata/`

**Response:**
```json
{
  "genres": [
    "ambient", "bleep_techno", "dub_house", "dub_reggae", "dub_techno",
    "garage", "hardgroove", "house", "idm", "indie_electronic", 
    "italo_disco", "lofi", "nu_disco", "psydub", "riddim", 
    "schranz", "shoegaze", "techno", "trance", "wave"
  ],
  "moods": [
    "dark", "happy", "psychedelic", "relaxed", "uplifting"
  ]
}
```

**Example:**
```bash
curl -X GET "http://localhost:8000/metadata/"
```

#### 2. Generate Song Title
Generate a creative song title based on genre, mood, and optional custom words.

**Endpoint:** `POST /generate`

**Request Body:**
```json
{
  "genre": "string",           // Required: One of the available genres
  "mood": "string",            // Optional: One of the available moods
  "custom_words": ["string"]   // Optional: Array of custom words to incorporate
}
```

**Response:**
```json
{
  "title": "Generated Song Title"
}
```

**Examples:**

*Basic usage:*
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"genre": "techno"}'
```

*With mood:*
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"genre": "techno", "mood": "dark"}'
```

*With custom words:*
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"genre": "ambient", "mood": "relaxed", "custom_words": ["Ocean", "Waves"]}'
```

### Available Options

#### Genres (20 total)
- `ambient` - Atmospheric, ambient music
- `bleep_techno` - Minimal techno with bleeps and bloops
- `dub_house` - House music with dub influences
- `dub_reggae` - Reggae with dub effects
- `dub_techno` - Techno with dub influences
- `garage` - UK garage style
- `hardgroove` - Hard, groovy electronic music
- `house` - Classic house music
- `idm` - Intelligent Dance Music
- `indie_electronic` - Independent electronic music
- `italo_disco` - Italian disco style
- `lofi` - Lo-fi, relaxed beats
- `nu_disco` - Modern disco revival
- `psydub` - Psychedelic dub
- `riddim` - Riddim dubstep
- `schranz` - Hard techno style
- `shoegaze` - Dreamy, reverb-heavy music
- `techno` - Classic electronic techno
- `trance` - Trance music
- `wave` - Synthwave/retrowave

#### Moods (5 total)
- `dark` - Dark, mysterious themes
- `happy` - Upbeat, joyful themes
- `psychedelic` - Trippy, mind-bending themes
- `relaxed` - Calm, peaceful themes
- `uplifting` - Inspiring, energetic themes

### Frontend Integration Examples

#### JavaScript/Fetch API
```javascript
// Get available options for dropdowns
async function getMetadata() {
  const response = await fetch('/metadata/');
  const data = await response.json();
  return data;
}

// Generate a song title
async function generateTitle(genre, mood = null, customWords = []) {
  const response = await fetch('/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      genre: genre,
      mood: mood,
      custom_words: customWords
    })
  });
  const data = await response.json();
  return data.title;
}

// Usage example
const metadata = await getMetadata();
const title = await generateTitle('techno', 'dark', ['Neural', 'Matrix']);
```

#### React Component Example
```jsx
import React, { useState, useEffect } from 'react';

function SongTitleGenerator() {
  const [metadata, setMetadata] = useState({ genres: [], moods: [] });
  const [genre, setGenre] = useState('');
  const [mood, setMood] = useState('');
  const [customWords, setCustomWords] = useState('');
  const [generatedTitle, setGeneratedTitle] = useState('');

  useEffect(() => {
    fetch('/metadata/')
      .then(res => res.json())
      .then(data => setMetadata(data));
  }, []);

  const handleGenerate = async () => {
    const response = await fetch('/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        genre,
        mood: mood || null,
        custom_words: customWords ? customWords.split(',').map(w => w.trim()) : []
      })
    });
    const data = await response.json();
    setGeneratedTitle(data.title);
  };

  return (
    <div>
      <select value={genre} onChange={(e) => setGenre(e.target.value)}>
        <option value="">Select Genre</option>
        {metadata.genres.map(g => <option key={g} value={g}>{g}</option>)}
      </select>
      
      <select value={mood} onChange={(e) => setMood(e.target.value)}>
        <option value="">Select Mood (Optional)</option>
        {metadata.moods.map(m => <option key={m} value={m}>{m}</option>)}
      </select>
      
      <input
        type="text"
        placeholder="Custom words (comma-separated)"
        value={customWords}
        onChange={(e) => setCustomWords(e.target.value)}
      />
      
      <button onClick={handleGenerate} disabled={!genre}>
        Generate Title
      </button>
      
      {generatedTitle && <h3>Generated: {generatedTitle}</h3>}
    </div>
  );
}
```

### Error Handling
The API uses standard HTTP status codes and graceful error handling:
- `200 OK` - Successful request
- `422 Unprocessable Entity` - Invalid request body or parameters
- `500 Internal Server Error` - Server error

**Note:** Invalid genres will return `{"title": "Genre not found"}` rather than throwing an error, allowing frontend applications to handle this gracefully.

### Interactive Documentation
Once the server is running, visit `http://localhost:8000/docs` for an interactive Swagger UI where you can test the endpoints directly.
