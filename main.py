import asyncio
import websockets as ws
import json
import time


async def main():
    url = 'wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker'
    async with ws.connect(url) as client:
        while True:
            data = json.loads(await client.recv())['data']

            time_list = time.localtime(data['E'] // 1000)
            event_time = f'{time_list.tm_hour}:{time_list.tm_min}:{time_list.tm_sec}'
            quotation = data['c']
            print(f'{event_time} ==> BTC/USDT : {quotation}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
