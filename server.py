from project.monitor import Flow
import time

flow = Flow()
while True:
    time.sleep(1)
    flow.recount()