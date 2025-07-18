song_title_data = {
    "extended_mood_map": {
        "relaxed": {
            "verbs": ["Flow", "Slide", "Sync", "Glide", "Feel"],
            "nouns": ["Loop", "Echo", "Groove", "Soul", "Rhythm"],
            "adjectives": ["Smooth", "Warm", "Silent", "Velvety", "Soft"]
        },
        "dark": {
            "verbs": ["Crush", "Override", "Break", "Annihilate"],
            "nouns": ["Drone", "System", "Collapse", "Shadow", "Code"],
            "adjectives": ["Brutal", "Dark", "Cold", "Industrial", "Raw"]
        },
        "uplifting": {
            "verbs": ["Rise", "Lift", "Shine", "Awaken"],
            "nouns": ["Pulse", "Light", "Sky", "Dream", "Energy"],
            "adjectives": ["Bright", "Golden", "Soulful", "Euphoric"]
        },
        "happy": {
            "verbs": ["Dance", "Love", "Feel", "Ignite"],
            "nouns": ["Joy", "Beat", "Vibe", "Motion"],
            "adjectives": ["Happy", "Sweet", "Bubbly", "Sunny"]
        },
        "psychedelic": {
            "verbs": ["Trip", "Melt", "Twist", "Spin", "Drift"],
            "nouns": ["Wave", "Vision", "Pattern", "Signal", "Frequency"],
            "adjectives": ["Hypnotic", "Glitchy", "Trippy", "Spaced", "Cosmic"]
        }
    },

    "techno": {
        "templates": [
            "{verb} {noun}",
            "{noun}",
            "{adjective} {noun}",
            "{verb} the {noun}",
            "{adjective} {noun} {noun}",
            "{verb} your {noun}",
            "{noun} {noun} of {noun}"
        ],
        "verbs": ["Push", "Control", "Break", "Drive", "Crush", "Shift", "Surge",
                  "Sync", "Blast", "Flow", "Override", "Reset", "Charge", "Spin"],
        "nouns": ["Machine", "Pulse", "System", "Code", "Loop", "Echo", "Wave",
                  "Grid", "Circuit", "Frequency", "Shift", "Feedback", "Module", "Drone"],
        "adjectives": ["Dark", "Deep", "Raw", "Silent", "Electric", "Industrial",
                       "Hypnotic", "Brutal", "Minimal", "Atomic", "Digital", "Cold"]
    },
    "house": {
        "templates": [
            "{verb} to {feel}",
            "{adjective} {emotion}",
            "{verb} {pronoun}",
            "{adjective} {noun}",
            "{noun} of {noun}",
            "{verb} your {noun}",
            "{adjective} Soul {noun}"
        ],
        "verbs": ["Move", "Feel", "Touch", "Love", "Groove", "Slide", "Flow",
                  "Dance", "Hold", "Turn", "Ignite", "Awaken", "Rise"],
        "feel": ["Feel", "Groove", "Dance", "Soul", "Rhythm", "Beat"],
        "emotion": ["Desire", "Affection", "Attraction", "Passion", "Connection", "Warmth"],
        "adjectives": ["Afraid", "Lonely", "Happy", "Lost", "Warm", "Sweet",
                       "Deep", "Smooth", "Soulful", "Bright", "Velvety", "Golden"],
        "pronoun": ["You", "Me", "Us", "Them", "All", "Every"]
    },
    "trance": {
        "templates": [
            "{question}",
            "{statement}",
            "{verb} {noun}",
            "{noun} of {noun}",
            "{adjective} {noun}",
            "{verb} your {noun}"
        ],
        "question": ["What Took You So Long?", "Where Are You {verb} Now?",
                     "Why Wait?", "Do You {verb}?", "Are We Alive?",
                     "Have We Met?", "When Will We Rise?"],
        "statement": ["Just Breathe", "We Belong", "Never Forget",
                      "Eternity", "Awaken", "Stay Alive", "Embrace Light"],
        "verbs": ["Remember", "Embrace", "Believe", "Lift", "Rise", "Shine", "Unite"],
        "nouns": ["Light", "Euphoria", "Dreams", "Sky", "Hearts", "Souls", "Journey"],
        "adjectives": ["Euphoric", "Melodic", "Uplifted", "Soulful", "Divine", "Celestial"]
    },
    "dub_reggae": {
        "templates": [
            "{noun} Dub",
            "{adjective} {riddim}",
            "{noun} of {noun}",
            "{riddim} {noun}",
            "{adjective} Dub {noun}",
            "{verb} the {noun}",
            "{adjective} Roots {noun}"
        ],
        "noun": ["Zion", "Rasta", "Roots", "Jah", "Spirit", "Kingdom",
                 "Vibration", "Echo", "Bass", "Journey", "Rebel", "Dubplate"],
        "adjective": ["Heavy", "Conscious", "Jah", "Rooted", "Mystic",
                      "Dubwise", "Subsonic", "Peaceful", "Spiritual", "Reverent", "Echoing"],
        "riddim": ["Riddim", "Version", "Bassline", "Dubplate", "Rhythm",
                   "Dubmix", "Echo", "Wave", "Track", "Mixin"],
        "verb": ["Shake", "Move", "Feel", "Let", "Rumble", "Echo"]
    },
    "idm": {
        "templates": [
            "{year}",
            "{noun} {glitch}",
            "{abstract}",
            "{verb} the {signal}",
            "{noun} of {abstract}",
            "{glitch} {noun}",
            "{verb} your {noun}"
        ],
        "year": ["1969", "2099", "Tha", "3030", "7777", "1984", "1001", "2049", "8080", "9999"],
        "noun": ["Memory", "Data", "Signal", "Pulse", "Grid", "Noise",
                "Frame", "Buffer", "Vector", "Sample", "Pattern", "System"],
        "glitch": ["Corruption", "Drift", "Distortion", "Glitch", "Skip",
                "Stutter", "Error", "Crash", "Bloom", "Fragment"],
        "abstract": ["Do You Know Squarepusher", "You're Creeping Me Out",
                    "Experience", "Complex Echo", "Digital Dream", "Fragmented Reality"],
        "verb": ["Read", "Write", "Encrypt", "Decode", "Override", "Trace", "Probe", "Scan", "Render", "Compile"],
        "signal": ["Signal", "Data", "Echo", "Wave", "Packet", "Stream", "Frame", "Pulse", "Burst", "Code"]
    },
    "garage": {
        "templates": [
            "{adjective} Nights", "Late {noun}", "{noun} Sessions", "{adjective} {noun}", "{verb} the {noun}"
        ],
        "adjective": ["Velvet", "Shadow", "Urban", "Silky", "Deep", "Private", "Hidden", "Warm"],
        "noun": ["Drive", "Groove", "Bass", "Streets", "Echoes", "Rooms", "Keys"],
        "verb": ["Slide", "Ride", "Feel", "Groove", "Enter"]
    },
    "lofi": {
        "templates": [
            "{adjective} {noun}", "{mood} {time}", "{adjective} {emotion}", "{noun} {time}"
        ],
        "adjective": ["Quiet", "Warm", "Dusty", "Slow", "Blurry", "Dim"],
        "noun": ["Beats", "Thoughts", "Dreams", "Moments", "Loops"],
        "mood": ["Late", "Soft", "Muted", "Lazy"],
        "time": ["Night", "Morning", "Evening"]
    },
    "italo_disco": {
        "templates": [
            "{verb} the {noun}", "{something} {night}", "{adjective} {love}", "Electric {noun}", "Dance with {noun}"
        ],
        "verb": ["Touch", "Chase", "Desire", "Feel"],
        "noun": ["Fantasy", "Heart", "Desire", "Motion", "Star"],
        "something": ["Neon", "Cosmic", "Romantic", "Future"],
        "night": ["Night", "Dream", "Fire", "Vibes"],
        "adjective": ["Retro", "Passionate", "Digital"],
        "love": ["Affair", "Emotion", "Desire"]
    },
    "ambient": {
        "templates": [
            "{verb} {direction}", "{stars}", "{abstract}", "{verb} {noun}", "{noun} {noun}"
        ],
        "verb": ["Floating", "Drifting", "Descending", "Emerging"],
        "direction": ["Inward", "Downward", "Beyond"],
        "stars": ["Glow", "Light Echo", "Stars", "Radiance"],
        "abstract": ["Silent Collapse", "Empty Fields", "Infinite Drift"],
        "noun": ["Silence", "Light", "Memory", "Depth"]
    },
    "indie_electronic": {
        "templates": [
            "{verb}", "{verb}ing", "{noun} {verb}ing", "Drift {noun}", "{adjective} {noun}"
        ],
        "verb": ["Fade", "Wait", "Breathe", "Glow"],
        "noun": ["Night", "Moment", "Shadow", "Sound"],
        "adjective": ["Gentle", "Echoing", "Glowing"]
    },
    "shoegaze": {
        "templates": [
            "{noun}", "{adjective} {noun}", "{noun} of {noun}", "{verb} the {noun}"
        ],
        "noun": ["Dreams", "Shadows", "Waves", "Fuzz"],
        "adjective": ["Faded", "Noisy", "Shimmering"],
        "verb": ["See", "Feel", "Chase"]
    },
    "dub_house": {
        "templates": [
            "{adjective} {groove}", "{noun} {effect}", "{noun} of {noun}"
        ],
        "adjective": ["Deep", "Subtle", "Analog"],
        "groove": ["Groove", "Riddim", "Vibe"],
        "noun": ["Bass", "Loop", "Space"],
        "effect": ["Dub", "Echo", "Reverb"]
    },
    "dub_techno": {
        "templates": [
            "{noun} Dub", "{adjective} {noun}", "{noun} of {noun}"
        ],
        "noun": ["Grid", "Signal", "Phase"],
        "adjective": ["Frozen", "Submerged", "Basic"]
    },
    "psydub": {
        "templates": [
            "{adjective} {noun}", "{concept} Dub", "{noun} of {concept}"
        ],
        "adjective": ["Trippy", "Psychedelic", "Mystical"],
        "noun": ["Journey", "Temple", "Consciousness"],
        "concept": ["Shaman", "Vision", "Frequency"]
    },
    "nu_disco": {
        "templates": [
            "{verb} into {noun}", "{adjective} {color}", "{adjective} Disco {noun}"
        ],
        "verb": ["Step", "Slide", "Glide"],
        "noun": ["Rhythm", "Light", "Floor"],
        "adjective": ["Velvet", "Retro", "Bright"],
        "color": ["Gold", "Silver", "Pink"]
    },
    "riddim": {
        "templates": [
            "{noun}", "{verb} the {bass}", "{adjective} {noun}"
        ],
        "noun": ["Drop", "Slap", "Bassline"],
        "verb": ["Smash", "Wobble", "Crush"],
        "bass": ["Bass", "Sub", "Wave"],
        "adjective": ["Heavy", "Massive", "Brutal"]
    },
    "bleep_techno": {
        "templates": [
            "{sound} {noun}", "{adjective} {bleep}", "{sound} the {noun}"
        ],
        "sound": ["Bleep", "Zap", "Ping"],
        "noun": ["Machine", "Loop", "Code"],
        "adjective": ["Minimal", "Digital", "Sparse"],
        "bleep": ["Pattern", "Sequence", "Cycle"]
    },
    "hardgroove": {
        "templates": [
            "{adjective} {groove}", "{verb} {beat}", "{verb} the {groove}"
        ],
        "adjective": ["Tribal", "Syncopated", "Energetic"],
        "groove": ["Groove", "Flow", "Pattern"],
        "verb": ["Drive", "Bounce", "Thump"],
        "beat": ["Beat", "Kick", "Rumble"]
    },
    "schranz": {
        "templates": [
            "{verb} the {machine}", "{adjective} {noun}", "{noun} of {noun}"
        ],
        "verb": ["Crush", "Annihilate", "Pound"],
        "machine": ["System", "Engine", "Loop"],
        "adjective": ["Brutal", "Hard", "Industrial"],
        "noun": ["Wall", "Force", "Structure"]
    },
    "wave": {
        "templates": [
            "{adjective} {noun}", "{effect} {wave}", "{adjective} Neon {noun}"
        ],
        "adjective": ["Cold", "Neon", "Retro"],
        "noun": ["Dream", "Vision", "Shadow"],
        "effect": ["Dark", "Digital", "Shimmer"],
        "wave": ["Wave", "Signal", "Pulse"]
    }
}

