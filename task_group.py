import asyncio

async def fetch_data(data):
    print("Start fetching data")
    await asyncio.sleep(2)
    print("Done fetching data")
    return {'data': data}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as group:
        for i in range(3):
            tasks.append(group.create_task(fetch_data(i)))
    
    results = [task.result() for task in tasks]
    # results = [await t for t in tasks]
    print(results)
    
asyncio.run(main())