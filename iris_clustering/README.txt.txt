Iris K-Means Clustering

Iris 데이터를 이용하여 K-Means 알고리즘으로 비지도 학습을 실습한 프로젝트입니다.

사용 기술

Python

NumPy

Scikit-learn

사용한 모델

K-Means Clustering

데이터셋

Scikit-learn에서 제공하는 Iris dataset을 사용했습니다.

Iris dataset에는 붓꽃의 꽃받침과 꽃잎의 길이와 너비에 대한 데이터가 포함되어 있습니다.

from sklearn.datasets import load_iris

data = load_iris()
X = data.data


이번 실습에서는 정답 클래스인 target을 모델 학습에 사용하지 않고, 꽃의 특성 데이터만 이용하여 K-Means 군집화를 수행했습니다.

K-Means 군집화

K-Means를 사용하여 데이터를 3개의 군집으로 나누었습니다.

from sklearn.cluster import KMeans

km = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

km.fit(X)


n_clusters=3: 3개의 군집으로 분류

random_state=42: 실행할 때마다 동일한 결과를 얻기 위한 설정

n_init=10: 서로 다른 초기 중심점으로 10번 실행한 뒤 가장 좋은 결과 선택

결과 확인
군집별 데이터 개수
labels = km.labels_

print("무리별 인원 =", np.bincount(labels))


각 군집에 몇 개의 데이터가 포함되어 있는지 확인했습니다.

군집 내 오차
print("무리 안 흩어진 정도 = %.2f" % km.inertia_)


inertia_는 각 데이터와 해당 군집 중심점 사이의 거리 제곱을 모두 더한 값입니다.

값이 작을수록 일반적으로 데이터가 각 군집의 중심에 가깝게 모여 있다는 의미입니다.

군집 중심점
print("무리 중심점:")
print(np.round(km.cluster_centers_))


각 군집의 중심점을 확인했습니다.

실제 Iris 품종과 비교

K-Means 학습에는 정답인 target을 사용하지 않았지만, 군집 결과가 실제 Iris 품종과 어느 정도 대응하는지 확인하기 위해 비교했습니다.

for c in range(3):
    m = labels == c
    print(
        "무리", c,
        "인원", m.sum(),
        np.bincount(data.target[m], minlength=3)
    )


이를 통해 각각의 군집에 실제 Iris 품종이 어떻게 섞여 있는지 확인할 수 있습니다.

배운 점

비지도 학습의 개념

K-Means 군집화

군집의 개수 설정

군집 중심점의 의미

labels_를 이용한 군집 결과 확인

inertia_의 의미

군집 결과와 실제 정답 데이터 비교

지도 학습과 비지도 학습의 차이

프로젝트 구조
iris-clustering/
├── iris_clustering.py
├── requirements.txt
└── README.txt

실행 방법
1. 라이브러리 설치
pip install -r requirements.txt

2. Python 파일 실행
python iris_clustering.py