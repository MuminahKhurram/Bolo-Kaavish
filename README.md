# Sign Language Learning Application

## Prerequisites

- Node.js (v18 or higher)
- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. Install Python Dependencies:
```bash
pip install mediapipe numpy
```

2. Install Node.js Dependencies:
```bash
npm install
```

3. Start the Backend Server:
```bash
npm run server
```

4. Start the Frontend Development Server (in a new terminal):
```bash
npm run dev
```

## Project Structure

```
├── public/
│   └── videos/          # Sign language video files
│       ├── alphabet/    
│       ├── numbers/     
│       ├── colors/      
│       └── greetings/   
├── server/
│   ├── index.js         # Express server
│   └── python/          # Python ML model
└── src/                 # React frontend
```

## Development

- Frontend runs on: http://localhost:5173
- Backend runs on: http://localhost:3001

## Adding New Signs

1. Place video files in the appropriate directory under `public/videos/`
2. Update the signs data in `src/data/signs.ts`

## Troubleshooting

- If the webcam doesn't work, ensure you've granted browser permissions
- If Python errors occur, verify all dependencies are installed
- For backend connection issues, check if both servers are running