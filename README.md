# <img src="https://avatars.githubusercontent.com/u/23418820?s=200&v=4" width="28" style="vertical-align:middle;" /> tronald_dump.py

> Web-API for [TronaldDump](https://tronalddump.io) a searchable archive of Trump quotes, memes, authors, and tags.

## Quick Start
```python
from tronald_dump import TronaldDump

td = TronaldDump()
print(td.get_random_quote())
```

---

## Quotes

| Method | Description |
|--------|-------------|
| `get_quote_by_id(quote_id)` | Get a quote by ID |
| `get_quotes_by_id(quote_id)` | Get a quote source by ID |
| `search_quote(query, page)` | Search quotes by keyword |
| `get_random_quote()` | Get a random quote |
| `get_random_meme()` | Get a random meme |

## Tags & Authors

| Method | Description |
|--------|-------------|
| `get_all_tags()` | Get all available tags |
| `get_tag_by_value(value)` | Get a tag by its value |
| `get_author_by_id(author_id)` | Get an author by ID |
