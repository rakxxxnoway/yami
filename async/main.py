import asyncio
import signal
import os
import time
from sys import argv

clear = lambda: os.system("cls")

async def main(argc:int, arg:list) -> None:
    #await asyncio.sleep(10, result="hello")
    print("Hello,")
    await asyncio.sleep(1)
    print("...World")

    raise signal.SIGINT


if __name__ == "__main__":
    with asyncio.Runner() as run:
        try:
            clear()
            run.run(main(len(argv), argv))
            print(run.get_loop())

        except asyncio.exceptions.CancelledError:
            pass
    
        finally:
            run.close()