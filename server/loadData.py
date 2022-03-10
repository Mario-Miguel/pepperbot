import pandas as pd

class Trial():
    def __init__(self, targetLocation, participant, ai, numbersToDisplay):
        self.targetLocation= targetLocation
        self.participant = participant
        self.ai = ai
        self.numbersToDisplay = numbersToDisplay


def load_init():
    file = pd.read_csv('data/INIT/SimAgent_INI_HeadConstrained_ALL.csv')
    trajectoryName = file["PlaybackID"]
    targetLocation = file["TargetLocation"]
    participant = file["Participant"]
    ai = file["AI"]
    size = trajectoryName.shape
    
    trials = []
    for i in range (size):
        numbersToDisplay = load_trajectories(trajectoryName[i])
        trials.append(Trial(targetLocation[i], participant[i], ai[i], numbersToDisplay))
    
    return trials
    
        

def load_trajectories(fileName):
    filepath = "data/Trajectories/{}".format(fileName)
    file = pd.read_csv(filepath)
    numbers = file[["B1_Val_A","B2_Val_A","B3_Val_A"]]
    return numbers


load_init()