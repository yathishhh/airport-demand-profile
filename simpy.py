import simpy
import random
import statistics
import matplotlib.pyplot as plt
import pandas as pb


def myround(x, base=30):
    return base * round(x/base)
class Airport(object):
    def __init__(self,env,numBaggageCounter):
        self.env=env
        self.bgctr=simpy.Resource(env,numBaggageCounter)
    def immigration_counter(self,passenger):
        yield self.env.timeout(random.randint(1,7))
        
def baggage_counter(self,passenger):
        yield self.env.timeout(random.randint(1,10))
	def customs(self,passenger):
        yield self.env.timeout(random.randint(1,12))
      def security_check(self,passenger):
        yield self.env.timeout(random.randint(w1,3))




def incrementkey(a):
    if a in graph.keys():
        graph[a]+=1
    else:
        graph[a]=1
       
def go_to_Airport(env,airport,passenger):
    arrival_time=env.now
    waitimes=[]
    with airport.bgctr.request() as request:
        yield request
        yield env.process(airport.immigration_counter(passenger))
        yield env.process(airport.baggage_counter(passenger))
        yield env.process(airport.customs(passenger))
        yield env.process(airport.security_check(passenger))






    waittimes.append(env.now-arrival_time)
   
    incrementkey(str(myround(env.now)))
   
       
def goAirport(env,numBaggageCounters):
    curr_airport=Airport(env,numBaggageCounters)
   
#     for i in range(3):
#         env.process(go_to_Airport(env,curr_airport,i))
       
    i = 0
    while(True):
        no_per_30=fin[i]
        for j in range(no_per_30):
            env.process(go_to_Airport(env,curr_airport,j))


        i+=30
        yield env.timeout(30)
       
    yield env.timeout(0)
       
def calculate_wait_time(wait_times):
    average_wait = statistics.mean(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def main():
   
    num_baggagecounters=2000
    random.seed(42)
    env = simpy.Environment()
    env.process(goAirport(env, num_baggagecounters))
    env.run(until=1500)
   
    mins, secs =calculate_wait_time(waittimes)
    print(
      "Running simulation...",
      f"\nThe average wait time is {mins} minutes and {secs} seconds.",
     )
waittimes=[]




graph={}
if __name__ == '__main__':
    main()


plt.plot(graph.keys(),graph.values())
plt.title("No Of Passengers VS 30 min Time Interval")
plt.xlabel("Time(30)")
plt.ylabel("No of Passergers")
plt.show()
