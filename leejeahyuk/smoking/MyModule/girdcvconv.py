import pandas as pd
from datetime import datetime
import os
# os.makedirs(os.path.join(self.opt.ckpt_root, self.opt.data_name), exist_ok=True)
            
def paramsTocsv(data_name, scaler, model_name, best_params, best_score):
    now = datetime.now()
    # 폴더가 없으면 생성 있으면 통과
    try:
        if not os.path.exists('modeldata'):
            os.makedirs('modeldata')
    except OSError:
        print ('Error: Creating directory. modeldata')
    
    # 파일 경로
    file_path = './modeldata/' + data_name + '.csv'
    # 시간 불러오기
    date =  now.strftime('%Y-%m-%d %H:%M:%S')
    
    # 파일이 없으면 생성 있으면 불러오기
    if os.path.isfile('./modeldata/' + data_name + '.csv'): # 파일 존재
        df_exist = pd.read_csv(file_path)
        df_nonparam = pd.DataFrame([{'date':date,'model_name':model_name,'scaler':scaler,'best_score':best_score}]) #시간 + score 데이터
        new_param=pd.DataFrame([best_params])
        
        df_new = pd.concat([df_nonparam,new_param],axis=1)
        df = pd.concat([df_exist,df_new],axis=0)
        df.to_csv(file_path, index=False)
        
    else: # 파일 존재하지 않음
        df_nonparam = pd.DataFrame([{'date':date,'model_name':model_name,'scaler':scaler,'best_score':best_score}]) #시간 + score 데이터
        df_param=pd.DataFrame([best_params])
        df = pd.concat([df_nonparam,df_param],axis=1)
        df.to_csv(file_path, index=False)

        
        