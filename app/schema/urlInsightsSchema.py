from pydantic import BaseModel, AnyUrl
from typing import List


class UrlIn(BaseModel):
    url: AnyUrl


class UrlSummeryOut(BaseModel):
    contentSummery: str

