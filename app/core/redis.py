import valkey
from app.models.redisModel import RedisModel
from dotenv import load_dotenv
import os

load_dotenv()

valkey_uri = os.getenv("VALKEY_URL")
redisClient = valkey.from_url(valkey_uri)

    # valkey_client.set('key', 'hello world')
    # key = valkey_client.get('key').decode('utf-8')

    # print('The value of key is:', key)
# data = RedisModel(
#     url="https://www.timesnownews.com/sports/top-coaches-see-khelo-india-water-sports-festival-as-springboard-for-global-success-article-152529784",
#     conversation=[
#         {"sender": "AI", "text": "Hello!"},
#         {"sender": "Human", "text": "Hi there!"}
#         ],
#     embedding=[12,4,1],
#     )
# client.set("12",data.model_dump_json())
# print(client.get("12").decode('utf-8'))
