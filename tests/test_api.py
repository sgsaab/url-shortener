import pytest
from fastapi.testclient import TestClient

def test_url_shortening_flow(client):
    """Test complete URL shortening flow."""
    # Create shortened URL
    response = client.post(
        "/shorten/",
        json={"original_url": "https://example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["short_url"].startswith("teenie/")
    assert data["clicks"] == 0
    
    # Get the short code
    short_code = data["short_url"].split('/')[-1]
    
    # Test redirection
    redirect_response = client.get(f"/teenie/{short_code}", follow_redirects=False)
    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"].rstrip('/') == "https://example.com"
    
    # Verify click was counted
    stats_response = client.get(f"/analytics/?shortened={short_code}")
    assert stats_response.json()["clicks"] == 1

def test_invalid_url(client):
    """Test error handling for invalid URLs."""
    response = client.post(
        "/shorten/",
        json={"original_url": "not-a-url"}
    )
    assert response.status_code == 422

def test_nonexistent_url(client):
    """Test error handling for nonexistent shortened URLs."""
    response = client.get("/teenie/nonexistent")
    assert response.status_code == 404

def test_get_url_analytics(client):
    """Test getting URL info and click count."""
    # First create a URL
    create_response = client.post(
        "/shorten/",
        json={"original_url": "https://example.com"}
    )
    short_code = create_response.json()["short_url"].split('/')[-1]
    
    # Get URL info
    response = client.get(f"/analytics/?shortened={short_code}")
    assert response.status_code == 200
    data = response.json()
    assert data["original_url"].rstrip('/') == "https://example.com"
    assert data["clicks"] == 0  # Should be 0 since we're just getting info

def test_click_counter(client):
    """Test that click counter increments correctly."""
    # Create a URL
    create_response = client.post(
        "/shorten/",
        json={"original_url": "https://example.com"}
    )
    short_code = create_response.json()["short_url"].split('/')[-1]
    
    # Get info shouldn't increment counter
    info_response = client.get(f"/analytics/?shortened={short_code}")
    assert info_response.json()["clicks"] == 0
    
    # Access URL multiple times should increment counter
    for _ in range(3):
        client.get(f"/teenie/{short_code}")
    
    # Check the click count
    info_response = client.get(f"/analytics/?shortened={short_code}")
    assert info_response.json()["clicks"] == 3  # Only expansion requests count

def test_get_nonexistent_url(client):
    """Test accessing a nonexistent shortened URL."""
    response = client.get("/analytics/?shortened=nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "URL not found: teenie/nonexistent"

def test_url_expansion(client):
    """Test URL expansion and redirection."""
    # First create a URL
    create_response = client.post(
        "/shorten/",
        json={"original_url": "https://example.com"}
    )
    short_code = create_response.json()["short_url"].split('/')[-1]
    
    # Try expanding it
    response = client.get(f"/teenie/{short_code}", follow_redirects=False)
    assert response.status_code == 307  # Temporary redirect
    assert response.headers["location"].rstrip('/') == "https://example.com"  # Remove trailing slash