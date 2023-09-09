# Kaggle CompetitionSpacetitanic

kaggle 교육용 competition data를 사용한 머신러닝 프로젝트에서 사용한 코드 모음입니다



---

## EDA

1. EDA01.ipynb
   1. 이상치 확인 (Cabin_num,Age,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck)
2. EDA03.ipynb
   1. 상관관계 확인
   2. 모든 컬럼의 transported된 비율 확인하는 코드 만들기
   3. 2번의 함수를 csv 파일에 저장하는 코드 만들기
   4. 컬럼별로 도착하지 못한 비율 확인
   5. Cabin_num를 그룹화해서 확인
3. EDA04.ipynb
   1. vip와 vip가 아닌 경우에 서비스 이용률 확인
4. EDA05.ipynb
   1. CryoSleep==1 인 경우에 돈을 사용하지 않음 확인 후 데이터 변경
   2. Age<=12 인 경우에 돈을 사용하지 않음 확인후 데이터 변경
5. EDA06.ipynb
   1. kaggle EDA 따라 해보기
   2. HomePlanet별로  Destination 확인
   3. 상관관계 깔끔하게 확인
   4. HomePlanet  Destination별 사망율 원그래프
   5. 전체 나이 그래프
   6. 죽은 사람 나이 그래프 
6. EDA07.ipynb
   1. kaggle EDA 따라 해보기2
   2. HomePlanet 별 나이 그래프
   3. Destination 별 나이 그래프
   4. 어느 행성을 도착지로 많이 선택했는지
   5. HomePlanet,Destination 별 RoomService 에 지불한 비용



---


## 모델 전처리

1. preprocessing04

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

2. preprocessing05_XGBClassifier_def

   1. fillnullclassifier 함수
      1. column_name을 받아서 그 컬럼 이름의 null값을 XGBClassifier를 통해 예측한다
      2. 해당 컬럼의 null값이 채워진 dataframe을 리턴

3. preprocessing03_XGBRegressor_def02

   1. fillnull 함수
      1. column_name을 받아서 그 컬럼 이름의 null값을 XGBRegressor를 통해 예측한다
      2. 해당 컬럼의 null값이 채워진 dataframe을 리턴

4. preprocessing06_age

   1. Age의 정확도가 낮게 나와서 Age이상치를 확인하고 이상치를 제거한 값의 중앙값으로 null값을 채운다



## 모델 학습 코드

1. modeling_NaNdelete
   1. NaN값들을 모두 지운 데이터를 사용하여 훈련한 코드
   2.  Support Vector Machine (SVM)을 사용하여 데이터를 학습하고 모델을 구축한 후, 이 모델을 기반으로 테스트 데이터에 대한 예측을 수행하였다
   3. `accuracy_score(y_test, pred)`를 사용하여 모델의 성능을 평가하고, 정확도(accuracy)를 계산하였다
   4. `confusion_matrix`를 사용하여 모델의 예측 결과와 실제 레이블 간의 일치와 불일치를 계산하고, `skplt.metrics.plot_confusion_matrix`를 사용하여 혼동 행렬을 시각화하여 모델의 성능을 더 자세하게 분석하였다.
2. 
