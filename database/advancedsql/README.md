## SQL 심화  

지난 시간에는 SQL의 기본적인 내용에 대해 다뤘다. 이전 시간에는 SQL에 대해 소개하고 간단한 문법을 살펴보았다면, 이번 시간에는 조금 더 심화적인 내용을 다루도록 하겠다.   

---

##### Schema(스키마)란?

테이블에 적재될 데이터의 구조와 형식을 정의하는 것을 말한다. 즉, 칼럼의 이름을 정한다거나 컬럼에 해당되는 데이터의 형식 등을 정의하는 것이다.  

일종의 데이터 설계도라고 보면 된다. 설계도에 맞게 데이터베이스를 작성해야 하고, 설계도와 다를 경우 오류가 나오게 되는 구조이다.  

##### 테이블 생성 예시  

```
CREATE TABLE table_name (  
    칼럼명1 data_type,  
    칼럼명2 data_type  
)  

CREATE TABLE `student` (  
   `id`  tinyint NOT NULL ,  
   `name`  char(4) NOT NULL ,  
   `sex`  enum('남자','여자') NOT NULL ,  
   `address`  varchar(50) NOT NULL ,  
   `birthday`  datetime NOT NULL ,  
   PRIMARY KEY (`id`)  
);  
)  
)  
```

##### 테이블 리스트  

```
SHOW tables;
```
  
##### 테이블 스키마 열람  

```
DESC `테이블명`
```  
  
##### 테이블 제거  

```
DROP TABLE `테이블명`
```
  
##### 데이터 타입   

**문자**

|CHAR( ) | 0 to 255 고정문자 길이 |
|VARCHAR( ) |  0~65535 가변 문자 길이 |
|TINYTEXT | 최대 255 문자길이  |
|TEXT | 최대 65535 문자길이|
|BLOB | 최대 65535 문자길이|
|MEDIUMTEXT | 최대 16777215 문자길이 |
|MEDIUMBLOB | 최대 16777215 문자길이 |
|LONGTEXT | 최대 4294967295 문자길이|
|LONGBLOB | 최대 4294967295 문자길이|
  

**수**

|TINYINT( ) |  -128 ~ 127 정수형  |
| |0 ~ 255 정수형, UNSIGNED|
|SMALLINT( ) | -32768 ~ 32767, 정수형 |
| |0 ~ 65535, 정수형, UNSIGNED|
|MEDIUMINT( ) | -8388608 to 8388607, 정수형|
| |0 to 16777215 , 정수형, UNSIGNED|
|INT( ) | -2147483648 ~ 2147483647 정수형|
| |0 ~ 4294967295, 정수형, UNSIGNED|
|BIGINT( ) | -9223372036854775808 ~ 9223372036854775807, 정수형 |
| |0 ~ 18446744073709551615, 정수형, UNSIGNED.|
|FLOAT | 작은 부동소수점|
|DOUBLE( , ) | 큰 부동소수점  |
|DECIMAL( , ) |       |
  

**날짜**

|DATE | YYYY-MM-DD.|
|DATETIME | YYYY-MM-DD HH:MM:SS.|
|TIMESTAMP | YYYYMMDDHHMMSS.|
|TIME | HH:MM:SS.  |
  

**기타**

|ENUM ( ) | 정해진 값을 강제|
|SET | |
  

##### SELECT 기본문법에 대하여 이해한다.  

SELECT에 대해 살펴보자. 우선 SELECT는 '조회'를 위한 명령이다. 조회는 테이블에서 데이터를 조회하는 것을 말하며, 다음과 같이 사용한다.  

```
SELECT 칼럼명1, 칼럼명2  
   [FROM 테이블명 ]  
   [GROUP BY 칼럼명]  
   [ORDER BY 칼럼명 [ASC | DESC]]  
   [LIMIT offset, 조회 할 행의 수]  
```  

'[]'에 들어있는 내용은 생략이 가능하다. 이에 대한 설명은 잠시 후에 하도록 하겠다. 이러한 형태는 다음과 같이 실전에서 사용할 수 있다.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL,  
  name char(4) NOT NULL,  
  sex enum('남자','여자') NOT NULL,  
  address varchar(50) NOT NULL,  
  birthday datetime NOT NULL,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
 
