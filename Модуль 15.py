import json

with open(r'https://github.com/EngiBP/-15/blob/master/json_example_QAP.json', encoding='utf8') as f:
    templates = json.load(f)


def CheckInt(item):
    return isinstance(item, int)

def CheckStr(item):
    return isinstance(item, str)

def CheckBool(item):
    return isinstance(item, bool)

def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False

def CheckValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})

ListOfItems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url',
               'remoteHost' : 'str', 'partyId': 'str', 'sessionId': 'str', 'PageViewId': 'str', 'item_Id': 'str',
               'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool',
               'detectedCorruption': 'bool','firstInSession': 'bool'}

Error = []
for item in templates:
    for item in items:
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, itens[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, itens[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not CheckDool(items[item]):
                    ErrorLog(item, itens[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, itens[item], f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'val':
                if not CheckVal(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(item, itens[item], f'ожидали тип itemBuyEvent bkb itemViewEvent}')
            else:
                ErrorLog(item, itens[item],'неожиданное значение')
        else:
            ErrorLog(item, itens[item], 'неизвестная переменная')

if Error == []:
    print('pass')
else:
    print('Fail')
    print(Error)


