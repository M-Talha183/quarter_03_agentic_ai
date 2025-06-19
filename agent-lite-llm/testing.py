import asyncio

async def first():
    print("1")
    await asyncio.sleep(5)
    print("1: 3.2")
    
    
async def second():
    print("2")
    
    await asyncio.sleep(3)
    print("2: 3.6")
    
print("over all 3.4")

async def main():
    await asyncio.gather(
        first(),
        second()
    )
    
asyncio.run(main())