INSERT INTO student VALUES (2, '박재숙', '남자', '서울', '1985-10-26 00:00:00');  
INSERT INTO student VALUES (1, '이숙경', '여자', '청주', '1982-11-16 00:00:00');  
INSERT INTO student VALUES (3, '백태호', '남자', '경주', '1989-2-10 00:00:00');  
INSERT INTO student VALUES (4, '김경훈', '남자', '제천', '1979-11-4 00:00:00');  
INSERT INTO student VALUES (8, '김정인', '남자', '대전', '1990-10-1 00:00:00');  
INSERT INTO student VALUES (6, '김경진', '여자', '제주', '1985-1-1 00:00:00');  
INSERT INTO student VALUES (7, '박경호', '남자', '영동', '1981-2-3 00:00:00'); 
```
  
이와 같이 구성된 데이터베이스에서 다음과 같이 'SELECT'를 사용할 수 있다.  
```
SELECT * FROM student;
```  

이것은 student라는 데이터베이스에 존재하는 모든 칼럼을 조회한다는 명령이다. 그럼 다음 예문을 살펴보자.  

```
SELECT name, birthday FROM student;  
```

* WHERE절에 대해 이해한다.    

이제 어느정도 감이 잡힐 것이다. 이것은 student라는 데이터베이스의 name과 birthday라는 칼럼을 조회하는 것이다. 다음은 새로운 형태이다.  

```
SELECT * FROM student WHERE id=3;  
```

WHERE는 현재 작업하려는 대상이 되는 행에 대해 조회하라는 명령이다. 여기서는 student 데이터베이스의 id값이 3인 ROW의 모든 칼럼을 출력하는 것이다. 여기서는 '백태호'라는 학생의 정보가 출력될 것이다.  

```
SELECT * FROM student WHERE sex='남자' AND address='서울';
```
  
이것은 성별이 남자이고, 주소가 서울인 학생의 모든 정보를 조회하는 것이다. 다음은 'OR'에 해당하는 명령을 살펴보자.  

```
SELECT * FROM student WHERE sex='여자' OR address='서울';
```
  
다음은 스키마의 한계를 정하는 명령을 살펴보자.  

```
SELECT * FROM student LIMIT 1;
```
  
이는 한계를 1로 정해 첫 번째에 해당하는 ROW를 조회하는 것이다.  

```
SELECT * FROM student LIMIT 0,1;  
SELECT * FROM student LIMIT 1,1;  
SELECT * FROM student LIMIT 2,1;  
SELECT * FROM student LIMIT 3,1;
```
  
이것을 입력해 결과를 확인해보기 바란다. 결과는 당연할 수도, 놀라울 수도 있다. 

왜냐하면 처음 입력한 명령의 경우 0번째 행을 1개 조회하는 명령이기 때문이다. 컴퓨터는 일반적으로 숫자를 0에서부터 시작하기 때문에 여기서는 '이숙경'에 해당하는 정보가 조회된다.  

```
SELECT * FROM student LIMIT 0,2;
```
  
이건 어떨까? 그렇다. 0번째 행부터 2개의 행을 조회하는 명령이다. 여기서는 '이숙경'과 '박재숙'의 정보가 조회된다.  

앞서 설명한 것들은 복합적으로도 사용할 수 있다. 다음과 같이 말이다.  

```
SELECT * FROM student WHERE sex='남자' LIMIT 2;
```
  
이는 성별이 '남자'에 해당하는 데이터를 2개의 ROW로 가져오는 것이다.  

##### INSERT 기본 문법에 대하여 이해한다.  

INSERT는 테이블에 데이터를 삽입하는 명령이다. 문법은 다음과 같다.  

```
INSERT INTO table_name VALUES (value1, value2, value3,...)
```  
  
또 다른 방법은 다음과 같다.  

```
INSERT INTO table_name (column1, column2, column3,...) VALUES (value1, value2, value3,...)
```
  
INSERT는 위와 같은 형태의 구조를 지니고 있으며, 다음과 같은 두 가지 방법으로 사용할 수 있다.  

```
INSERT INTO `student` VALUES ('2', 'leezche', '여자', '서울', '2010-10-26');  

