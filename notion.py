import os
from notion_client import Client
from dotenv import load_dotenv
load_dotenv()

notion_token = os.getenv('NOTION_TOKEN')
notion_database_id = os.getenv('NOTION_DATABASE_ID')

notion = Client(auth=notion_token)

def recepiesDDBB():
    return notion.databases.query(
        **{
            "database_id": notion_database_id,
        }
    )


def get_page():
    return recepiesDDBB()


def get_page_by_id(id):
    return notion.pages.retrieve(page_id=id)