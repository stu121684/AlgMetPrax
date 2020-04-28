#include <iostream>
#include <vector>
#include <algorithm>
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define tii tuple<int,int,int>
struct Triple {
  int isDiag;
  int amount;
  int factor;
};

bool compareTriple(const Triple a, const Triple b){
  return (a.isDiag * a.amount < b.isDiag * b.amount);
}

using namespace std;

int cti(char c){
  int res;
  switch(c){
    case 'A':
      res=0;
      break;
    case 'C':
      res=1;
      break;
    case 'G':
      res=2;
      break;
    case 'T':
      res=3;
  }
  return res;
}  

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;

  FOR(t,0,T){
    int n,m;
    cin >> n;
    cin >> m;
    string human[n];
    string mouse[m];

    FOR(i,0,n){
      cin>>human[i];
    }
    FOR(i,0,m){
      cin>>mouse[i];
    }
    int table[4][4] = {{0}};

    FOR(i,0,n){
      FOR(j,0,m){
	FOR(k,0,human[0].length()){
	  int d1=cti(human[i][k]);
	  int d2=cti(mouse[j][k]);
	  table[d1][d2]++;
	  if(d1!=d2) table[d2][d1]++;
	}
      }
    }
    vector<Triple> data;
    FOR(i,0,4){
      FOR(j,i,4){
	int isDiag;
	int amount;
	int factor;
	if(i==j){
	  isDiag=2;
	} else {
	  isDiag=1;
	}
	amount=table[i][j];
	factor=10;
	Triple tmp = {
	  isDiag,
	  amount,
	  factor
	};
	data.push_back(tmp);
      }
    }
    sort(data.begin(),data.end(),compareTriple);
    int c = 16;
    int i = 0;
    while (c>0) {
      if (data[i].isDiag==2) {
	data[i].factor=0;
	c--;
	i++;
      } else if (data[i].factor>-10) {
	data[i].factor-=5;
	c--;
      } else {
	i++;
      }
    }
    int result = 0;
    FOR(i,0,10){
      //cout << data[i].isDiag << " " << data[i].amount << " " << data[i].factor << endl;
      result+=data[i].amount*data[i].factor;
    }
    printf("Case #%d: %d\n", t+1, result);
  }

  return 0;
}
