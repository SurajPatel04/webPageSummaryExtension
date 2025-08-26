# AI Summary Extension 🤖✨

A powerful FastAPI-based web service that generates AI-powered summaries of web pages using Google's Gemini AI model. Simply provide a URL and get a concise, bullet-point summary of the content in real-time.

## 🚀 Features

- **Smart Web Scraping**: Extracts content from any public web page
- **AI-Powered Summarization**: Uses Google Gemini 2.5 Flash model for intelligent content analysis
- **Real-time Streaming**: Server-sent events (SSE) for live summary generation
- **Clean API**: RESTful FastAPI endpoints with proper validation
- **Bullet Point Format**: Organized, easy-to-read summaries
- **Error Handling**: Robust exception handling and validation

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **LangChain**: Framework for developing applications with LLMs
- **Google Gemini AI**: Advanced language model for content summarization
- **Pydantic**: Data validation using Python type annotations
- **SSE (Server-Sent Events)**: Real-time streaming responses

## 📋 Prerequisites

- Python 3.8+
- Google AI API Key (Gemini)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SurajPatel04/webPageSummaryExtension.git
   cd AiSummeryExtension
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn langchain-google-genai langchain-community python-dotenv sse-starlette pydantic
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_ai_api_key_here
   USER_AGENT=MyLangChainApp/1.0 (contact: your@email.com)
   ```

## 🚀 Running the Application

1. **Start the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API**
   - API will be available at: `http://localhost:8000`
   - Interactive API docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

## 📡 API Endpoints

### Generate URL Summary

**POST** `/urlSummary/`

Generate a real-time summary of web page content.

**Request Body:**
```json
{
  "url": "https://example.com/article"
}
```

**Response:**
- Content-Type: `text/event-stream`
- Real-time streaming summary in bullet points

**Example Usage:**
```bash
curl -X POST "http://localhost:8000/urlSummary/" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com/article"}'
```

## 📁 Project Structure

```
AiSummeryExtension/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── core/
│   │   └── llm.py             # Google Gemini AI configuration
│   ├── exceptions/
│   │   └── schemaValidationExceptionHandler.py  # Error handling
│   ├── models/                # Data models (if any)
│   ├── router/
│   │   ├── urlInsightsRouter.py    # URL summary endpoints
│   │   └── userRouter.py           # User-related endpoints
│   ├── schema/
│   │   └── urlInsightsSchema.py    # Pydantic schemas
│   ├── services/
│   │   ├── webContentSummary.py    # Core summarization logic
│   │   └── urlQnA.py              # Q&A functionality (future)
│   └── utils/                 # Utility functions
├── main.py                    # Application launcher
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google AI API key for Gemini | Yes |
| `USER_AGENT` | User agent string for web scraping | No (has default) |

### Getting Google AI API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

## 📝 Usage Examples

### Python Client Example

```python
import requests
import json

def get_summary(url):
    response = requests.post(
        "http://localhost:8000/urlSummary/",
        json={"url": url},
        stream=True
    )
    
    for line in response.iter_lines():
        if line:
            # Parse SSE data
            data = line.decode('utf-8')
            if data.startswith('data: '):
                content = data[6:]  # Remove 'data: ' prefix
                print(content, end='', flush=True)

# Example usage
get_summary("https://example.com/article")
```

### JavaScript/Fetch Example

```javascript
async function getSummary(url) {
    const response = await fetch('http://localhost:8000/urlSummary/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url })
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        
        const text = decoder.decode(value);
        console.log(text);
    }
}
```

## 🧪 Testing

Test the API using the interactive documentation at `http://localhost:8000/docs` or with curl:

```bash
curl -X POST "http://localhost:8000/urlSummary/" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.python.org"}'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- [ ] Q&A functionality for web content
- [ ] Support for multiple AI models
- [ ] Content caching for improved performance
- [ ] Batch URL processing
- [ ] Export summaries to different formats (PDF, DOCX)
- [ ] User authentication and rate limiting
- [ ] Custom summary length options

## 📞 Support

If you have any questions or run into issues, please:

1. Check the [Issues](https://github.com/SurajPatel04/webPageSummaryExtension/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your setup and the error

## ⭐ Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [LangChain](https://langchain.com/) for LLM integration tools
- [Google AI](https://ai.google/) for the Gemini model
- The open-source community for continuous inspiration

---

**Made by [SurajPatel04](https://github.com/SurajPatel04)**
