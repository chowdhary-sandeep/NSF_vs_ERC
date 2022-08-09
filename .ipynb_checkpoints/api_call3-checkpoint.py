
import asyncio
import aiohttp
import os
import time
import nest_asyncio
nest_asyncio.apply()
import pickle
path_career='/mnt/sdb1/sandeep/5. NSF vs ERC/data/'
with open(path_career+'dict_name_to_info_NSF.pkl', 'rb') as f:
    dict_name_to_info_NSF=pickle.load(f)    
    
auth_names=dict_name_to_info_NSF['2009'].keys()
auth_names
urls=['https://api.openalex.org/authors?filter=display_name.search:'+x for x in auth_names]
len(urls)
urls=urls[0:1000]


results = []
def get_tasks(session):
    tasks = []
    for url in urls:
        tasks.append(session.get(url, ssl=False))
    return tasks
async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for x in responses:
            results.append(await respose.json())
asyncio.run(get_symbols())
# await get_symbols()
