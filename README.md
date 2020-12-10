# Graduation_project

## 시연 영상 주소
### 유튜브채널 주소

### 시제품 (웹)
https://emoticon-chat-project.herokuapp.com/

<br>
## 프로젝트에 대한 소개
A project to identify the nuances of a conversation through a user's chat conversation and recommend appropriate emoticons.

### 프로젝트의 목적
본인의 감정을 표현할 수 있는 이모티콘을 찾는데 시간이 소요되고 번거롭다. <br>
현재 있는 이모티콘 추천시스템은 비슷한 단어를 기반으로 한 이모티콘 추천에 그쳤다. <br>
따라서 이모티콘의 수요가 점점 높아져가는 상황에서, 대화의 전체적인 맥락을 파악하여 상황에 맞는 적절한 이모티콘을 추천하고 채팅방에 효과가 나타나는 시스템을 만들어 채팅사용자의 만족도를 높이고자 한다.

### 시나리오
1. 사용자가 채팅을 주고받는 동안 대화 내용 수집
2. 수집한 대화를 분석하여 대화의 감정을 분석하여 분류 <br>
3. 감정의 카테고리(13가지): 머쓱할 때, 화가 날 때, 고마울 때(감동), 대화를 끝낼 때, 파이팅 할 때, 슬플 때, 무기력 할 때, 예측하는 이모티콘, 의문을 가질 때, 귀여운 모습을 보이고 싶을 때, 미안할 때, 비꼴 때, 대답할 때
4. 대화 내용에 해당하는 감정과 맞는 이모티콘을 사용자에게 실시간으로 추천 및 채팅창에 효과 제공

<br>
## Reference
+ 채팅 웹 구현 <br>
https://github.com/leegeunhyeok/node-chat <br>
+ 대화의 감정 분석 <br>
넥슨의ndc(개발자 컨퍼런스) 욕설 분류: 정확도 약 90퍼센트 (1dCNN 사용): https://www.youtube.com/watch?v=K4nU7yXy7R8 <br>
딥러닝을 사용한 온라인 게임에서의 욕설 탐지 - 한국컴퓨터정보학회 학술발표논문집 27(2), 2019.7, 13-14(2 pages) <br>
BERT언어 이해를 위한 양방향 트랜스포머 사전 학습(BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding) -googleAI <br>
구글 bert github: https://github.com/google-research/bert <br>
Attention is all you need(transformer model paper): https://arxiv.org/abs/1706.03762 <br>
Bert model paper: https://arxiv.org/abs/1810.04805 <br>

<br>
## 팀원 기술블로그 주소
양은서 (https://eunseo1092.tistory.com/) : attention 기법을 기반으로 문장의 의미를 분석해보는 transformer model을 이용한 감정 분석 <br>
남궁지윤 (https://deepdeep12.tistory.com/) : 사전학습을 통해 텍스트의 흐름까지 파악할 수 있는 bert model을 이용한 감정 분석<br>
이경민 (https://blog.naver.com/julie-code) : 자연어처리를 위한 Word2Vec을 한국어에 적용 및 채팅 시스템 구현<br>
장보미 (https://bomiiiii.tistory.com/11) : 크롤링 및 자연어의 이미지화가 가능한 1dCNN을 통한 감정분석 <br>

<br>
## License
MIT License
