import os
from notion_client import Client
from pprint import pprint

notion = Client(auth=os.environ.get("NOTION_TOKEN"))


my_page = notion.databases.query(
    **{
        "database_id": "95ad2620c6264b4ba6149b4653ef6367",
        "filter": {
            "property": "Tag",
            "multi_select": {
                "contains": "Bridge",
            },
        },
    }
)

print(1 + 1)

# 95ad2620c6264b4ba6149b4653ef6367 
# f605f973216f41839ab5ede2cfccda08