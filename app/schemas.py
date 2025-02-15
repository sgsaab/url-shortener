from pydantic import BaseModel, HttpUrl, ConfigDict

class URLBase(BaseModel):
    """Base URL model with original URL."""
    model_config = ConfigDict(from_attributes=True)
    original_url: HttpUrl

class URLCreate(URLBase):
    """URL creation model."""
    pass

class URLResponse(URLBase):
    """Response model with all URL fields."""
    id: int
    short_url: str
    clicks: int
