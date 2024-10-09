from scipy import signal

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([-2, 0, 1])

# correlation

signal.correlate(a,b)

signal.correlate(b,a)

# convolution = flip + correlation

a

b

np.flip(b)

signal.convolve(a,b)

signal.convolve(b,a)

signal.correlate(a, np.flip(b))

signal.convolve(a,b)

signal.convolve(a,np.flip(b))

# image

# ml -> 1차 형태의 데이터로 변환 ( 차원의 저주, 로컬 정보 손실 )
# nn ( full connected > 크기, 위치, 회전 등 다르면 문제가 생김 )

# 2/3차 형채로 입력데이터를 구성 ( 1차로 변환시킬때 문제 )
# 특성이 있는지 없는지의 형태로 변환 ( correlation(convolution : 수학적 특성) > 로컬 정보 활용, 1차로 변환시 문제 소지 축소, 독립성 가정 확보 ) - translation equivalance 위치에 상관없는 특징
# nn 연산 특징 유사
# 여러개 사용


# 이미지 > 이미지 ( image processing ) : filter
# image kernel explainged - https://setosa.io/ev/image-kernels/

# https://poloclub.github.io/cnn-explainer/

