from dotenv import load_dotenv
from sse_starlette.sse import EventSourceResponse
from app.core.llm import llmFlash
from app.core.redis import redisClient
from app.models.redisModel import RedisModel
import os

load_dotenv()

if not os.getenv("USER_AGENT"):
    os.environ["USER_AGENT"] = "MyLangChainApp/1.0 (contact: you@example.com)"


from langchain_community.document_loaders import WebBaseLoader
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def pageContentSummary(url, key=None):
    async def streamSummary():
        link = url
        user_agent = os.getenv("USER_AGENT", "MyLangChainApp/1.0")
        loader = WebBaseLoader(str(link), header_template={"User-Agent": user_agent})

        doc = loader.load()
        contentDoc = doc[0].page_content

        embeddings = GoogleGenerativeAIEmbeddings(
             model="gemini-embedding-001",
             google_api_key=os.getenv("GOOGLE_API_KEY")
        )

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
        response = ""
        async for chunk in llmFlash.astream(msg):
                response+=chunk.content
                yield {"data": chunk.content}

        data = RedisModel(
            url=url,
            uslSummery=response
        )

        redisClient.set("12",data.model_dump_json())
        print(redisClient.get("12").decode("utf-8"))
    return EventSourceResponse(streamSummary())

