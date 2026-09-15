Diabetes Regression & Classification

Scikit-learn의 Diabetes dataset을 이용하여 **회귀(Regression)**와 분류(Classification) 모델을 실습한 프로젝트입니다.

사용 기술

Python

Pandas

NumPy

Scikit-learn

데이터셋

Scikit-learn에서 제공하는 Diabetes dataset을 사용했습니다.

데이터를 load_diabetes()를 통해 불러오고, 회귀 문제와 분류 문제에 각각 활용했습니다.

from sklearn.datasets import load_diabetes

df = load_diabetes(as_frame=True).frame
print(df.head())

사용한 모델
Regression

Linear Regression

Dummy Regressor

Classification

Logistic Regression

Dummy Classifier

데이터 분리

전체 데이터를 학습 데이터와 테스트 데이터로 8:2 비율로 분리했습니다.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

1. Regression

Diabetes dataset의 연속적인 질병 진행 정도를 예측하기 위해 선형 회귀 모델을 사용했습니다.

Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

평가 지표

MAE (Mean Absolute Error)

R² (R-squared)

결과
모델	MAE	R²
Linear Regression	42.79	0.4526
Dummy Regressor	64.01	-0.0120

Linear Regression은 Dummy Regressor보다 낮은 MAE와 높은 R²를 보여주었습니다.

따라서 단순히 평균값을 예측하는 Baseline 모델보다 실제 특성을 이용한 선형 회귀 모델이 더 좋은 성능을 보였습니다.

2. Classification

Diabetes dataset의 목표값을 기준으로 데이터를 두 개의 클래스로 변환하여 분류 문제를 만들었습니다.

y_train_c = (y_train > 140).astype(int)
y_test_c = (y_test > 140).astype(int)


목표값이 140보다 크면 1, 그렇지 않으면 0으로 변환했습니다.

Logistic Regression
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train_c)

pred = clf.predict(X_test)

평가 지표

Accuracy

Precision

Recall

Confusion Matrix

print("정확도 = %.4f" % accuracy_score(y_test_c, pred))
print("정밀도 = %.4f" % precision_score(y_test_c, pred))
print("재현율 = %.4f" % recall_score(y_test_c, pred))
print(confusion_matrix(y_test_c, pred))

Dummy Classifier

분류에서도 Baseline 모델과 비교하기 위해 DummyClassifier를 사용했습니다.

base = DummyClassifier(strategy="most_frequent")
base.fit(X_train, y_train_c)

pred = base.predict(X_test)


most_frequent 전략을 사용하여 학습 데이터에서 가장 많이 등장하는 클래스를 항상 예측하도록 설정했습니다.

프로젝트에서 배운 점

Scikit-learn의 Diabetes dataset 사용 방법

Pandas DataFrame으로 데이터 확인하기

Train/Test 데이터 분리

Linear Regression을 이용한 회귀

Logistic Regression을 이용한 분류

MAE와 R²의 의미

Accuracy, Precision, Recall의 의미

Confusion Matrix 해석

Regression과 Classification의 차이

Dummy 모델을 이용한 Baseline 설정의 필요성

실제 모델의 성능을 Baseline과 비교하는 방법

실행 방법
1. 저장소 다운로드
git clone <repository-url>
cd <project-folder>

2. 필요한 라이브러리 설치
pip install -r requirements.txt

3. Python 파일 실행
python main.py

프로젝트 구조
.
├── main.py
├── requirements.txt
└── README.md

참고

본 프로젝트는 머신러닝의 기본적인 회귀 및 분류 모델 학습과 평가 방법을 익히기 위한 실습 프로젝트입니다.