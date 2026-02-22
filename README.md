# City Facts FastAPI Application

A FastAPI web application that provides random facts about major cities from around the world and Pakistan.

## Features

- 🌍 **20 Cities Covered**: 10 major world cities + 10 Pakistani cities
- 🎲 **Random Facts**: Each city has 10 unique facts, one randomly selected each time
- 🖥️ **Web Interface**: Beautiful, responsive web UI for easy city selection
- 🚀 **REST API**: Full API endpoints for programmatic access
- 📱 **Mobile Friendly**: Responsive design works on all devices

## Cities Included

### 🌍 World Cities
- Tokyo, Japan
- New York, USA  
- London, UK
- Paris, France
- Rome, Italy
- Sydney, Australia
- Dubai, UAE
- Singapore
- Moscow, Russia
- Cairo, Egypt

### 🇵🇰 Pakistan Cities
- Karachi
- Lahore
- Islamabad
- Rawalpindi
- Faisalabad
- Multan
- Peshawar
- Quetta
- Sialkot
- Gujranwala

## Installation & Setup

1. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access the application:**
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## API Endpoints

### GET `/`
Returns the main web interface for city selection.

### GET `/cities`
Returns a list of all available cities.

**Response:**
```json
[
  "Tokyo",
  "New York",
  "London",
  ...
]
```

### GET `/city/{city_name}/fact`
Returns a random fact about the specified city.

**Example:** `/city/Tokyo/fact`

**Response:**
```json
{
  "city": "Tokyo",
  "fact": "Tokyo is the most populous metropolitan area in the world with over 37 million people.",
  "total_facts": 10
}
```

### GET `/city/{city_name}/facts`
Returns all facts about the specified city.

**Example:** `/city/Karachi/facts`

**Response:**
```json
{
  "city": "Karachi",
  "facts": [
    "Karachi is Pakistan's largest city and commercial capital with over 15 million people.",
    "The city was the first capital of Pakistan from 1947 to 1958.",
    ...
  ],
  "total_facts": 10
}
```

## Usage Examples

### Web Interface
1. Open http://localhost:8000 in your browser
2. Select a city from the dropdown menu
3. Click "Get Random Fact!" to see a random fact about that city

### API Usage (with curl)
```bash
# Get all cities
curl http://localhost:8000/cities

# Get a random fact about Tokyo
curl http://localhost:8000/city/Tokyo/fact

# Get all facts about Lahore
curl http://localhost:8000/city/Lahore/facts
```

### API Usage (with Python requests)
```python
import requests

# Get a random fact
response = requests.get("http://localhost:8000/city/Dubai/fact")
fact_data = response.json()
print(f"Did you know? {fact_data['fact']}")
```

## Project Structure

```
├── main.py              # FastAPI application with routes and web interface
├── cities_data.py       # Database of city facts (10 facts per city)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Server**: Uvicorn ASGI server
- **Data**: In-memory Python dictionary (easily expandable)

## Features in Detail

- **Random Selection**: Each API call returns a different random fact
- **Case-Insensitive**: City names work regardless of capitalization
- **Error Handling**: Proper HTTP status codes and error messages
- **Documentation**: Auto-generated API docs at `/docs`
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Fast Performance**: In-memory data for quick responses

## Future Enhancements

- Add more cities and facts
- Database integration (PostgreSQL/MongoDB)
- User favorites and history
- Images for each city
- Multi-language support
- Caching for improved performance

## Contributing

Feel free to add more cities or facts by editing the `cities_data.py` file. Each city should have exactly 10 interesting and factual statements.