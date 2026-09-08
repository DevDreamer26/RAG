import chromadb

client = chromadb.PersistentClient(path='/home/anon-x/RAG/data/vector_store')

# List all collections stored in this database
collections = client.list_collections()
print("Collections found:", [c.name for c in collections])

# Inspect a specific collection's data
for col_info in collections:
  col = client.get_collection(col_info.name)
  print(f"\nData inside collection '{col_info.name}':")
  print(col.get())