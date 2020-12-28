import pandas as pd

def computeDFG(df, caseIDColumn, taskIDColumn, orderColumn):
    df['Order']=df.groupby(caseIDColumn)[taskIDColumn].transform(lambda x : pd.factorize(x)[0]+1)
    df['PreOrder'] = df['Order']-1
    df = df.merge(df, how='left', left_on=[caseIDColumn, 'Order'], right_on=[caseIDColumn, 'PreOrder'])
    df = df[[taskIDColumn+'_x', taskIDColumn+'_y']]
    df = df.dropna()
    
    dfg = {}
    for idx, row in df.iterrows():
        if (row[0], row[1]) in dfg.keys():
            dfg[(row[0], row[1])] += 1
        else:
            dfg[(row[0], row[1])] = 1
    
    return dfg