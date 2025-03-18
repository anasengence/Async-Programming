import asyncio

async def fetch_data():
    print("Start fetching data")
    await asyncio.sleep(2)
    print("Done fetching data")
    return {'data': 1}
    
async def main():
    task1 = fetch_data()
    task2 = fetch_data()
    task3 = fetch_data()

    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1, result2, result3)

asyncio.run(main())