INSERT INTO `student` (`id`, `name`, `sex`, `address`, `birthday`) VALUES ('1', 'myungjinko', '남자', 'seoul', '2022-11-16');
```
  
추가적으로 각 데이터는 해당 칼럼의 데이터타입 형태로 삽입되기 때문에 2번째 칼럼인 name이 char(4)와 같이 정의되어 있다면, 'leez'만 삽입될 수 있는 것이다.  

그렇다면 두 방식 중 어느 것이 좋은가에 대한 이야기를 해보자.  

데이터베이스라는 구조는 변경될 가능성이 높고, 변경된 사항에 대해 염두하지 않고 INSERT할 경우에 여러 문제가 발생할 수 있다.  

첫 번째 형태의 경우에는 칼럼의 순서와 이름이 명시되어 있지 않고, 암시되어 있기 때문에 두 번째 방식과 같이 직접 칼럼에 순서와 이름을 정의해주고 그에 따라 값을 생성하는 것이 바람직하다고 할 수 있다.  

##### UPDATE의 기본 문법에 대하여 이해한다.  

UPDATE는 데이터베이스에 적재되어 있는 데이터를 변경하는 명령이다. 문법은 다음과 같다.  

```
UPDATE 테이블명 SET 컬럼1=컬럼1의 값, 컬럼2=컬럼2의 값 WHERE 대상이 될 컬럼명=컬럼의 값
```
  
SET이라는 키워드로 그 뒤에 컬럼의 이름과 그 컬럼에 적용될 값이 들어간다. WHERE의 경우에는 앞에서도 설명한 것처럼 변경할 행에 대해 명시해주는 것이다. 다음과 같이 사용할 수 있다.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL,  
  name char(4) NOT NULL,  
  sex enum('남자','여자') NOT NULL,  
  address varchar(50) NOT NULL,  
  birthday datetime NOT NULL,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
   
INSERT INTO student VALUES (1, '이숙경', '여자', '청주', '1982-11-16 00:00:00');   
INSERT INTO student VALUES (2, '박재숙', '남자', '서울', '1985-10-26 00:00:00');  
INSERT INTO student VALUES (3, '백태호', '남자', '경주', '1989-2-10 00:00:00');  
INSERT INTO student VALUES (4, '김경훈', '남자', '제천', '1979-11-4 00:00:00');  
INSERT INTO student VALUES (8, '김정인', '남자', '대전', '1990-10-1 00:00:00');  
INSERT INTO student VALUES (6, '김경진', '여자', '제주', '1985-1-1 00:00:00');  
INSERT INTO student VALUES (7, '박경호', '남자', '영동', '1981-2-3 00:00:00');  
```

위와 같은 테이블이 존재한다고 할 때, 다음의 명령을 사용할 수 있다.  

```
UPDATE `student` SET address='서울';
```
  
이는 student 데이터베이스에 존재하는 address 칼럼의 정보를 모두 '서울'로 바꾸겠다는 의미를 지닌다. 즉, 모든 행들의 address가 '서울'로 변경된 것이다.  

```
UPDATE `student` SET name='이진경' WHERE id=1;
```  
  
이는 id 칼럼의 값이 1인 행에 관해서 student 데이터베이스의 name 행을 '이진경'으로 변경한다는 의미를 지닌다.  

조금 응용해서 다음을 살펴보자.  

```
UPDATE `student` SET name='고명진', birthday='2001-4-1' WHERE id=3;
```
  
이처럼 UPDATE는 두 개의 칼럼을 한 번에 변경할 수도 있다.  

##### DELETE 기본 문법에 대하여 이해한다.  

데이터베이스에서 데이터나 테이블을 삭제하는 명령이다. 문법은 다음과 같다.  

```
DELETE FROM 테이블명 [WHERE 삭제하려는 칼럼 명=값]
```
  
