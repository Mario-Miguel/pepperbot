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
    
    def isParticipantInitiator(self):
        return True if self.participant=="Initiator" else False


# Loads data stored in data/INIT . 
# It can be modified to load data from other files instead of only the one hardcoded
def load_init():
    file = pd.read_csv('data/INIT/SimAgent_INI_HeadConstrained_ALL.csv')
    trajectoryName = file["PlaybackID"]
    targetLocation = file["TargetLocation"]
    participant = file["Participant"]
    ai = file["AI"]
    size = len(trajectoryName)
    
    trials = [
        Trial(
            targetLocation[i], 
            participant[i], 
            ai[i], 
            __load_trajectories(trajectoryName[i])
        ) for i in range(size)
    ]

    return trials
    
        
# Extracts numbers to be displayed in each trial.
def __load_trajectories(fileName):
    filepath = "data/Trajectories/{}".format(fileName)
    file = pd.read_csv(filepath)
    numbers = file[["B1_Val_A","B2_Val_A","B3_Val_A"]]
    return numbers

