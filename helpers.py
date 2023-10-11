def getRecepieFormated(item):
    # printItemInJson = json.dumps(item, indent=4, sort_keys=True)
    # print(printItemInJson)
    return {
        "title": item['properties']['Name']['title'][0]['plain_text'],
        "link": item['url'],
        "id": item['id'],
    }