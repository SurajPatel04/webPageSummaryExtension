from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llmFlash = ChatGoogleGenerativeAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.5-flash",
)