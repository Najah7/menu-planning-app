from .clients import RakutenIchibaItemClient

client = RakutenIchibaItemClient()
result = client.fetch_groceries("牛乳")
print(result)

client = RakutenIchibaItemClient()
result = client.fetch_recommend_cookwares("卵焼き")
print(result)
