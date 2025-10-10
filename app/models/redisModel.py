from pydantic import BaseModel, AnyUrl
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    sender: str        # "AI" or "Human"
    text: str

class RedisModel(BaseModel):
    url: AnyUrl
    uslSummery: Optional[str] = None
    conversation: Optional[List[Message]]=None
    embedding: Optional[List[float]]=None