# ZERROUKI & LOUNICI
import numpy as np
import matplotlib.pyplot as plt

statesName = ["Bon","mineur","majeur", "Panne"]

transName = [
        ["B-B","B-Mn","B-Mj", "B-P"],
        ["Mn-B","Mn-Mn","Mn-Mj", "Mn-P"],
        ["Mj-B","Mj-Mn","Mj-Mj", "Mj-P"],
        ["P-B","P-Mn","P-Mj", "P-P"]]
        
transMatrix = [
        [0.9, 0.06, 0.04, 0],
        [0, 0.5, 0.3, 0.2],
        [0, 0, 0.3, 0.7],
        [0, 0, 0, 1]]

def get_trans_prob(tansname: str) -> float:
    global transName
    ind = np.where(np.array(transName) == tansname)
    x = ind[0][0]
    y = ind[1][0]
    global transMatrix
    return transMatrix[x][y]

def prob_sum_valid(new_matrix):
    """
    Parameters
    ----------
    transition_matrix : 2d-array, required
        Check if the given transtion matrix is valide or not.
    Returns
    -------
    bool
        returns True if is valide else False.
    """
    if sum(transMatrix[0])+sum(transMatrix[1])+sum(transMatrix[2])+ sum(transMatrix[3]) != 4:
        return False
    else: 
        return True

if prob_sum_valid(transMatrix):
    #print('Matrix valid..')
    pass
else: 
    print('Something went wrong..!!')

def update_trans_matrix(transition_matrix=None):
    """
    Parameters
    ----------
    transition_matrix : 2d-array, required
        DESCRIPTION. The default is None.

    Returns
    -------
    Boolean.

    """
    if transition_matrix:
        if prob_sum_valid(transition_matrix):
            global transMatrix
            transMatrix = transition_matrix
            return True
        else: 
            print('Please make sure the probabilities sum up to 1 (on all the rows)')
            return False
    else:
        print('You are not specifying any param..,')
        return False
    
def apply_matrix_multiplication(transMatrix, startVector, periods=2):
    """
    Parameters
    ----------
    transition_matrix : 2d-array, required
    startVector: 1d--array, required
    periods: integer, optional
        DESCRIPTION. The default is 2 (next step).
    Returns
    -------
    1d-array.
        DESCRIPTION. the probality of all the state in the selected period
    """
    s1 = [[0.9, 0.06, 0.04, 0]]

    s=[[0.9, 0.06, 0.04, 0]]
    for i in range(periods):
       s.append(np.array(np.transpose(transMatrix)).dot(np.array(s[-1])))
    
    return np.array(s[-1])

