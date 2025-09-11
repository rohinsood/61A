def play_machine(machine_id):
    ''' result of playing the machine corresponding to machine_id
    Parameters
    ----------
    machine_id : int
        the id of the slot machine (ex: 1 is machine 1)
 
    Returns
    -------
    outcome: int
        the outcome of playing this machine. 1 if success and 0 otherwise 
    '''
 
def update_rule(machine_id, outcome):
    ''' get the updated probability for this machine given an outcome
 
    Parameters
    ----------
    machine_id : int
        the id of the slot machine (ex: 1 is machine 1)
 
    outcome : int
        the outcome produced by this machine
 
    Returns
    -------
    new_estimate : float
        our updated success probability estimate for this machine
    '''
 
def get_best_machine(estimates):
    ''' returns the id of the machine with the highest estimated success rate 
 
    Parameters
        ----------
        estimates : list
            the success probability estimates for the slot machines. [0.5, 0.9, 0.1] 
            means that machine 0 has success prob 0.5, machine 1 has 0.9, and machine
            2 has 0.1.
    
        Returns
        -------
        machine_id : int
            the id of the slot machine (ex: 1 is machine 1)
    
    '''
 
def greedy(num_iterations=1000, num_machines=5):
    ''' return the best machine after running the greedy algorithm num_iterations 
            times. Success probability estimates for all machines are initialized 
            to 0.5.
    
    Parameters
    ----------
    num_iterations: int
        the number of iterations to run the greedy algorithm
    num_machines: int
        the number of slot machines we have
    
    Returns
    -------
    best_machine: int
        the machine with the highest success probability estimate after running
        the greedy algorithm num_iterations times
    
    '''
    estimates = []
    for i in range(num_machines):
        estimates.append(0.5)
    
    init_machine_id = randint(0,num_machines)
    
    init_play = play_machine()
    for i in range (num_iterations):
