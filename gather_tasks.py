import asyncio

async def fetch_data(data):
    print("Start fetching data")
    await asyncio.sleep(2)
    print("Done fetching data")
    return {'data': data}
    
async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
    )
    
    for result in results:
        print(result)

asyncio.run(main())