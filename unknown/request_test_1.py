def read_async_generator(res):
    async def helpler(res):
        """读取流"""
        items = ""
        async for item in res:
            items += item
        return items
    return asyncio.run(helper(res))

async def read_stream_async_iter(res):
    """读取流"""
    async for item in await res:
        yield item

async def async_stream_request(url, method="GET", params=None, data=None, headers=None, timeout=10):
    async with aiohttp.ClientSession() as session:
        async with session.request(method=method, url=url, params=params, data=data, headers=headers, timeout=timeout) as response:
            async for chunk in response.content.iter_chunked(1024):
                yield chunk

# 异步请求，返回text
async def async_request(url, method="GET", params=None, data=None, headers=None, timeout=60):
    """异步请求总方法

    Args:
        url (_type_):_description_
        method (str,optional):_description_. Defaults to "GET" 
        params (_type_, optional): _description_. Defaults to Nonee,
        data (_type_, optional): _description_. Defaults to None. headers (_type_, optional): _description_. Defaults to None. 
        timeout (int,optional): _description_. Defaults to 60. 
        stream (bool, optional): _description_. Defaults to False.

    Returns:
        coroutine,
        在非async函数中可以用read_stream的方法统一读取
        在async函数中用里面的awaithelper可以读出来
        如果要流,则foriteminawaitstream:yielditem
  
    """
    async with aiohttp.ClientSession() as session:
        async with session.request(method=method, url=url, params=params,data=data, headers=headers, timeout=timeout) as response:
            return await response.text()