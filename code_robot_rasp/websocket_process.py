import websockets
import asyncio
import multiprocessing
import json
import logging
import socket
import time


class WebSocketProcess(multiprocessing.Process):
    def __init__(self, mpid, pipe, ip, port):
        multiprocessing.Process.__init__(self)
        self.logger = logging.getLogger(__name__)
        # Process ID
        self.mpid = mpid
        # Communication port to allow for communication with other WebSocketProcess
        self.pipe = pipe
        # WebSocket port (e.g. 5555)
        self.port = port
        # Bind to specified IP address, if provided, otherwise bind to any address
        self.ip = ip
        # Get nice name (e.g. "SensorStream")
        self.name = self.__class__.__name__

    def run(self):

        
        # Start the WebSocket server, run the main() function
        
        try:
            # task1 = asyncio.get_event_loop().create_task(self.awaiting())
            
            self.proc = multiprocessing.Process(target=self.server)
            self.proc.daemon = True
            
            self.logger.info("Starting " + self.name + " process at " + str(self.ip) + ":" + str(self.port))
            
            if self.port == 5556:
                time.sleep(1)

            self.proc.start()
            
            #asyncio.run(self.awaiting())
            self.proc.join()
        except multiprocessing.ProcessError:
            self.terminate()
            #task1.cancel()
            self.logger.info("Exiting " + self.name + " process")
        
    async def awaiting(self):
        pass