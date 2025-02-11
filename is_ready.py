import weaviate

client = weaviate.connect_to_local(port=8085)

print(client.is_ready()) 

client.close()