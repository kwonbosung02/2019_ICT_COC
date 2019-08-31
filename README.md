### 2019_ICT_COC

데이터셋 훈련을 통한 모델 생성 -> 두가지 방법 이용

1. Vgg16 (케라스에서 학습된 결과 제공)

   accuracy : 80% ~ 82%



2. MobileNet  (효율성의 trade off를 맞춤)

   accuracy: 95%



최종적으로 1번 방식을 .h5파일로 저장 후 openCV에서 로딩하여 Real time으로 사용, 감지된 오브젝트의 값을 데이터베이스에 전달