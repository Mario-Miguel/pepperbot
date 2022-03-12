import pandas as pd

class Trial():
    def __init__(self, targetLocation, participant, ai, numbersToDisplay):
        self.targetLocation= targetLocation
        self.participant = participant
        self.ai = ai
        self.numbersToDisplay = numbersToDisplay
    
    def toString(self):
        return "{} - {} - {} - {}".format(
            self.targetLocation, self.participant, self.ai, len(self.numbersToDisplay)
        )


def load_init():
    file = pd.read_csv('data/INIT/SimAgent_INI_HeadConstrained_ALL.csv')
    trajectoryName = file["PlaybackID"]
    targetLocation = file["TargetLocation"]
    participant = file["Participant"]
    ai = file["AI"]
    size = len(trajectoryName)
    
    trials = []
    for i in range (size):
        numbersToDisplay = __load_trajectories(trajectoryName[i])
        trials.append(Trial(targetLocation[i], participant[i], ai[i], numbersToDisplay))
    
    return trials
    
        

def __load_trajectories(fileName):
    filepath = "data/Trajectories/{}".format(fileName)
    file = pd.read_csv(filepath)
    numbers = file[["B1_Val_A","B2_Val_A","B3_Val_A"]]
    return numbers
