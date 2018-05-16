---
layout: post
title:  "Cpp로 만드는 OOP 단계 별 프로젝트 02단계"
date:   2017-08-17 15:20:00
categories: [Cpp]
tags: OOP_project
comments: true
---
<h2>Bank System Ver0.2</h2>  

<!--more-->

OOP(Object Oriented Programming, 객체 지향 프로그래밍)을 학습하면서 OOP의 주요 특징(캡슐화, 상속, 다형성)을 보다 확실하게 이해하기 위해 이 프로젝트를 진행한다. 프로젝트의 진행 과정은 총 11단계로 구성되어있다. 프로그램의 구성은 달라질 수 있으나 그 초기 단계는 BankingSystem(은행 시스템)으로 한다.

---

이전 프로젝트에서는 틀을 구성하는 것이 목적이었다면, 이번에는 본격적으로 프로젝트를 시작하는 것이라고 생각하길 바란다. 이제부터는 문법적인 요소를 고려하기 보다는 어떻게, 무엇을 만들 것인가를 고려하도록 하자.  

프로젝트 구현에 앞서 간단하게 프로그램을 설명하려고 한다. 이전에 구현했던 버전을 업그레이도 하자. 아직 클래스 설계가 익숙하지 않으니, 버전 0.1에서 정의한 구조체를 클래스로 변경하려고 한다. 이는 단순히 키워드를 struct에서 class로 변경하겠다는 것이 아니라 아래와 같은 고민을 하겠다는 것이다.  

> "어떻게 캡슐화를 하고, 정보를 은닉시킬까?"
> "생성자와 소멸자는 어떻게 정의할까?"
  

추가적으로 2가지를 제약하고자 한다. 버전 0.1의 Account 구조체는 char형 배열을 멤버로 둬서 고객의 이름을 저장했는데, 버전 0.2에서는 이를 동적 할당의 형태로 구현할 것이다. 즉, Account 클래스는 멤버변수로 문자열 포인터를 지니고 있어야 한다.  

또 다른 제약은 객체를 저장하는 배열에 대해서이다. 객체 배열을 선언하지 말고, 객체 포인터 배열을 선언해서 객체를 저장하고자 한다. 버전 0.1에서는 구조체 배열을 선언하였으니, 이를 포인터 배열로 변경해야할 것이다.  

{% highlight Cpp %}

#include <iostream>
#include <cstring>
using namespace std;
const int NAME_LEN = 20;

void ShowMenu();		// 메뉴 출력
void MakeAccount();		// 개좌 개설
void DepositMoney();	// 입금
void WithdrawMoney();	// 출금
void ShowAllAccInfo();	// 잔액 조회

enum { MAKE = 1, DEPOSIT, WITHDRAW, INQUIRE, EXIT };

class Account
{
private:
	int accID;
	int balance;
	char* name;
public:
	Account(int accID, int balance, char* name)
		: accID(accID), balance(balance)
	{
		this->name = new char[strlen(name) + 1];
		strcpy_s(this->name, strlen(name) + 1, name);
	}
	int GetAccID() { return accID; }

	void Deposit(int money)		// 입금
	{
		balance += money;
	}

	void Withdraw(int money)		// 출금
	{
		if (balance < money)
		{
			cout << "잔액 부족" << endl;
			return;
		}
		balance -= money;
		cout << "출금 완료" << endl;

	}

	void ShowAccInfo()
	{
		cout << "계좌 ID: " << accID << endl;
		cout << "이 름: " << name << endl;
		cout << "잔 고: " << balance << endl;
	}
	~Account()
	{
		delete[]name;
	}
};

Account* accArr[100];
int accNum = 0;

int main()
{
	int choice;

	while (1)
	{
		ShowMenu();
		cout << "선택: ";
		cin >> choice;
		cout << endl;

		switch (choice)
		{
		case MAKE:
			MakeAccount();
			break;
		case DEPOSIT:
			DepositMoney();
			break;
		case WITHDRAW:
			WithdrawMoney();
			break;
		case INQUIRE:
			ShowAllAccInfo();
			break;
		case EXIT:
			for (int i = 0; i < accNum; i++)
				delete accArr[i];
			return 0;
			break;
		default:
			cout << "Illegal selection.." << endl;
		}
	}
}

void ShowMenu()
{
	cout << "-----MENU-----" << endl;
	cout << "1. 계좌 개설" << endl;
	cout << "2. 입 금" << endl;
	cout << "3. 출 금" << endl;
	cout << "4. 계좌정보 전체 출력" << endl;
	cout << "5. 프로그램 종료" << endl;
}

void MakeAccount()
{
	int id;
	char name[NAME_LEN];
	int balance;

	cout << "[개좌 개설]" << endl;
	cout << "계좌 ID: "; cin >> id;
	cout << "이름: "; cin >> name;
	cout << "입금액: "; cin >> balance;
	cout << endl;

	//accArr[accNum] = new Account(id, balance, name);
	accArr[accNum++] = new Account(id, balance, name);
}

void DepositMoney()
{
	int money;
	int id;

	cout << "[입 금]" << endl;
	cout << "계좌ID: "; cin >> id;
	cout << "입금액: "; cin >> money;

	for (int i = 0; i < accNum; i++)
	{
		if (accArr[i]->GetAccID() == id)
		{
			accArr[i]->Deposit(money);
			cout << "입금 완료" << endl << endl;
			return;
		}
	}
	cout << "유효하지 않은 ID입니다." << endl << endl;
}

void WithdrawMoney()
{
	int money;
	int id;
	cout << "[출 금]" << endl;
	cout << "계좌ID: "; cin >> id;
	cout << "출금액: "; cin >> money;

	for (int i = 0; i < accNum; i++)
		if (accArr[i]->GetAccID() == id)
			accArr[i]->Withdraw(money);
}

void ShowAllAccInfo()
{
	for (int i = 0; i < accNum; i++)
	{
		accArr[i]->ShowAccInfo();
		cout << endl;
	}
}

{% endhighlight %}  

><h5>어려웠던 점</h5>

>어려웠다기 보다는 다소 헷갈렸던 것이 아래의 MakeAccount 함수이다.

{% highlight Cpp %}

void MakeAccount()
{
	int id;
	char name[NAME_LEN];
	int balance;

	cout << "[개좌 개설]" << endl;
	cout << "계좌 ID: "; cin >> id;
	cout << "이름: "; cin >> name;
	cout << "입금액: "; cin >> balance;
	cout << endl;

	//accArr[accNum] = new Account(id, balance, name);
	accArr[accNum++] = new Account(id, balance, name);
}

{% endhighlight %}  


>처음에는 주석처리한 코드를 사용했는데 계좌가 개설이 되지 않았다. 지금 생각해보면 사실 당연한 것이다. 왜냐하면 accNum의 용도는 계좌의 개수를 새는 것인데 이것을 증가시키는 코드도 없을 뿐더러 1부터 시작하는 것이 관리하기 용이하기 때문이다.

>또한, 추가적으로 클래스가 익숙하지 않다보니 클래스를 어떻게 구현할지에 대해서도 오래 생각하게 되었다.