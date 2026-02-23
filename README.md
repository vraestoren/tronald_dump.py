# tronald_dump.py
Web-API for [tronalddump.io](https://www.tronalddump.io) web archive for the dumbest things Donald Trump has ever said

## Example
```python
from tronald_dump import TronaldDump

tronald_dump = TronaldDump()
random_quote = tronald_dump.get_random_quote()
print(random_quote)
```
