class PrivateKeysHandler:
    def __init__(self, relative_path_to_file : str):
        from configparser import RawConfigParser
        import os
        self.configParser = RawConfigParser()   
        configFilePath = os.path.join(os.path.dirname(''), relative_path_to_file) 
        self.configParser.read(configFilePath)

    def load_keys(self, section : str) -> dict:
        return self.configParser[section]

    
def dict_to_csv(author, author_dict):
    import flatdict
    import pandas as pd
    auth_dict = flatdict.FlatterDict(authors_dict)
    auth_df = pd.DataFrame(data = zip(auth_dict.keys(), auth_dict.values()),
                         columns = ['keys', 'values'])
    auth_df.to_csv('data/' + author + '.csv', index=False)
    
def csv_to_dict(author):
    import flatdict
    import pandas as pd
    df = pd.read_csv('data/' + author + '.csv')
    d = {}
    for key, value in zip(df['keys'], df['values']):
        d[key] = value
    d = flatdict.FlatterDict(d).as_dict()
    for title in d['titles']:
        d['titles'][title]['chapters'] = list(d['titles'][title]['chapters'].values())
    return d
    
def load_csv(relative_path):
    import os
    from ast import literal_eval
    from pandas import read_csv
    if os.path.isfile(relative_path):
        df = pd_read_csv(relative_path)
        if 'lemma' in df.columns.tolist():
            df['lemma'] = df.lemma.apply(lambda x: literal_eval(x))
        return df
    else:
        return 'No csv-file with that name found. Check for spelling errors.'