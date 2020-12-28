import pandas as pd
import numpy as np

def getData():

    sequence = 'sequence'
    count = 'count'

    emergency = 'emergency'

    register = 'register patient'
    read = 'read patient''s journal'
    visit = 'visit patient'
    update = 'update the journal'
    operate = 'operate patient'

    df_columns = ['caseid', 'activity', 'order', 'isEmergency']

    case_types = {
        1:  {emergency: True,  count: 2  , sequence: [register, read]},
        2:  {emergency: True,  count: 5  , sequence: [register, read, visit]},
        3:  {emergency: True,  count: 10 , sequence: [register, read, visit, update]},
        4:  {emergency: True,  count: 30 , sequence: [register, read, visit, operate, update]},
        5:  {emergency: True,  count: 15 , sequence: [register, visit]},
        6:  {emergency: True,  count: 25 , sequence: [register, visit, update]},
        7:  {emergency: True,  count: 40 , sequence: [register, visit, operate, update]},
        8:  {emergency: True,  count: 65 , sequence: [register, operate, update]},
        ###
        9:  {emergency: False, count: 1 , sequence: [register, read]},
        10: {emergency: False, count: 20, sequence: [register, read, visit]},
        11: {emergency: False, count: 50, sequence: [register, read, visit, update]},
        12: {emergency: False, count: 110, sequence: [register, visit]},
        13: {emergency: False, count: 20, sequence: [register, visit, update]},
        14: {emergency: False, count: 5, sequence: [register, visit, operate, update]},
    }

    df = pd.DataFrame(columns=df_columns)

    # creating log as df
    for k in case_types.keys():
        count_val = case_types[k][count]
        for i in range(0, count_val):
            caseid_val =  str(k) + '_' + str(i)

            emergency_val = case_types[k][emergency]

            i=0
            for a in case_types[k][sequence]:
                i+=1

                activity_val = a

                row = pd.DataFrame([[caseid_val, a, i, emergency_val]], columns=df_columns)
                df = pd.concat([df, row], ignore_index=True)    
    return df