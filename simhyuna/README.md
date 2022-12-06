# << DS 프로젝트 - Kaggle Sapceship Titanic 분석/예측 >>

## 파일 Summary
1. CSV
- train : 기본 제공 train set
- test : 기본 제공 test set
- train_HomePlanetNull_update : HomePlanet 컬럼의 null 값을 예측값으로 채운 data
- train_CryoSleepNull_update : CryoSleep 컬럼의 null 값을 예측값으로 채운 data
- train_CabinNull_update : Cabin 컬럼의 null 값을 예측값으로 채운 data
- train_VIPNull_update : VIP 컬럼의 null 값을 예측값으로 채운 data
- died_rate : 각 컬럼별 Transported 비율


<br/>

2. DataOverview
- [data_summary.html]() : Data 기본 정보에 대한 html문서
- [DataOverview.ipynb]() : Data 기본 정보 코드

<br/>

3. EDA
- [Cabin_Analysis.ipynb]() : 각 객실별(D~T) Transported 비율 계산
- [DataVisualization.ipynb]() : 나이별 RoomService 지불 금액 히스토그램 시각화
- [EDA_HA .ipynb]()
    - 특정 사분위수 이상의 지출을 한 승객들의 Transported 비율 계산, 함수 정의
    - 지출을 하지 않은 승객들의 Transported비율 계산
    - 총 지출 확인
    - 나이별 지출 확인
    - 나이별, 각 나이 미만의 Transported 비율 계산
    - 가족단위 승객 탐색
- [EDA03.ipynb]() : Cabin num별 Transported 비율 계산

<br/>

4. Preprocessing
- [preprocessing01_CryoSleep02.ipynb]()
    - CryoSleep의 Null값을 예측하는 모델 실행, 새로운 csv생성
- [preprocessing01_Destination04.ipynb]()
    - Destination의 Null값을 예측하는 모델 실행, 새로운 csv생성
- [preprocessing01_VIP03.ipynb]()
    - VIP의 Null값을 예측하는 모델 실행, 새로운 csv생성
- [preprocessing01_Cabin_port.ipynb]()
    - Cabin_port의 Null값을 예측하는 모델 실행, 새로운 csv생성
    - 추후 보완점 확인되어 사용하지 않음(Score 낮음, Cabin컬럼을 새롭게 범주화함)
- [preprocessing01_Cabin.ipynb]()
    - Cabin_port의 Null값을 예측하는 모델 실행, 새로운 csv생성
    - 추후 보완점 확인되어 사용하지 않음(Score 낮음, Cabin컬럼을 새롭게 범주화함)


<br/>