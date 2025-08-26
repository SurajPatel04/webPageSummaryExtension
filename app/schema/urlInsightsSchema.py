from pydantic import BaseModel, AnyUrl


class urlIn(BaseModel):
    url: AnyUrl


class urlSummeryOut(BaseModel):
    contentSummery: str