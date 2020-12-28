import pandas as pd

def computeStochasticDFG(dfg):
    activities = list(dict.fromkeys([a for a,b in dfg.keys()] + [b for a,b in dfg.keys()]))
    df = pd.DataFrame.from_dict([[a, b, dfg[(a,b)]] for a,b in dfg.keys()])
    df = df.rename(columns={0:'from', 1: 'to', 2:'value'})
    dfgroup = df.groupby(['from'])['value'].sum().reset_index()
    dfr = pd.DataFrame(columns=df.columns)
    for idx, row in df.iterrows():
        total = dfgroup[dfgroup['from']==row['from']][['value']].iloc(0)[0][0]
        new_row = pd.DataFrame({'from':[row['from']], 'to':[row['to']], 'value':[int(row['value'])/int(total)]})
        dfr = dfr.append(new_row)
    res = {}
    for idx, row in dfr.iterrows():
        res[(row['from'],row['to'])] = round(row['value'],2)
    return res

def compareStochasticDFGs(dfg1, dfg2, threshold):
    dic1 = dfg1
    dic2 = dfg2

    df = pd.DataFrame.from_dict([(a,b, dic1[(a,b)]) for a,b in dic1.keys()] + [(a,b, -dic2[(a,b)]) for a,b in dic2.keys()])
    df = df.groupby([0,1]).sum().reset_index()
    df = df.rename(columns={0:'from', 1: 'to', 2:'value'})

    df = df.groupby(['from','to'])['value'].max().reset_index()
    
    df = df[abs(df['value'])>=threshold]
    res = {}
    for idx, row in df.iterrows():
        res[(row['from'],row['to'])] = round(row['value'],2)
    return res