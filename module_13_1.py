import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    p = 10 - power
    c = 1
    while c != 6:
        if c == 5:
            print(f'Силач {name} поднял {c}')
            print(f'Силач {name} закончил соревнования.')
            break
        else:
            await asyncio.sleep(p)
            print(f'Силач {name} поднял {c}')
            c += 1


async def start_tournament():
    start = asyncio.create_task(start_strongman('Pasha', 3))
    start_2 = asyncio.create_task(start_strongman('Denis', 4))
    start_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await start
    await start_2
    await start_3


asyncio.run(start_tournament())

