import streamlit as st

st.title("aaa6")
st.markdown("""
# 소개

안녕하세요! 저는 인테리어 디자이너 서경찬 입니다.

## 나에 대해
- **위치**: 대한민국 부산
- **경력**: 10년간 인테리어 회사를 운영하며 창의적인 프로젝트를 다수 진행.
- **취미**: 
  - 일렉기타 연주
  - 다양한 물건을 고치며 창의적인 해결책을 찾는 활동
- **관심 분야**:
  - 예술 및 창작
  - 사회와 경제
  - 창업과 미래 준비

## 목표
1. **능력 향상**: 사고력을 확장하고 문제 해결 능력을 체계적으로 키우기.
2. **영어 실력 강화**: 글로벌한 소통 능력을 갖추기 위해 노력.
3. **현실화 기술**: 창조적인 아이디어를 실제로 실현하는 데 집중.
4. **경제적 성공**: 지속 가능한 수익 모델 구축.

## 현재 활동
- **창업 준비**: 다양한 아이디어를 현실화하며 새 비즈니스를 구상 중.
- **AI 프로젝트**:
  - 지각 방지 앱
  - 외로움 방지 AI 동반자
  - 낚시 장비 추천 웹사이트
  - 예산 내 제품 추천 AI 쇼핑 카트 시스템

## 비전
세상에 더 나은 가치를 제공하는 창의적이고 혁신적인 프로젝트를 통해, 모두가 더 나은 삶을 누릴 수 있는 미래를 만드는 것이 목표입니다.
""")

st.markdown(""" 완전신기한 컴언어!!대박이넹ㅋㅋㅋ 존잼임 """)

import matplotlib.pyplot as plt
import pandas as pd

# 데이터 준비 (예시 데이터)
years = list(range(2000, 2025))
house_price_index = [
    50, 52, 55, 58, 60, 65, 70, 75, 80, 85,  # 2000~2009
    90, 95, 100, 105, 110, 115, 120, 125, 130, 135,  # 2010~2019
    140, 145, 150, 155, 160, 165, 170, 175, 180, 185,  # 2020~2024
]

# 데이터프레임 생성
data = pd.DataFrame({
    'Year': years,
    'House Price Index': house_price_index
})

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(data['Year'], data['House Price Index'], marker='o', linestyle='-', color='b', label='House Price Index')

# 그래프 제목 및 축 레이블
plt.title('South Korea House Price Index (2000-2024)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('House Price Index (2005=100)', fontsize=12)

# 주요 이벤트 표시
plt.annotate('Global Financial Crisis (2008)', xy=(2008, 80), xytext=(2006, 70),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.annotate('COVID-19 Surge (2020-2022)', xy=(2021, 170), xytext=(2018, 160),
             arrowprops=dict(facecolor='green', shrink=0.05))

# 그리드 및 범례 추가
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 그래프 표시
plt.show()