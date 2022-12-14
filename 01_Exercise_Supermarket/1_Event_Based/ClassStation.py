import heapq

from ClassCustomer import Customer

class Station():
  """
  ### Class Station
  Describe a station in the supermarket. Class consists of:
    name: station name
    buffer: customer queue
    delay_per_item: service time
    CustomerWaiting, busy: possible states of this station
  """
  
  def __init__(self, delay_per_item, name):
    """
    ### Station Constructor
    Args:
      delay_per_item (int): delay per item when served
      name (str): name of the station
    """
    self.name = name
    self.buffer = []
    self.delay_per_item = delay_per_item
    self.CustomerWaiting = False
    self.busy = False


  def queue(self, customer):
    self.buffer.append(customer)
    self.CustomerWaiting = True


  def serve(self):
    self.busy = True
    customer = self.buffer.pop(0)
    if len(self.buffer) == 0:
      self.CustomerWaiting = False
    Customer.served[self.name] += 1 
    return customer

  def leave(self):
     return self.serve()


  def isBusy(self):
    return self.busy


  def isCustomerWaiting(self):
    return self.CustomerWaiting


  def __str__(self):
    return self.name