#include <iostream>
#include <queue>

using namespace std;

const int MAX = 45;
const int GOLDEN_KEY = -1;
const int ISLAND = -2;
const int SOCIAL = -3;
const int SPACE = -4;
const int START = -5;
const int OWNED = -6;
int n, W, G, I;
queue<pair<int, bool>> dice; // 두 숫자합, 주사위가 같은지 여부 T:같다
queue<pair<int ,int>> goldKey; // 황금열쇠 정보 저장
int board[MAX] = {}; // -1:황금열쇠, -2 :무인도, -3:사회복지기금, -4:우주여행, -5:시작점, -6: 이미 산 땅

long long int socialMoney = 0; // 사회복지기금
long long int money = 0;
int playerPosition = 1;
int imprisonedTurns = 0;
int buyBuilding = 0; // 구매한 빌딩 개수
int buildingNum = 0; // 존재하는 빌딩 개수
bool isLose = false;

void input(){
  cin >> n >> money >> W >> G;

  // 황금열쇠 정보저장
  while(G--){
    int a, b;
    cin >> a >> b;
    goldKey.push({a, b});
  }

  // 보드판 정보 입력
  board[1] = START; // 시작점
  board[n] = ISLAND; // 무인도
  board[2 * n - 1] = SOCIAL; // 사회복지기금
  board[3 * n - 2] = SPACE; // 우주여행
  
  for(int i = 1; i <= 4 * n - 4; i++){
    if(board[i] == 0){ // 특수칸이 아니면
      string type; cin >> type;
      
      if(type == "L"){ // 건물
        int price; cin >> price;
        board[i] = price;
        buildingNum++;
      }
      else // 황금열쇠
        board[i] = GOLDEN_KEY;
    }
  }

  // 주사위 정보 입력
  cin >> I;
  for(int i = 0; i < I; i++){
    int a, b;
    cin >> a >> b;
    if(a == b) dice.push({a + b, true});
    else dice.push({a + b, false});
  }
}

// check
void check(){
  cout << "\n";
  for(int i = 1; i <= 4 * n - 4; i++){
    cout << board[i] << ' ';
    if(i % (n - 1) == 0) cout << "\n";
  }
  cout << "\n";
  cout << "money : " << money << " playerPos: " << playerPosition << "\n";
}

// 황금 키를 뽑을때
void playGoldkey(){
  int type = goldKey.front().first;
  int value = goldKey.front().second;
  goldKey.pop();
  goldKey.push({type, value});

  if(type == 1){ // 은행에서 돈 받기
    money += value;
  }
  else if(type == 2){ // 은행에 돈주기
    money -= value;

    if(money < 0){
      isLose = true;
    }
  }
  else if(type == 3){ // 사회 복지기금 내기
    money -= value;
    socialMoney += value;
    
    if(money < 0){
      isLose = true;
    }
  }
  else{ // 움직이기
    playerPosition += value;
    if(playerPosition > 4 * n - 4){ // 한바퀴를 돌면
      playerPosition %= 4 * n - 4;
      money += W;
    }
  
    // 행동하기
    if(board[playerPosition] == ISLAND) imprisonedTurns = 3;
      
    else if(board[playerPosition] == SOCIAL){
      money += socialMoney;
      socialMoney = 0;
    }

    else if(board[playerPosition] > 0){ // 일반 건물
      if(money >= board[playerPosition]){
        money -= board[playerPosition];
        buyBuilding++;
        board[playerPosition] = OWNED;
      }
    }
  }
}

void playGame(){
  if(imprisonedTurns > 0){ // 감옥
    if(dice.front().second){ // 더블이면 탈출
      imprisonedTurns = 0;
    }
    else{
      imprisonedTurns--; // 하루지남
      dice.pop();
      return;
    }
  }

  if(dice.empty()){ // 더이상 주사위가 없다면 끝
    return;
  }

  // 우주여행 보내기
  if(board[playerPosition] == SPACE){
    playerPosition = 1;
    money += W;
  }
  
  // 주사위를 굴리고 이동
  int moveValue = dice.front().first;
  dice.pop();
  
  playerPosition += moveValue;
  if(playerPosition > 4 * n - 4){ // 한바퀴를 돌면
    playerPosition %= 4 * n - 4;
    money += W;
  }

  // 행동하기
  if(board[playerPosition] == GOLDEN_KEY){
    playGoldkey();
  }
   
  else if(board[playerPosition] == ISLAND) imprisonedTurns = 3;
  
  else if(board[playerPosition] == SOCIAL){
    money += socialMoney;
    socialMoney = 0;
  }
    
  else if(board[playerPosition] > 0){ // 일반 건물
    if(money >= board[playerPosition]){
      money -= board[playerPosition];
      buyBuilding++;
      board[playerPosition] = OWNED;
    }
  }
}

int main() {
  // freopen("input.txt", "r", stdin);

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
    
  input();

  // check();

  while(!dice.empty()){
    playGame();
    if(isLose) break;
    // check();
  }

  if(buyBuilding == buildingNum && isLose == false) // 다 지었다면
    cout << "WIN";
  else
    cout << "LOSE";
  
  return 0;
}
