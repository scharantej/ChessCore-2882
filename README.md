## Flask Application Design

### HTML Files

**1. Main HTML File (index.html)**
- Houses the entire chess board interface.
- Contains the necessary JavaScript code to handle chess game logic and user interactions.

### Routes

**1. Main Route (/)**
- Renders the main HTML file (index.html), which contains the chess board interface.
- URL: https://yourdomain.com/

**2. API Route to Handle Chess Moves (/api/move)**
- Receives POST requests with move data from the client-side JavaScript code.
- Processes the move and updates the board state on the server-side.
- Returns the updated board state as a JSON response.
- URL: https://yourdomain.com/api/move