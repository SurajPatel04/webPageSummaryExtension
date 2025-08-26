from dotenv import load_dotenv
from sse_starlette.sse import EventSourceResponse
import os
import asyncio

load_dotenv()

if not os.getenv("USER_AGENT"):
    os.environ["USER_AGENT"] = "MyLangChainApp/1.0 (contact: you@example.com)"

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, ChatMessage

llm = ChatGoogleGenerativeAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    model="gemini-2.5-flash",
)
def pageContentSummary(url):
    async def streamSummary():
        link = url
        user_agent = os.getenv("USER_AGENT", "MyLangChainApp/1.0")
        loader = WebBaseLoader(str(link), header_template={"User-Agent": user_agent})

        doc = loader.load()
        contentDoc = doc[0].page_content
        system_prompt = """You work is to tell in short what is written. you will get content and the user query based on the content give user answer
        Ouput should look like this
        AI: your response
        """

        query = f"Provide me whole content summery in points{contentDoc}"
        msg = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]

        async for chunk in llm.astream(msg):
                yield {"data": chunk.content}

    return EventSourceResponse(streamSummary())

