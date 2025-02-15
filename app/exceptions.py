class URLNotFoundException(Exception):
    """Exception raised when a shortened URL is not found in the database."""
    
    def __init__(self, short_url: str):
        self.short_url = short_url
        self.message = f"URL not found: {short_url}"
        super().__init__(self.message)
