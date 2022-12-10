import pandas as pd
from datetime import datetime
import os

def reportTocsv(data_name, scaler, model_name, report):
    now = datetime.now()
    # 폴더가 없으면 생성 있으면 통과
    try:
        if not os.path.exists('modeldata'):
            os.makedirs('modeldata')
    except OSError:
        print ('Error: Creating directory. modeldata')
    
    # 파일 경로
    file_path = './modeldata/' + data_name + 'report.csv'
    # 시간 불러오기
    date =  now.strftime('%Y-%m-%d %H:%M:%S')
    
    #리스트 파일 만들기
    date_list = []    
    name_list = []
    scaler_list = []
    for i in range(5):
        name_list.append(model_name)
        scaler_list.append(scaler)
        date_list.append(date)
        df = pd.DataFrame(report).transpose()
        df = df.reset_index().rename(columns={"index": "report"})    
    
    # 파일이 없으면 생성 있으면 불러오기
    if os.path.isfile('./modeldata/' + data_name + 'report.csv'): # 파일 존재
        df_exist = pd.read_csv(file_path)
        df_new = pd.concat([pd.Series(date_list),pd.Series(name_list),pd.Series(scaler_list),df], axis=1).rename(columns={0:"datetime", 1:"model_name", 2:"scaler"})
        df = pd.concat([df_exist,df_new],axis=0)
        df.to_csv(file_path, index=False)
        
    else: # 파일 존재하지 않음       
        df = pd.concat([pd.Series(date_list),pd.Series(name_list),pd.Series(scaler_list),df], axis=1).rename(columns={0:"datetime", 1:"model_name", 2:"scaler"})
        df.to_csv(file_path, index=False)