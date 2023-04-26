import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

print(main.__class__)


'''async 定义的函数在运行的时候并不会真的运行其中的内容，而是返回一个<class 'coroutine'>'''
coro = main()
print(coro.__class__)


'''
    如果需要其中的代码正常运行
    1. 我们需要进入async模式，即将code object的执行权交给event_loop，利用入口函数asyncio.run(<class 'coroutine'>)
    2. 将<class 'coroutine'>变成一个task
    
    asyncio.run()会做两件事：
    1. 建立event_loop
    2. 将coroutine变成task放进loop里，成为loop里的第一个对象
    
    await 就像一个正常的生成器一样工作
    await的时候task并不会把运行的控制权交还给loop，而是等待coroutine运行返回future
    
    直接创建task的时候create_task()会直接返回控制权，event_loop重新调用sleep()
    
    event_loop调度的最小单位是task，必须把coroutine变成task后event_loop才能运行
    
    await的东西要么是一个coroutine要么是一个task要么是一个future
    
    coroutine就是一个生成器
    task继承了future
    
    await后面是coroutine的话直接返回coroutine，不是的话就会调用.__await__()这个函数
    本质上.__await__()就是一个生成器，没有结束的话吧self yield出去，否则返回结果
'''
# asyncio.run(main())