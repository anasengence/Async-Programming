import asyncio

async def fetch_data(data):
    print("Start fetching data")
    await asyncio.sleep(2)
    print("Done fetching data")
    return {'data': data}
    
async def main():
    task1 = asyncio.create_task(fetch_data(2))
    task2 = asyncio.create_task(fetch_data(3))
    task3 = asyncio.create_task(fetch_data(4))

    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1, result2, result3)

asyncio.run(main())