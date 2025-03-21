import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    await asyncio.sleep(1)
    print(f"Future Result is set to {value}")

async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    
    asyncio.create_task(set_future_result(future, "Future Result is ready"))
    
    result = await future
    print(f"Got the future value {result}")
    
asyncio.run(main())