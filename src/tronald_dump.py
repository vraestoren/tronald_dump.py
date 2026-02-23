from requests import Session

class TronaldDump:
    def __init__(self) -> None:
        self.api = "https://api.tronalddump.io"
        self.session = Session()
        self.session.headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }
    
    def get_tag_by_value(self, value: str) -> dict:
        return self.session.get(
            f"{self.api}/tag/{value}").json()
    
    def get_all_tags(self) -> dict:
        return self.session.get(f"{self.api}/tag").json()
    
    def get_quotes_by_id(self, quote_id: str) -> dict:
        return self.session.get(
            f"{self.api}/quote-source/{quote_id}").json()
    
    def get_author_by_id(self, author_id: str) -> dict:
        return self.session.get(
            f"{self.api}/author/{author_id}").json()
    
    def search_quote(
            self,
            query: str,
            page: int) -> dict:
        return self.session.get(
            f"{self.api}/search/quote?query={query}&page={page}").json()
    
    def get_quote_by_id(self, quote_id: str) -> dict:
        return self.session.get(
            f"{self.api}/quote/{quote_id}").json()
    
    def get_random_meme(self) -> dict:
        return self.session.get(
            f"{self.api}/random/meme").json()
    
    def get_random_quote(self) -> dict:
        return self.session.get(
            f"{self.api}/random/quote").json()
