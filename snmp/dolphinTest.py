import pandas as pd
import numpy as np
import dolphindb as ddb

if __name__ == '__main__':
    conn=ddb.session()
    conn.connect( 'localhost', 8900)
    df = pd.DataFrame({'id': np.int32([1, 2, 3, 4, 3]), 'value':  np.double([7.8, 4.6, 5.1, 9.6, 0.1]), 'x': np.int32([5, 4, 3, 2, 1])})
    conn.upload({'t1': df})
    path="E:\\ReportData\\东港机房\\UPS\\UPS-OutputLoad_%.dat"
    USstocks = ploadText(path);
