import random
import string
from sqlalchemy.orm import Session
from .models import URL
from .schemas import URLCreate
from .config import get_settings
from .exceptions import URLNotFoundException

def generate_short_url():
    """Generate a short URL with 'teenie/' prefix"""
    random_chars = ''.join(random.choices(string.digits + string.ascii_lowercase, k=get_settings().SHORT_URL_LENGTH))
    return f"teenie/{random_chars}"

def create_short_url(db: Session, url_data: URLCreate):
    """Create a new shortened URL."""
    short_url = generate_short_url()
    # This while loop keeps generating urls until we get one not in the database
    while db.query(URL).filter(URL.short_url == short_url).first():
        short_url = generate_short_url()
    
    # Convert HttpUrl to string before saving
    db_url = URL(
        original_url=str(url_data.original_url),  # Convert HttpUrl to string
        short_url=short_url
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_info(db: Session, short_url: str):
    """Get URL info without incrementing click count."""
    url = db.query(URL).filter(URL.short_url == short_url).first()
    if url:
        return url
    raise URLNotFoundException(short_url)

def increment_clicks(db: Session, url: URL):
    """Increment click count for a URL."""
    url.clicks += 1
    db.commit()
    db.refresh(url)
    return url

def expand_url(db: Session, short_url: str):
    """
    Get original URL and increment click count.
    Returns the original URL string for redirection.
    """
    url = get_url_info(db, short_url)
    increment_clicks(db, url)
    return url.original_url