def status_forecast(periods, start_state, low_large=True):
    current_state = start_state
    # Shall store the sequence of statesName taken. So, this only has the starting state for now.
    states_trace = [current_state]
    i = 0
    # To calculate the probability of the states_trace
    prob = 1
    while i != periods:
        if current_state == "Bon": #
            new_state = np.random.choice(transName[0], replace=True, p=transMatrix[0])
            if new_state == "B-B":
                prob = prob * get_trans_prob("B-B")
                states_trace.append("Bon")
                pass
            elif new_state == "B-Mn":
                prob = prob * get_trans_prob("B-Mn")
                current_state = "mineur"
                states_trace.append("mineur")
            elif new_state == "B-Mj":
                prob = prob * get_trans_prob("B-Mj")
                current_state = "majeur"
                states_trace.append("majeur")
            elif new_state == "B-P":
                prob = prob * get_trans_prob("B-P")
                current_state = "Panne"
                states_trace.append("Panne")       
        elif current_state == "mineur":
            new_state = np.random.choice(transName[1],replace=True,p=transMatrix[1])
            if new_state == "Mn-B":
                prob = prob * get_trans_prob("Mn-B")
                states_trace.append("Bon")
                pass
            elif new_state == "Mn-Mn":
                prob = prob * get_trans_prob("Mn-Mn")
                current_state = "mineur"
                states_trace.append("mineur")
            elif new_state == "Mn-Mj":
                prob = prob * get_trans_prob("Mn-Mj")
                current_state = "majeur"
                states_trace.append("majeur")
            elif new_state == "Mn-P":
                prob = prob * get_trans_prob("Mn-P")
                current_state = "Panne"
                states_trace.append("Panne")
        elif current_state == "majeur":
            new_state = np.random.choice(transName[2],replace=True,p=transMatrix[2])
            if new_state == "Mj-B":
                prob = prob * get_trans_prob("Mj-B")
                states_trace.append("Bon")
                pass
            elif new_state == "Mj-Mn":
                prob = prob * get_trans_prob("Mj-Mn")
                current_state = "mineur"
                states_trace.append("mineur")
            elif new_state == "Mj-Mj":
                prob = prob * get_trans_prob("Mj-Mj")
                current_state = "majeur"
                states_trace.append("majeur")
            elif new_state == "Mj-P":
                prob = prob * get_trans_prob("Mj-P")
                current_state = "Panne"
                states_trace.append("Panne")                
        elif current_state == "Panne":
            new_state = np.random.choice(transName[3],replace=True,p=transMatrix[3])
            if new_state == "P-B":
                prob = prob * get_trans_prob("P-B")
                states_trace.append("Bon")
                pass
            
            elif new_state == "P-Mn":
                prob = prob * get_trans_prob("P-Mn")
                current_state = "mineur"
                states_trace.append("mineur")
            elif new_state == "P-Mj":
                prob = prob * get_trans_prob("P-Mj")
                current_state = "majeur"
                states_trace.append("majeur")
            elif new_state == "P-P":
                prob = prob * get_trans_prob("P-P")
                current_state = "Panne"
                states_trace.append("Panne")
        i += 1  
    if low_large:
        return states_trace
    return states_trace, periods, current_state, prob
def get_prob(n_periods):
    # To save every states_trace
    historical_traces = []
    count = 0
    countBon = 0
    countMineur = 0
    countMajeur = 0
    n_periods
    start_state = 'Bon'
    end_state = 'Panne'
    
    for iterations in range(1,10000):
            historical_traces.append(status_forecast(n_periods, start_state))
    
    for smaller_list in historical_traces:
        if(smaller_list[n_periods] == end_state):
            count += 1
        if(smaller_list[n_periods] == 'Bon'):
            countBon += 1
        if(smaller_list[n_periods] == 'mineur'):
            countMineur += 1
        if(smaller_list[n_periods] == 'majeur'):
            countMajeur += 1
        
    # Sans la "loi des grands nombres"..
    states_trace, periods, current_state, prob = status_forecast(n_periods, start_state, False)
    print(f'---------\nétats possibles: {states_trace}')
    print(f'état après {n_periods} périodes: {current_state}')
    print(f"Probabilité de la séquence d'états possible: {round(prob*100, 1)}%\n---------")
    
    # Avec la "loi des grands nombres"..
    percentage = round((count/10000) * 100, 1)
    percentageBon = round((countBon/10000) * 100, 1)
    percentageMineur = round((countMineur/10000) * 100, 1)
    percentageMajeur = round((countMajeur/10000) * 100, 1)
    print(f"La probabilité de commencer à l'état: {start_state} et terminer à l'état: {end_state}= {percentage}% ({n_periods}-p)")
    return percentage, percentageBon, percentageMineur, percentageMajeur

percentPanne = []
percentBon = []
percentMineur = []
percentMajeur = []
for i in range(1, 20):
    pPanne, pBon, pMineur, pMajeur = get_prob(i)
    percentPanne.append(pPanne)
    percentBon.append(pBon)
    percentMineur.append(pMineur)
    percentMajeur.append(pMajeur)
    
#Plot a line graph
plt.plot(percentPanne, label='Panne')
plt.plot(percentBon, label='Bon')
plt.plot(percentMineur, label='Defaut mineur')
plt.plot(percentMajeur, label='Defaut majeur')
 
# Add labels and title
plt.xlabel("Periodes")
plt.ylabel("probabilité")
 
plt.legend()
plt.show()


    