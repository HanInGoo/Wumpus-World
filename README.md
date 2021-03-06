# Wumpus-World
2021년 1학기 인공지능 수업 Wumpus World 팀 프로젝트 (3조)

## 💡 Description

![image](https://user-images.githubusercontent.com/79908728/178920582-755fbfab-0826-4cc4-ab9c-80308ae5f14f.png)


### 【배경】
본 프로젝트의 목적은 여러분이 인공지능 교과목에서 배운 지능형 소프트웨어 
패러다임에 대한 이해를 바탕으로 지능형 시스템의 간단한 예제인 Wumpus 
World를 프로그래밍하는 것입니다.<br/>
 여러분이 익숙한 프로그래밍 언어를 선택할 수 있으며, Wumpus World에서 
에이전트의 이성적인 행동을 구현해 보십시오. 또한, 팀 프로젝트를 수행함으로
써 협력작업 및 각자 맡은 일의 효율적이며 공정한 분배를 추구할 것입니다. 즐
거운 프로젝트가 되기를 바랍니다.

### 【Project 내용】
Wumpus World의 기초적인 형태를 구현해 본다. 

#### ■ 에이전트가 처한 환경
탐험하는 에이전트가 처한 환경은 4×4 격자로 구성되어 있으며, (1,1) 격자는 
안전하다(safe)고 가정한다. 4×4 격자 세계(Grid World)의 고정된 위치에 금
(gold), wumpus 괴물 및 웅덩이(pitch)가 존재한다. wumpus 괴물 및 웅덩이
가 발생할 확률은 각각의 격자에서 독립적이며, 0.15로 가정한다. 에이전트가 
금을 획득하여 [1,1] 격자로 되돌아오면 탐험은 종료된다. 

에이전트의 센서를 통한 입력은 다음과 같다:<br/> 
[Stench, Breeze, Glitter, Bump, Scream] 
- Stench: wumpus 괴물의 존재 여부
- Breeze: 웅덩이의 존재 여부
- Glitter: 금(gold)의 존재 여부
- Bump: 벽(wall)의 존재 여부
- Scream: wumpus 괴물이 에이전트가 쏜 화살에 의하여 제거되었는지에 대
한 여부

에이전트의 행동은 다음과 같다: <br/>
[GoForward, TurnLeft, TurnRight, Grab, Shoot, Climb] 
- GoForward: 에이전트가 한 격자를 이동한다. - TurnLeft: 현재 격자에서 왼쪽으로 90도 방향 전환한다. 
- TurnRight: 현재 격자에서 오른쪽으로 90도 방향 전환한다. 
- Grab: 금(gold)을 잡는다. 
- Shoot: 현재 에이전트의 방향으로 화살을 쏜다. 
- Climb: 에이전트가 금을 획득하여 [1,1] 격자로 되돌아 오면, 동굴을 빠져나
간다. 

#### ■에이전트의 기본 값
에이전트는 안전한 (1,1) 격자에서 출발한다. 즉, (1,1) 격자에는 wumpus 괴
물과 웅덩이가 존재하지 않으며, 금 역시 존재하지 않는다. 에이전트는 처음에 
동쪽(East)을 향하고 있으며, 화살을 3개 가지고 있다. 

#### ■입출력 화면
Wumpus World에서 에이전트의 이동과 현재까지 에이전트가 탐험한 결과에 
대한 격자 세계를 표현한다. 텍스트 모드 혹은 그래픽 모드로 표현할 수 있다.

## ⚙ Main Function
:point_right: ppt자료 참고

## 🛠 Tech Stack
<strong>언어 : </strong> Python<br>
<strong>개발환경 : </strong> PyCharm<br>


