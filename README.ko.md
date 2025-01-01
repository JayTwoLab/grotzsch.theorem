# 그뢰츠쉬의 정리

> [English](README.md) , [Korean](README.ko.md)

- **그뢰츠쉬의 정리** 는 그래프 이론에서 중요한 결과로, 특히 평면 그래프와 색칠 가능성에 관련된 연구에서 다뤄집니다. 
- 이 정리는 다음과 같이 서술됩니다:

### 정리:
**"모든 삼각형이 없는 평면 그래프는 3-색칠이 가능하다."**

### 주요 개념:
1. **삼각형 없는 그래프**:
   - 그래프가 삼각형이 없다는 것은, 길이가 3인 순환(cycle)을 포함하지 않는다는 뜻입니다(삼각형 모양의 부분 그래프가 없음).

2. **3-색칠 가능성**:
   - 그래프가 3-색칠 가능하다는 것은, 그래프의 정점들을 최대 3가지 색으로 색칠할 수 있으며, 서로 인접한 정점이 같은 색을 가지지 않도록 할 수 있음을 의미합니다.

3. **평면 그래프**:
   - 평면 그래프는 평면 위에 간선이 서로 교차하지 않도록 그릴 수 있는 그래프를 뜻합니다.

### 설명:
그뢰츠쉬의 정리는, 삼각형이 없는 평면 그래프라면 크기나 구조가 얼마나 복잡하든 항상 3가지 색으로 색칠할 수 있음을 보장합니다. 이 결과는 평면 그래프의 색칠 문제를 다루는 네 색 정리(Four-Color Theorem)의 특수한 경우로 볼 수 있으며, 삼각형이 없는 추가 조건을 적용한 경우 색칠이 더 단순해짐을 보여줍니다.

### 중요성:
- **그래프 색칠**:
  - 이 정리는 그래프 색칠 문제에 대한 통찰을 제공하며, 특히 주어진 제약 조건하에서 사용할 색의 수를 최소화하는 문제를 해결하는 데 기여합니다.

- **응용**:
  - 지도 색칠, 일정 관리, 네트워크 설계와 같은 분야에서 특정 조건을 만족하는 그래프 색칠 문제를 해결하는 데 활용됩니다.

### 네 색 정리와 비교:
- 네 색 정리는 모든 평면 그래프에 적용되지만, 그뢰츠쉬의 정리는 삼각형 없는 평면 그래프의 경우 필요한 색의 최대 수를 3으로 줄여줍니다. 이는 작은 순환(예: 삼각형)을 제거하면 색칠 문제가 단순화된다는 것을 보여줍니다.