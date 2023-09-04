#并行非流任务
def run_async_tasks(tasks, return_when="ALL_COMPLETED"):
    """
    tasks: list of asyncio.Task
    done是一个set，包含所有已经完成的task
    调用done中item的result()方法可以获取task的返回值
    如果task抛异常,result()方法会raise对应异常
    默认情况是全部结束后返回,可以支持[FIRST_COMPLETED,FIRST_EXCEPTION, ALL_COMPLETED]
    """
    #线程不安全的1oop,所以不要多线程 
    try:
        loop = asyncio.get_running_loop() 
    except:
        try:
            loop = asyncio.get_event_loop() 
        except:
            loop = asyncio.new_event_loop() 
            asyncio.set_event_loop(loop)
    done, pending = loop.run_until_complete(asyncio.wait(tasks, return_when=return_when)) 
    return done, pending