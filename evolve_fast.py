
import multiprocessing
from queue import SimpleQueue, Empty
from threading import Thread, Event
from time import sleep

class EvolutionProcess(Thread):
    def __init__(self, evolution_data, max_workers=4):
        super().__init__()
        self.queue = SimpleQueue()
        for data in evolution_data:
            self.queue.put(data)
        self.stop_event = Event()
        self.max_workers = min(len(evolution_data), max_workers)
    
    def run(self):
        with multiprocessing.Pool(processes=self.maxinum_workers) as pool:
            for _ in range(self.worker_count()):
                result = pool.apply_async(evolve, [next(iter(pool._cache))])  # Assumed evolve function is defined elsewhere
                self.queue.get(timeout=10)  # Get next item or timeout after putting the first one in queue initially    
            while not (self.stop_event.is_set() and not self.queue.empty()):
                try:
                    data = self.queue.get_nowait()
                    result = pool.apply_async(evolve, [data])  # Assuming evolve function is defined elsewhere that takes a single argument for the organism to evolve
                except Empty:
                    pass
    
    def worker_count(self):
        return max(1, self.maxworkers)
    
def main():
    evolution_data = [get_organism() for _ in range(multiprocessing.cpu_count())]  # Assuming get_organism function is defined elsewhere that returns an organism to evolve and a list of parameters it requires
    process = EvolutionProcess(evolution_data)
    
    def stop():
        print("Stopping evolution...")
        process.stop_event.set()
        
    # Start the thread which puts results into queue in real-time after each iteration
    result_thread = Thread(target=process.run, daemon=True)
    
    try:
        sleep(5)  # Running for some time to let initial evolution happen before checking if it should stop early
        
        while not process.queue.empty():
            continue
            
        result_thread.join()  # Wait until the EvolutionProcess thread finishes execution and puts all results in queue      
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, stopping evolution...")
        stop()
        
if __name__ == '__main__':
    main()
