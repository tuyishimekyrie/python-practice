import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1990},
#     {"id": 3, "title": "Total Recall", "year": 1990},
#     {"id": 4, "title": "True Lies", "year": 1994}
# ]

# data = json.dumps(movies);
# Path("movies.json").write_text(data);

data = Path("movies.json").read_text();
movies = json.loads(data);
print(movies);