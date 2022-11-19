## Multcampus Science 2조 Mini Project

### 사용하는 데이터

[Body signal of smoking](https://www.kaggle.com/datasets/kukuroo3/body-signal-of-smoking/code?datasetId=2157551&sortBy=voteCount)



### EDA



### 모델 학습

1. [Mini_proj_basic](https://github.com/LeeJeaHyuk/Mulcam_ML_DL/blob/master/source_code/DS_ML/%5B01%5DMini_proj_basic.ipynb)
   1. EDA
      1. 범주형 데이터 gender, oral, tartar 를 0과 1로 라벨링
      2. object형 데이터 변환
   2. 훈련
      1. random_state = 42로 설정
      2. model
         - DecisionTreeClassifier
         - RandomForestClassifier
         - XGBoost
         - LGBMClassifier
         - Logistic Regression
         - Support Vector Machine
      3. 예측 후 confusion_matrix 확인
      4. classification_report 확인
2. [**Mini_proj_gridcv**](https://github.com/LeeJeaHyuk/Mulcam_ML_DL/blob/master/source_code/DS_ML/%5B01%5DMini_proj_gridcv.ipynb)
   1. Mini_proj_basic model 에 GridSerchCV 를 사용해서 하이퍼파라미터 조정
   2. params_fit 함수를 만들어서 GridSerchCV 의 .best_params_ 을 받아와서 모델에 바로 적용
      1. 최적의 파라미터를 찾는 데 오래 걸리므로 다음 번에 다시 결과를 볼 때에는 저장된 파라미터를 사용해서 시간을 단축
      2. **실행할 때 마다 날짜별로 저장되는 함수를 추하해야 함 // 미적용**
   3. 각 모델 별 하이퍼파라미터 조사
      1. 