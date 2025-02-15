import pytest
from app.crud import generate_short_url, create_short_url, get_url_info, expand_url
from app.schemas import URLCreate
from app.exceptions import URLNotFoundException

def test_generate_short_url():
    """Test URL shortening - unique code generation."""
    url = generate_short_url()
    assert url.startswith("teenie/")
    assert len(url) == len("teenie/") + 6
    assert all(c.isalnum() or c == '/' for c in url)

def test_create_unique_urls(db):
    """Test URL shortening - uniqueness requirement."""
    # Create multiple URLs for the same target
    url_data = URLCreate(original_url="https://example.com")
    url1 = create_short_url(db, url_data)
    url2 = create_short_url(db, url_data)
    
    # Verify they're unique
    assert url1.short_url != url2.short_url
    assert url1.original_url == url2.original_url

def test_url_expansion(db):
    """Test URL expansion - retrieval of original URL."""
    # Create a short URL
    url_data = URLCreate(original_url="https://example.com")
    db_url = create_short_url(db, url_data)
    
    # Get the original URL
    original_url = expand_url(db, db_url.short_url)
    assert original_url.rstrip('/') == "https://example.com"

def test_click_tracking(db):
    """Test analytics - click counting."""
    # Create a URL
    url_data = URLCreate(original_url="https://example.com")
    db_url = create_short_url(db, url_data)
    
    # Initial count should be 0
    url_info = get_url_info(db, db_url.short_url)
    assert url_info.clicks == 0
    
    # Expand URL multiple times
    for _ in range(3):
        expand_url(db, db_url.short_url)
    
    # Verify click count
    url_info = get_url_info(db, db_url.short_url)
    assert url_info.clicks == 3

def test_get_nonexistent_url(db):
    """Test that accessing nonexistent URL raises exception."""
    with pytest.raises(URLNotFoundException):
        get_url_info(db, "teenie/nonexistent") 