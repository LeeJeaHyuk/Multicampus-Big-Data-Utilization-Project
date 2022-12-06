1. [preprocessing04](https://github.com/LeeJeaHyuk/MulcamProject02/blob/master/leejeahyuk/spacetitanic/preprocessing04.ipynb)

   1. 훈련에 사용할 범주형 데이터 모두 수치형으로 변환
      1. HomePlanet
         1. {'Earth':0,'Europa':1,'Mars':2} 로 매핑
      2. Destination
         1. {'55 Cancri e':0,'PSO J318.5-22':1,'TRAPPIST-1e':2} 로 매핑
      3. Cabin
         1. null값 모두 제거
            1. get_dummies(dummy_na=False)를 사용하면 자동으로 null값을 채워준다
            2. get_dummies(dummy_na=True)를 사용하면 null값만 존재하는 열을 추가하는데 훈련시에 필요하지 않은 열이므로 사용하지 않는다
            3. XGBoostRegressor를 사용한 예측은 정확도가 너무 낮게 나왔음으로 사용하지 않음
         2. Cabin,Cabin_num,Cabin_port 로 분할
            1. /를 제거해서 3개로 열을 분할한다
            2. 가장 첫번째 열은 get_dummies를 사용해서 Cabin_A ... Cabin T까지 분할한다
            3. get_dummies를 사용하면 열이 뒤에 붙으므로 각 컬럼을 적당히 슬라이싱하여 열 위치를 바꾸어 준다
            4. astype을 사용해 훈련할 모든 컬럼을 전부 float형으로 바꾸어서 훈련
         3. CryoSleep,VIP,Transported
            1. True / False 의 경우에 {'False':0,'True':1}로 매핑

2. [preprocessing05_XGBClassifier_def](https://github.com/LeeJeaHyuk/MulcamProject02/blob/master/leejeahyuk/spacetitanic/preprocessing05_XGBClassifier_def.ipynb)

   1. fillnullclassifier 함수
      1. column_name을 받아서 그 컬럼 이름의 null값을 XGBClassifier를 통해 예측한다
      2. 해당 컬럼의 null값이 채워진 dataframe을 리턴

3. [preprocessing03_XGBRegressor_def02](https://github.com/LeeJeaHyuk/MulcamProject02/blob/master/leejeahyuk/spacetitanic/preprocessing03_XGBRegressor_def02.ipynb)

   1. fillnull 함수
      1. column_name을 받아서 그 컬럼 이름의 null값을 XGBRegressor를 통해 예측한다
      2. 해당 컬럼의 null값이 채워진 dataframe을 리턴

4. [preprocessing06_age](https://github.com/LeeJeaHyuk/MulcamProject02/blob/master/leejeahyuk/spacetitanic/preprocessing06_age.ipynb)

   1. Age의 정확도가 낮게 나와서 Age이상치를 확인하고 이상치를 제거한 값의 중앙값으로 null값을 채운다

   







