from pathlib import Path
from network import call_server

call_server()

print(Path("ecommerce/shopping/shop.py").parent);