'[]'에 해당하는 내용은 생략 가능하고, 다음과 같이 사용할 수 있다.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL,  
  name char(4) NOT NULL,  
  sex enum('남자','여자') NOT NULL,  
  address varchar(50) NOT NULL,  
  birthday datetime NOT NULL,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
   
INSERT INTO student VALUES (1, '이숙경', '여자', '청주', '1982-11-16 00:00:00');  
INSERT INTO student VALUES (2, '박재숙', '남자', '서울', '1985-10-26 00:00:00');  
INSERT INTO student VALUES (3, '백태호', '남자', '경주', '1989-2-10 00:00:00');  
INSERT INTO student VALUES (4, '김경훈', '남자', '제천', '1979-11-4 00:00:00');  
INSERT INTO student VALUES (8, '김정인', '남자', '대전', '1990-10-1 00:00:00');  
INSERT INTO student VALUES (6, '김경진', '여자', '제주', '1985-1-1 00:00:00');  
INSERT INTO student VALUES (7, '박경호', '남자', '영동', '1981-2-3 00:00:00');  
```  
  
이와 같이 구성된 데이터베이스가 존재한다고 할 때, 아래와 같이 사용할 수 있다.  

```
DELETE FROM student WHERE id = 2;
```

##### TRUNCATE   

외래키에 해당하는 TRUNCATE는 WHERE문을 특정하지 않고, 테이블의 전체 데이터를 삭제할 때 사용할 수 있다. 문법은 다음과 같다.  

```
TRUNCATE 테이블명
```  
  
위의 데이터베이스의 모든 정보를 삭제할 때에는 다음과 같이 사용하면 될 것이다.  

```
TRUNCATE student;
```  

##### DROP TABLE   

또 다른 왜래키로는 DROP TABLE이 있다. TRUNCATE이 테이블의 모든 정보를 삭제했다면 DROP TABLE은 테이블 자체를 삭제하는 명령이다. 다음과 같은 문법을 지닌다.  

```
DROP TABLE 테이블명;
```  
  
또한, student 테이블을 삭제하기 위해서는 다음과 같이 사용할 수 있을 것이다.  

```
DROP TABLE student;
```
 
##### GROUP BY 절에 대하여 이해한다.  

다음은 Grouping에 대해 살펴볼 것이다. 그룹핑에는 GROUP BY를 사용하는데, 문법은 다음과 같다.  

```
SELECT * FROM 테이블명 GROUP BY 그룹핑 할 기준 칼럼명
```  
  
이는 특정 칼럼을 기준으로 그룹핑을 하는 명령이다. 실제로 아래와 같이 사용할 수 있다.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL,  
  name char(4) NOT NULL,  
  sex enum('남자','여자') NOT NULL,  
  address varchar(50) NOT NULL,  
  distance INT NOT NULL,  
  birthday datetime NOT NULL,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
   
INSERT INTO student VALUES (2, '박재숙', '남자', '서울',  10, '1985-10-26 00:00:00');  
INSERT INTO student VALUES (1, '이숙경', '여자', '청주', 200, '1982-11-16 00:00:00');  
INSERT INTO student VALUES (3, '백태호', '남자', '경주', 350, '1989-2-10 00:00:00');  
INSERT INTO student VALUES (4, '김경훈', '남자', '제천', 190, '1979-11-4 00:00:00');  
INSERT INTO student VALUES (8, '김정인', '남자', '대전', 200, '1990-10-1 00:00:00');  
INSERT INTO student VALUES (6, '김경진', '여자', '제주', 400, '1985-1-1 00:00:00');  
```  

위와 같은 테이블이 존재할 때, 아래와 같은 명령을 입력하여 그룹핑할 수 있다.  

```
select sex from student group by sex;
```
  
정리해서 이야기하면, student 테이블에 존재하는 'sex' 칼럼을 sex라는 그룹으로 조회하는 명령이다. 이것을 응용해 다음과 같은 명령을 사용할 수 있다.  

```
select sex,sum(distance), avg(distance) from student group by sex;
```  
  
이는 student 테이블의 sex 칼럼을 sex라는 그룹으로 묶고, 'distance' 칼럼의 데이터를 sum(합)하고, avg(평균)을 구하는 명령이다.  

