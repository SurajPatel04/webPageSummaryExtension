from dotenv import load_dotenv
from sse_starlette.sse import EventSourceResponse
from app.core.llm import llmFlash
import os

load_dotenv()

if not os.getenv("USER_AGENT"):
    os.environ["USER_AGENT"] = "MyLangChainApp/1.0 (contact: you@example.com)"


from langchain_community.document_loaders import WebBaseLoader
from langchain_core.messages import SystemMessage, HumanMessage


def pageContentSummary(url):
    async def streamSummary():
        link = url
        user_agent = os.getenv("USER_AGENT", "MyLangChainApp/1.0")
        loader = WebBaseLoader(str(link), header_template={"User-Agent": user_agent})

        doc = loader.load()
        contentDoc = doc[0].page_content
        system_prompt = """You are an AI assistant. 
        Your task is to read the provided content and generate a clear, concise summary in **bullet points**. 
        Do not include unnecessary details. 
        Output format:

        AI:
        - Point 1
        - Point 2
        - Point 3
        """

        query = f"Provide me whole content summery in points{contentDoc}"
        msg = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]

        async for chunk in llmFlash.astream(msg):
                yield {"data": chunk.content}

    return EventSourceResponse(streamSummary())

