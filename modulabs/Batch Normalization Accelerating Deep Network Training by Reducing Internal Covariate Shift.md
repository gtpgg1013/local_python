# Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift

### modulabs 풀잎스쿨 #1

- 3장 내용
  - 이 학습을 진행하면서 인풋이 점점 노드들을 지나가면서 편향됨
  - 그걸 막아보려고 정규화 (A1)
  - 더 좋은거 ? 감마, 베타 : BN 레이어 넣어서 걔네도 학습시키며 더 좋게 하자 (A2)

- Normalization via Mini-Batch Statistics 3.1
  - 1번째 시도
  - 2번째 시도
    - mini-batch 사용
    - joint covariance
    - decorrelate
    - back-propagation
  - 알고리즘 1
    - Normalization으로 input들을 한번 만져줌
  - 알고리즘 2
    - freezing
    - 근데 알고리즘 1로 input들을 만져준 다음에도 그게 그렇게 최적값이 아닐 수가 있다!
    - 그래서 감마와 베타라는 두  변수를 붙여서 더 좋게 해보자
    - 근데 감마와 베타도 학습시킴
    - 1~4  : Batch Norm layer를 만들어서 네트워크에 한겹씩 붙인다
    - 5~7 : 파라미터, 감마, 베타 학습
    - 8~11 : 여러개의 미니배치 모델을 만든 다음, 그 각자 미니배치 모델의 평균, 분산을 이용해서 전체 추론 네트워크(Ninf)의 평균과 분산을 추론한다
      - moving average : 이동 평균법 (지수평활) : 메모리 사용 적게해서 좋음
        - `M(n+1)=a*M(n)+(1-a)*x(n)`
    - 배치마다마다 감마베타 계속 학습
    - 모집단의 평균....?
    - auto-regressive
- 3.2
  - activation(relu, sigmoid) 바로 뒷단에서 BN 하는 것보다는
  - 각 노드노드 뒤에서 바로 BN 해주는게 낫다
  - CNN에서는 m개의 데이터에 관한거면 m * p /* g개가 배치 사이즈가됨
    - depth는 나머지 k가 되겠군....?
- 3.3
  - BN 하면 higher learning rate 할 수 있다!
- 3.4
  - BN하면 모델 정규화가능