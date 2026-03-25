from requests import Session

class TronaldDump:
    def __init__(self) -> None:
        self.api = "https://api.tronalddump.io"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }

    def _get(self, endpoint: str) -> dict:
        return self.session.get(f"{self.api}{endpoint}").json()

    def get_tag_by_value(self, value: str) -> dict:
        return self._get(f"/tag/{value}")

    def get_all_tags(self) -> dict:
        return self._get("/tag")

    def get_quotes_by_id(self, quote_id: str) -> dict:
        return self._get(f"/quote-source/{quote_id}")

    def get_author_by_id(self, author_id: str) -> dict:
        return self._get(f"/author/{author_id}")

    def search_quote(self, query: str, page: int) -> dict:
        return self._get(f"/search/quote?query={query}&page={page}")

    def get_quote_by_id(self, quote_id: str) -> dict:
        return self._get(f"/quote/{quote_id}")

    def get_random_meme(self) -> dict:
        return self._get("/random/meme")

    def get_random_quote(self) -> dict:
        return self._get("/random/quote")