그룹핑은 데이터의 구성을 원자화시키는 것 외에도 각각의 그룹핑된 칼럼을 기준으로 어떤 특정한 칼럼의 합이나 평균을 구할 수도 있다.  

##### HAVING 조건절에 대하여 이해한다.  

HAVING 조건절은 WHERE과 유사하지만 그룹을 나타내는 결과 집합의 행에 조건이 적용된다는 점에서 차이가 있다. 주로 다음과 같이 사용된다.  

```
select sex sum(distance) from student group by sex having sum >= 700
```  

이 경우에는 '남자'에 해당하는 칼럼이 출력된다. 왜냐하면 남자의 경우에는 distance의 합이 750으로 HAVING의 조건에 만족했고, 여자의 경우에는 600으로 조건에 만족하지 못했기 때문이다.  

##### 함수(Function)에 대하여 이해하고 활용한다.  

함수에는 기본적으로 벤터에서 제공하는 내장형 함수와 사용자가 정의할 수 있는 외장형 함수가 존재한다. 먼저 내장형 함수에 대해 살펴보자.  

##### 내장형 함수  

내장형 함수는 SQL을 더욱 강력하게 해주고 데이터 값을 간편하게 조작하는데 사용된다. 벤더별로 차이가 크지만 핵심적인 기능들은 이름이나 표현법이 다르더라도 대부분의 데이터베이스에서 제공하고 있다.  

이러한 내장형 함수는 다시 입력 값이 단일행 값이 입력되는 단일행 함수와 여러 행의 값이 입력되는 다중행 함수로 나눌 수 있다. 또, 다중행 함수는 다시 집계 함수, 그룹 함수, 윈도우 함수로 나눌 수 있는데, 이번에는 단일행 함수에 대해서만 살펴보도록 하자.  

##### 단일행 함수의 종류   

|종류|내용|함수의 예|
|:-----:|
|문자형 함수|문자를 입력하면 문자나 숫자 값을 반환한다.|LOWER, UPPER, LENGTH/LEN, SUBSTR/SUBSTRIING 등|
|숫자형 함수|숫자를 입력하면 숫자 값을 반환한다.|ABS, MOD, ROUND 등|
|날짜형 함수|DATE 타입의 값을 연산한다.|SYSDATE/GETDATE 등|
|변환형 함수|문자, 숫자, 날짜형 값의 데이터 타입을 변환한다.|TO_NUMBER, TO_CHAR, TO_DATE 등|
|NULL 관련 함수|NULL을 처리하기 위한 함수|NVL/ISNULL, NULLIF 등|  

이러한 단일행 함수는 다음과 같은 특징을 가지고 있다.  

#####  SELECT, WHERE, ORDER BY 절에 사용 가능하다.  

1. 각 행(ROW)들에 대해 개별적으로 작용하여 데이터 값들을 조작하고, 각각의 행에 대한 조작 결과를 리턴한다.  

2. 여러 인자를 입력해도 단 하나의 결과만을 리턴한다.  

3. 함수의 인자로 상수, 변수, 표현식이 사용 가능하고, 하나의 인수를 가지는 경우도 있지만 여러 개의 인수를 가질 수도 있다.  

4. 특별한 경우가 아니면 함수의 인자로 함수를 사용하는 함수의 중첩이 가능하다.  

#####  ORDER BY 절에 대하여 이해한다.  

SQL 문장으로 조회된 데이터들을 다양한 목적에 맞게 특정 칼럼을 기준으로 행을 정렬하여 출력하는데 사용하는 명령이다. 또한, 기본적으로 오름차순으로 정렬된다.  

다음과 같이 사용할 수 있다.  

```
select 칼럼명 [ALIAS명] from 테이블명 order by 칼럼명
select 칼럼명 [ALIAS명] from 테이블명 order by ALIAS명
select 칼럼명 [ALIAS명] from 테이블명 order by 칼럼순서를나타내는정수
```   
  
실제 아래의 예제와 같이 사용된다.  

```
select name from student order by name desc;
```  

