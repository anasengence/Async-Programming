import asyncio

async def fetch_data():
    print("Start fetching data")
    await asyncio.sleep(2)
    print("Done fetching data")
    return {'data': 1}
    
if __name__ == "__main__":
    asyncio.run(fetch_data())