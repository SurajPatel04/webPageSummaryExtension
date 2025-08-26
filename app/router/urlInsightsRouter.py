from fastapi import APIRouter
from fastapi import HTTPException, status
from app.schema.urlInsightsSchema import UrlIn, UrlSummeryOut
from app.services.webContentSummary import pageContentSummary


router = APIRouter(
    prefix="/urlSummary"
)

@router.post("/", status_code=status.HTTP_200_OK)
async def summeryGenerator(url: UrlIn):

    return pageContentSummary(url.url)