from fastapi import APIRouter
from fastapi import HTTPException, status
from app.schema import urlInsightsSchema
from app.services.webContentSummary import pageContentSummary


router = APIRouter(
    prefix="/urlSummary"
)

@router.post("/", status_code=status.HTTP_200_OK)
async def summeryGenerator(url: urlInsightsSchema.urlIn):

    return pageContentSummary(url.url)