import requests

def check_status_code(status_code: str) -> bool:
    match status_code:
        case 200: return True
        case 404: return False
        case _: return False
req = requests.get('https://api.monobank.ua/bank/currency')

currency = {
    840: '💵',
    978: '💶'
}

if req.status_code == 200:
    data = req.json()
    print(data)

for i in req.json():
        if i['currencyCodeA'] in (840, 978):
            print(f"Code is: {i['currencyCodeA']} Image: {currency[i['currencyCodeA']]} Buy: {i['rateBuy']}")
else:
    print(f'we can\'t work with currency {check_status_code(req)}')


