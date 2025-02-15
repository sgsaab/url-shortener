from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse, JSONResponse
from .database import get_db, Base, engine
from .schemas import URLCreate, URLResponse
from .crud import create_short_url, get_url_info, expand_url
from .exceptions import URLNotFoundException

app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortener service that shortens URLs and tracks clicks",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.post("/shorten/", 
    response_model=URLResponse,
    summary="Create a shortened URL",
    description="Takes a long URL and returns a shortened version"
)
def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):
    """
    Create a shortened URL:
    - **url_data**: The original URL to be shortened
    Returns a shortened URL with click tracking
    """
    return create_short_url(db, url_data)

@app.get("/url/{short_code}",
    response_model=URLResponse,
    summary="Get URL info",
    description="Get information about a shortened URL including click count"
)
def get_url_stats(short_code: str, db: Session = Depends(get_db)):
    """
    Get URL information and analytics:
    - **short_code**: The shortened URL code
    Returns the URL details and click count
    """
    try:
        return get_url_info(db, f"teenie/{short_code}")
    except URLNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/teenie/{short_code}",
    summary="Expand URL",
    description="Redirects to the original URL and increments click count"
)
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    """
    Expand shortened URL and redirect:
    - **short_code**: The shortened URL code
    Redirects to the original URL
    """
    try:
        original_url = expand_url(db, f"teenie/{short_code}")
        return RedirectResponse(original_url, status_code=307)
    except URLNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/shorten")
def shorten_url_get(url: str, db: Session = Depends(get_db)):
    """
    Create a shortened URL using GET request:
    - **url**: The URL to shorten (as query parameter)
    """
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    url_data = URLCreate(original_url=url)
    return create_short_url(db, url_data)
