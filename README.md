# 🎵 Songtitle Generator Service

A modular, production-ready microservice for generating creative German song titles based on mood, theme, and musical style – built with **FastAPI** and a custom rule-based algorithm (no AI required).

## 🚀 Features

- 🎛️ Rule-based title generator using mood, theme, and style
- 🧠 Rich word templates with poetic structure
- ⚡️ Lightweight FastAPI server with one clean endpoint
- 🧪 Includes unit tests for core logic
- 🧩 Designed for separation into microservices and frontend component usage

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
    "ambient",
    "bleep_techno",
    "dub_house",
    "dub_reggae",
    "dub_techno",
    "garage",
    "hardgroove",
    "house",
    "idm",
    "indie_electronic",
    "italo_disco",
    "lofi",
    "nu_disco",
    "psydub",
    "riddim",
    "schranz",
    "shoegaze",
    "techno",
    "trance",
    "wave"
  ],
  "moods": ["dark", "happy", "psychedelic", "relaxed", "uplifting"]
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
  "genre": "string", // Required: One of the available genres
  "mood": "string", // Optional: One of the available moods
  "custom_words": ["string"] // Optional: Array of custom words to incorporate
}
```

**Response:**

```json
{
  "title": "Generated Song Title"
}
```

**Examples:**

_Basic usage:_

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"genre": "techno"}'
```

_With mood:_

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"genre": "techno", "mood": "dark"}'
```

_With custom words:_

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

#### Angular HTTP with RxJS

```typescript
import { HttpClient } from "@angular/common/http";

export class SongTitleComponent {
  constructor(private http: HttpClient) {}

  // Get metadata
  getMetadata() {
    return this.http
      .get("http://localhost:8000/metadata/")
      .subscribe((data) => console.log(data));
  }

  // Generate title
  generateTitle() {
    return this.http
      .post("http://localhost:8000/generate", {
        genre: "techno",
        mood: "dark",
        custom_words: ["Neural", "Matrix"],
      })
      .subscribe((response) => console.log(response.title));
  }
}
```

#### Vanilla JavaScript

```javascript
// Get available options for dropdowns
async function getMetadata() {
  const response = await fetch("/metadata/");
  const data = await response.json();
  return data;
}

// Generate a song title
async function generateTitle(genre, mood = null, customWords = []) {
  const response = await fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      genre: genre,
      mood: mood,
      custom_words: customWords,
    }),
  });
  const data = await response.json();
  return data.title;
}

// Usage example
const metadata = await getMetadata();
const title = await generateTitle("techno", "dark", ["Neural", "Matrix"]);
console.log("Generated title:", title);
```

### Error Handling

The API uses standard HTTP status codes and graceful error handling:

- `200 OK` - Successful request
- `422 Unprocessable Entity` - Invalid request body or parameters
- `500 Internal Server Error` - Server error

**Note:** Invalid genres will return `{"title": "Genre not found"}` rather than throwing an error, allowing frontend applications to handle this gracefully.

### Interactive Documentation

Once the server is running, visit `http://localhost:8000/docs` for an interactive Swagger UI where you can test the endpoints directly.