이 경우에 사용된 desc는 내림차순을 의미한다(큰 수를 먼저 출력). 반대로 오름차순(작은 수를 먼저 출력)은 asc를 사용한다.  

또한, 다음과 같이 우선순위를 줄 수 있다.  

```
select name from student order by name desc, sex desc;
```

이 경우에는 name을 이용해 내림차순을 하고, 만약 name의 값이 같은 경우가 존재한다면 같은 값들의 sex를 내림차순으로 정렬하라는 의미를 지닌다.  

##### index 절에 대하여 이해한다.  

색인을 나타내며, 조회할 때 원하는 행을 빠르게 찾을 수 있게 준비해둔 데이터를 말한다. 보통 개념 중심의 전문 서적을 보면 부록으로 단어들이 어디에 있는지 볼 수 있는 색인이 있는 것과 같다.  

만약 DB의 행이 너무 많다면 필요한 단어를 찾는 것에도 많은 시간이 소모될 수 있다.  

우선 아래의 예제를 만들어보자.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL AUTO_INCREMENT,  
  name char(4) NOT NULL,  
  address varchar(50) NOT NULL,  
  department enum('국문과','영문과','컴퓨터공학과','전자공학과','물리학과') NOT NULL,  
  introduction text NOT NULL,  
  number char(255) NOT NULL,  
  PRIMARY KEY (id),  
  UNIQUE KEY idx_number (number) USING BTREE,  
  KEY idx_department (department),  
  KEY idx_department_name (department, address),  
  FULLTEXT KEY idx_introduction (introduction)  
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;  
   
