---
layout: post
title:  "Cpp로 만드는 OOP 단계 별 프로젝트 01단계"
date:   2017-07-21 15:20:00
categories: [Cpp]
tags: OOP_project
comments: true
---
<h2>Banking System Ver0.1 만들기</h2>  

<!--more-->

OOP(Object Oriented Programming, 객체 지향 프로그래밍)을 학습하면서 OOP의 주요 특징(캡슐화, 상속, 다형성)을 보다 확실하게 이해하기 위해 이 프로젝트를 진행한다.  

프로젝트의 진행 과정은 총 11단계로 구성되어있다. 프로그램의 구성은 달라질 수 있으나 그 초기 단계는 BankingSystem(은행 시스템)으로 한다.

---

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

enum {MAKE = 1, DEPOSIT, WITHDRAW, INQUIRE, EXIT};

typedef struct
{
	int accID;		// 계좌 번호
	int balance;	// 잔액
	char cusName[NAME_LEN];	// 고객 이름
} Account;

Account accArr[100];
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
			return 0;
		default:
			cout << "Illegal selection." << endl;
		}
	}
	return 0;
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

	accArr[accNum].accID = id;
	accArr[accNum].balance = balance;
	strcpy_s(accArr[accNum].cusName, name);
	accNum++;
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
		if (accArr[i].accID == id)
		{
			accArr[i].balance += money;
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
	{
		if (accArr[i].accID == id)
		{
			if (accArr[i].balance < money)
			{
				cout << "잔액 부족" << endl << endl;
				return;
			}
			accArr[i].balance -= money;
			cout << "출금 완료" << endl << endl;
			return;
		}
	}
}

void ShowAllAccInfo()
{
	for (int i = 0; i < accNum; i++)
	{
		cout << "계좌ID: " << accArr[i].accID << endl;
		cout << "이 름: " << accArr[i].cusName << endl;
		cout << "잔 액: " << accArr[i].balance << endl << endl;
	}
}

{% endhighlight %}  

><h5>어려웠던 점</h5>

>크게 어려운 내용이 없었다. 또한 표준에 맞추기 위해 strcpy를 strcpy_s로 표기했으니 참고하기 바란다.