import numpy as np
import pandas as pd #데이터 프레임 사용하기 위해
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [10, 8]

# face expression 데이터
face_expression_data = [
    [976, 0, 0, 0, 6, 18, 0],
    [0, 997, 0, 0, 3, 0, 0],
    [1, 0, 982, 0, 0, 6, 11],
    [1, 2, 2, 995, 0, 0, 0],
    [14, 0, 0, 0, 975, 11, 0],
    [17, 0, 0, 0, 5, 978, 0],
    [0, 0, 3, 0, 0, 0, 997]
]

# 인덱스와 컬럼 설정
emotions = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# 데이터프레임 생성
df = pd.DataFrame(face_expression_data, index=emotions, columns=emotions)

# 데이터프레임 출력
print(df)

def plot_confusion_matrix(face_expression_data, emotions):
    plt.figure(figsize=(12,10))
    sns.set(font_scale=1)
    sns.heatmap(df, annot=True, fmt='d', cmap='Greys')

    plt.xticks(np.arange(len(emotions))+0.5, emotions, rotation = 0)
    plt.yticks(np.arange(len(emotions))+0.5, emotions, rotation = 0)

    plt.xlabel('Estimated label')
    plt.ylabel('True label')
    plt.title('Confusion Matrix of face expression recognition')
    plt.show()

# 히트맵으로 Confusion Matrix 그리기
plot_confusion_matrix(face_expression_data, emotions)