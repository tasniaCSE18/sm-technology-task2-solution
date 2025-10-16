# E-Commerce Chatbot REST API

A fully functional chatbot REST API built with FastAPI that provides human-like answers about product details using Groq LLM and DummyJSON Products API.

## Features

- AI-powered chatbot using Groq LLM (llama-3.1-70b-versatile)
- Product information from DummyJSON API
- Natural language understanding and responses
- Smart product search and filtering
- RESTful API design
- Interactive API documentation (Swagger UI)

## Project Structure

```
server/
 ├── app/
 │    ├── api/
 │    │    ├── __init__.py
 │    │    ├── routes_chatbot.py
 │    ├── core/
 │    │    ├── __init__.py
 │    │    ├── config.py
 │    ├── services/
 │    │    ├── __init__.py
 │    │    ├── chatbot_service.py
 │    │    ├── product_service.py
 │    ├── models/
 │    │    ├── __init__.py
 │    │    ├── schemas.py
 │    ├── utils/
 │    │    ├── __init__.py
 │    │    ├── groq_client.py
 │    ├── main.py
 ├── requirements.txt
 ├── .env.example
 ├── README.md
```

## Prerequisites

- Python 3.8 or higher
- Groq API key (get it for free from [Groq Console](https://console.groq.com))

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd server
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 5. Create __init__.py Files

Create empty `__init__.py` files in each package directory:

```bash
# On Windows
type nul > app\__init__.py
type nul > app\api\__init__.py
type nul > app\core\__init__.py
type nul > app\services\__init__.py
type nul > app\models\__init__.py
type nul > app\utils\__init__.py

# On macOS/Linux
touch app/__init__.py
touch app/api/__init__.py
touch app/core/__init__.py
touch app/services/__init__.py
touch app/models/__init__.py
touch app/utils/__init__.py
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

## API Endpoints

### 1. Get All Products

```http
GET /api/products
```

**Response:**
```json
{
  "total": 100,
  "products": [...]
}
```

### 2. Chat with Chatbot

```http
POST /api/chat
```

**Request Body:**
```json
{
  "message": "Tell me about Kiwi"
}
```

**Response:**
```json
{
  "response": "Kiwi is a nutrient-rich fruit priced at $2.49..."
}
```

## Example Queries

The chatbot can handle various types of queries:

1. **Specific Product Information:**
   - "Tell me about Kiwi"
   - "What is the price of mango?"
   - "Show me details about iPhone"

2. **Category Queries:**
   - "Do you have any electronics?"
   - "Show me furniture products"

3. **Rating Queries:**
   - "Show me products with ratings above 4"
   - "What products have high ratings?"

4. **General Queries:**
   - "What products do you have?"
   - "Help me find a good laptop"

## Testing the API

### Using Swagger UI

1. Navigate to `http://localhost:8000/docs`
2. Try the endpoints interactively
3. See request/response examples

### Using cURL

```bash
# Get all products
curl http://localhost:8000/api/products

# Chat with bot
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about Kiwi"}'
```

### Using Python Requests

```python
import requests

# Chat endpoint
response = requests.post(
    "http://localhost:8000/api/chat",
    json={"message": "What is the price of iPhone?"}
)
print(response.json())
```

## How It Works

1. **User sends a message** via POST /api/chat
2. **Chatbot Service** analyzes the message to understand intent
3. **Product Service** fetches relevant product data from DummyJSON API
4. **Groq LLM** generates a natural, human-like response
5. **Response** is returned to the user

## Key Features

### RAG-Style Reasoning
- Identifies product mentions in queries
- Retrieves relevant data from DummyJSON
- Constructs context-aware responses

### Natural Language Processing
- Understands various query formats
- Extracts product names and categories
- Handles price, rating, and review queries

### Modular Architecture
- Clean separation of concerns
- Reusable service layer
- Easy to extend and maintain

## Technologies Used

- **FastAPI**: Modern, fast web framework
- **Groq LLM**: AI model for natural language generation
- **httpx**: Async HTTP client for API calls
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server

## Troubleshooting

### Issue: ModuleNotFoundError

**Solution:** Make sure all `__init__.py` files are created in the package directories.

### Issue: Groq API Error

**Solution:** Verify your API key is correct in the `.env` file.

### Issue: Port Already in Use

**Solution:** Use a different port:
```bash
uvicorn app.main:app --reload --port 8001
```

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License