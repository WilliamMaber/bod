import asyncio
import threading
from ResourceDiscovery.main import main_ResourceDiscovery
from machine_learning.main import NN_main
from utils import asynchronous_thread_task

new_loop = asyncio.new_event_loop()
b = threading.Thread(target=asynchronous_thread_task, args=(NN_main, new_loop))
b.start()
new_loop = asyncio.new_event_loop()
a = threading.Thread(target=asynchronous_thread_task,
                     args=(main_ResourceDiscovery, new_loop))
a.start()
a.join()
b.join()
