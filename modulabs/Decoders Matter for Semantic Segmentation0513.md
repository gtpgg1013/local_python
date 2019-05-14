# Decoders Matter for Semantic Segmentation:

### Data-Dependent Decoding Enables Flexible Feature Aggregation

- semantic segmentation
  - 사진에 있는 모든 픽셀을 해당하는 class로 분류
- decoder를 좀 열심히 만졌다
  - decoder + low-level feature랑 합쳐야 boundary가 더 잘 predicting 됨

- bilinear 대신에 지들이 만든 DUpsampling이 더 낫다
  - bilinear? 양선형 보간법
    - 
- FCNs(Fully Convolution Networks)
- desolution
  - 해상도
- ground truth
  - 진짜 답과 비교할 실측 자료
- concat
  - 더하긔
- downsampling / upsampling
  - ds : 차원을 줄여서 적은 메모리로 깊은 Convolution 을 할 수 있게 하는 것입니다. 보통 stride 를 2 이상으로 하는 Convolution 을 사용하거나, pooling을 사용합니다. 이 과정을 진행하면 어쩔 수 없이 feature 의 정보를 잃게됩니다. 
  - us : Downsampling 을 통해서 받은 결과의 차원을 늘려서 인풋과 같은 차원으로 만들어 주는 과정입니다. 주로 Strided Transpose Convolution 을 사용합니다.
- RESNet
- 4배 upsampling을 했다는 건 원본 데이터의 손실이어서 결과가 좋긴 애매할텐데.. 계산량 이득만 보는거 아닌가??
  - data-dependent하게 학습한 DUpsampling으로 극복?
- DeepNet vs UNet?
- 왜 flexable하지..?
- adaptive-temperature softmax
- [https://m.blog.naver.com/PostList.nhn?blogId=laonple&categoryNo=49&logCode=0&categoryName=%EC%9B%94%EA%B0%84%20%EC%9E%90%EB%8F%99%EC%9D%B8%EC%8B%9D%20%EC%95%84%EC%B9%B4%ED%85%8C%EB%AF%B8](https://m.blog.naver.com/PostList.nhn?blogId=laonple&categoryNo=49&logCode=0&categoryName=월간 자동인식 아카테미)
- <https://m.blog.naver.com/PostList.nhn?blogId=laonple&categoryNo=31&listStyle=style1>