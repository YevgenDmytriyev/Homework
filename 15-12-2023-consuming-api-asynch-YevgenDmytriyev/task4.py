import asyncio
import time
from task2_and_4 import main as async_main
from task_3_and_4 import main as sync_main

async def run_async():
    start_time = time.time()
    await async_main()  # Uncomment this line to run the async process
    end_time = time.time()
    result1 = end_time - start_time
    print(f"Asynchronous process completed in {result1} seconds")
    return result1
    
def run_sync():
    start_time = time.time()
    sync_main()
    end_time = time.time()
    result2 = end_time - start_time
    print(f"Synchronous process completed in {result2} seconds")
    return result2

async def main():
    # Run the asynchronous process and get the result
    result1 = await run_async()
    # Run the synchronous process and get the result
    result2 = run_sync()

    # Compare the results and print which one is faster
    if result1 < result2:
        print(f"The asynchronous process was faster by {result2 - result1} seconds")
    else:
        print(f"The synchronous process was faster by {result1 - result2} seconds")

if __name__ == "__main__":
    asyncio.run(main())