INSERT INTO student VALUES (1, '이숙경', '청주', '컴퓨터공학과', '저는 컴퓨터 공학과에 다닙니다. computer', '0212031');  
INSERT INTO student VALUES (2, '박재숙', '서울', '영문과', '저는 영문과에 다닙니다.', '0512321');  
INSERT INTO student VALUES (3, '백태호', '경주', '컴퓨터공학과', '저는 컴퓨터 공학과에 다니고 경주에서 왔습니다.', '0913134');  
INSERT INTO student VALUES (4, '김경훈', '제천', '국문과', '제천이 고향이고 국문과에 다닙니다.', '9813413');  
INSERT INTO student VALUES (6, '김경진', '제주', '국문과', '이번에 국문과에 입학한 김경진이라고 합니다. 제주에서 왔어요.', '0534543');  
INSERT INTO student VALUES (7, '박경호', '제주', '국문과', '박경호입니다. 잘 부탁드립니다.', '0134511');  
INSERT INTO student VALUES (8, '김정인', '대전', '영문과', '김정인입니다. 대전에서 왔고, 영문과에 다닙니다.', '0034543');
```

예제를 살펴보면 다음과 같다고 느낄 수 있다.  

예제의 '`id` tinyint(4) NOT NULL AUTO_INCREMENT'라는 문장은 뒤에서 'PRIMARY KEY (`id`)'로 사용되어 PRIMARY KEY를 나타내고, '`number` char(255)'는 'UNIQUE KEY `idx_number` (`number`) USING BTREE'로 사용되어 UNIQUE KEY를 나타낸다. 다른 속성들도 이와 같다고 보면 된다.  

이에 대해 위의 예제에서 사용된 키워드를 살펴보도록 하자.  

##### primary key

형태 : PRIMARY KEY (`칼럼명`)  
테이블 전체를 통틀어서 중복되지 않는 값을 지정해야 한다.  
where 문을 이용해서 데이터를 조회할 때 가장 고속으로 데이터를 가져올 수 있다.  
테이블마다 딱 하나의 primary key를 가질 수 있다.  

다음과 같이 사용할 수 있다.  

```
select * from student where id='3'
```  
  
이는 id가 3인 정보의 행을 출력하게 된다.  

##### unique key  

형태 : UNIQUE KEY `이름` (`칼럼명`)   
테이블 전체를 통틀어서 중복되지 않는 값을 지정해야 한다. (== primary key)  
고속으로 데이터를 가져올 수 있다.  
여러개의 unique key를 지정할 수 있다.  

다음과 같이 사용할 수 있다.  

```
select * from student where number=0534543;
```  
  
##### normal key  

형태 : KEY `이름` (`칼럼명`)  
중복을 허용한다.  
primary, unique 보다 속도가 느리다.  
여러개의 키를 지정할 수 있다.  

다음과 같이 사용할 수 있다.  

```
select * from student where department='국문과'
```  
  
또한, normal key는 중복이 가능하기 때문에 중복키 형태를 사용할 수 있다.  
```
select * from student where department='국문과' AND address='제주';
```
  
앞서 중복키로 정의되어 있어 두 개의 키에 해당하는 정보를 출력하는 것이다. 이는 index의 한 형태가 아닌, 하나의 스타일이라고 보면 된다.  

##### Full Text   


mysql의 기본설정(ft_min_word_len)이 4로 되어 있기 때문에 최소 4글자 이상을 입력하거나 이 값을 조정해야 한다.  

> mysql은 전문 검색 엔진이 아니기 때문에 한글 검색이 잘 안된다.  
> 전문검색엔진으로 lucene, sphinx 참고  
> 스토리지 엔진 중 myisam에서만 사용가능  

다음과 같이 사용할 수 있다.  

```
SELECT introduction, MATCH(introduction) AGAINST('영문과에') FROM student WHERE MATCH (introduction) AGAINST('영문과에');
```  
  
이는 긴 데이터에서 원하는 데이터를 찾아올 때 사용된다. 위의 경우는'영문과에'라는 문장이 들어간 내용을 출력하라는 의미를 지닌다.  

지금까지 설명한 index는 다음과 같은 경우에 사용하는 것이 바람직하다.  

> 자주 조회되는 칼럼에 적용  
> 조회 시 오랜시간을 소모하는 컬럼에 적용  
> 데이터가 긴 경우 인덱스를 사용하지 않는다.  
  
##### 조인(Join)절에 대하여 이해한다.  

보통 데이터베이스는 하나의 테이블이 아닌 여러 개의 테이블을 사용하는 경우가 많다. 하나의 테이블로 정보를 수용하는 것이 어렵고, 비효율적이기 때문이다.  

그래서 데이터베이스는 테이블을 분할하고, 각 테이블의 관계를 설정할 수 있다.  

사용할 예제는 다음과 같다.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL,  
  name char(4) NOT NULL,  
  sex enum('남자','여자') NOT NULL,  
  address varchar(50) NOT NULL,  
  distance INT NOT NULL,  
  birthday datetime NOT NULL,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
     
INSERT INTO student VALUES (2, '박재숙', '남자', '서울',  10, '1985-10-26 00:00:00');  
INSERT INTO student VALUES (1, '이숙경', '여자', '청주', 200, '1982-11-16 00:00:00');  
INSERT INTO student VALUES (3, '백태호', '남자', '경주', 350, '1989-2-10 00:00:00');  
INSERT INTO student VALUES (4, '김경훈', '남자', '제천', 190, '1979-11-4 00:00:00');  
INSERT INTO student VALUES (8, '김정인', '남자', '제주', 400, '1990-10-1 00:00:00');  
INSERT INTO student VALUES (6, '김경진', '여자', '제주', 400, '1985-1-1 00:00:00');  
INSERT INTO student VALUES (7, '박경호', '남자', '영동', 310, '1981-2-3 00:00:00');  
```

위의 예제를 살펴보면 '제주'와 '400'이 중복된다는 것을 알 수 있다. 이는 사소할 수 있지만 큰 데이터베이스의 경우에는 큰 문제가 될 수 있다.  

그래서 이를 다음과 같이 분할할 수 있다.  

