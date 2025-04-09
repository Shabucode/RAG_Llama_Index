from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv
import os

# Load environment variables from .env file

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
urls = [
    "https://www.wearethemis.com/uk/",
    "https://www.wearethemis.com/uk/about/team/"
]
# 1. Load webpage
documents = SimpleWebPageReader(html_to_text=True).load_data(urls)

# 2. Build index
index = VectorStoreIndex.from_documents(documents)

# 3. Query
query_engine = index.as_query_engine()
response = query_engine.query("Tell me the names of the officers in the organisation and what are their position and who is UBO?")
print(response)