```
DROP TABLE IF EXISTS student;  
CREATE TABLE student (  
  id tinyint(4) NOT NULL,  
  name char(4) NOT NULL,  
  sex enum('남자','여자') NOT NULL,  
  location_id tinyint(4) NOT NULL,  
  birthday datetime NOT NULL,  
  PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;  
   
DROP TABLE IF EXISTS location;  
CREATE TABLE location (  
id  tinyint UNSIGNED NOT NULL AUTO_INCREMENT ,  
name  varchar(20) NOT NULL ,  
distance  tinyint UNSIGNED NOT NULL ,  
PRIMARY KEY (id)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;;  
  
INSERT INTO location VALUES (1, '서울', 10);  
INSERT INTO location VALUES (2, '청주', 200);  
INSERT INTO location VALUES (3, '경주', 255);  
INSERT INTO location VALUES (4, '제천', 190);  
INSERT INTO location VALUES (5, '대전', 200);  
INSERT INTO location VALUES (6, '제주', 255);  
INSERT INTO location VALUES (7, '영동', 255);  
INSERT INTO location VALUES (8, '광주', 255);  
  
INSERT INTO student VALUES (1, '이숙경', '여자', 1, '1982-11-16 00:00:00');  
INSERT INTO student VALUES (2, '박재숙', '남자', 2, '1985-10-26 00:00:00');  
INSERT INTO student VALUES (3, '백태호', '남자', 3, '1989-2-10 00:00:00');  
INSERT INTO student VALUES (4, '김경훈', '남자', 4, '1979-11-4 00:00:00');  
INSERT INTO student VALUES (6, '김경진', '여자', 5, '1985-1-1 00:00:00');  
INSERT INTO student VALUES (7, '박경호', '남자', 6, '1981-2-3 00:00:00');  
INSERT INTO student VALUES (8, '김정인', '남자', 5, '1990-10-1 00:00:00');  
```

srudent의 'address'와 'distance'를 'location_id'로 묶인 것을 알 수 있다. 예를 들어 '이숙경'은 'location_id'가 1이므로, '서울'에 살고, 거리는 10이라는 것을 알 수 있는 것이다.  

그런데 여기서 중요한 것은 사용자의 입장에서 두 테이블의 관계성을 알기 어렵다. 그래서 사용되는 것이 'JOIN'이다.  

JOIN은 테이블간의 관계성에 따라서 복수의 테이블을 결합, 하나의 테이블인 것처럼 결과를 출력한다.  

JOIN의 종류는 다음과 같다.  

* OUTTER JOIN : 매칭되는 행이 없어도 결과를 가져오고 매칭되는 행이 없으니 그 결과를 NULL로 표시한다.   
* INNER JOIN : 조인하는 두 개의 테이블 모두에 데이터가 존재하는 행에 대해서만 겨과를 가져온다.  

일반적인 경우 많이 사용하는 것은 'LEFT JOIN'이다. 이는 OUTTER JOIN의 일종으로, 다음과 같이 사용한다.  

```
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id;
```
  
여기서 사용된 문법을 살펴보면, 'AS'는 ALIAS의 약자이다. 즉, 'student AS s'는 student 테이블의 별명을 s로 한다는 것이다.  

그래서 뒤에 따라오는 'location AS l'과 LEFT JOIN하는 것이다. 그래서 's.name, s.location_id, l.name AS address'를 이용해 세 결과를 address로 설정한다는 것이다.  

또한, 'ON'이라는 키워드를 이용해 student라는 테이블에 존재하는 location_id라는 칼럼과 location 테이블의 id 값이 같다라는 것을 기술한다.  

이는 다음에 student 테이블의 칼럼을 가져올 때 'location_id'에 해당하는 내용을 location 테이블의 id를 붙인다는 의미를 지니게 된다.  

마지막으로 'OUTTER JOIN'과 'INNER JOIN'의 차이를 다음의 예제를 통해 살펴보자.  

```
DELETE FROM location WHERE name='제주'; 
```  
  
제주도라는 데이터를 삭제하면,

```
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s LEFT JOIN location AS l ON s.location_id = l.id; 
```
  
검색 결과에서 '박경호'가 빠지지 않고 'NULL'을 출력하게 된다.

```
SELECT s.name, s.location_id, l.name AS address, l.distance  FROM student AS s INNER JOIN location AS l ON s.location_id = l.id;
```  
  
그러나 INNER JOIN은 '박경호'라는 데이터를 아예 출력하지 않는다는 차이점이 있다.  

