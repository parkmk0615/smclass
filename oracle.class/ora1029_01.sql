create table students(
stuno number(4),
name varchar(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

insert into students
values(1,'홍길동',100,100,100+100,sysdate);

commit;

select * from students;
-- 특정 컬럼을 입력하면 해당 컬럼만 출력 / *는 모든 컬럼 검색
select name,sdate from students;

-- 특정 컬럼만 데이터 추가하기
insert into students(stuno,name)
values(2,'유관순');

select * from employees;

-- 테이블 생성 후, 테이블 내용 복사
create table emp2 as select *from employees;
select * from emp2;
select count(*) from emp2; -- emp2 테이블의 튜플 갯수

select * from emp2;
--테이블 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
select * from member;
select * from member2;
insert into member2 select* from member;
commit;


--컬럼데이터 타입, 길이 변경

-- alter 변경 member 테이블 no 컬럼의 타입 길이 변경
alter table member modify no number(10);

update member set no='';
commit;
alter table member modify no varchar2(10);
desc member;

-- 컬럼명 변경
alter table member rename column NO to memberNo;


--테이블 구조
desc employees;

-- date는 날짜까지, 타임 스탬프는 날짜,시,분,초까지 저장 가능

--employees 테이블에서 사원번호, 사원이름, 입사일(hire_date) 출력
select *from employees;
select employee_id, emp_name,hire_date from employees;

--연산자 : 산술연산자 +,-,*,/
select kor,eng, (kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from employees;

select concat(emp_name,email) from employees;
select employee_id||emp_name from employees;

-- 달러 환산
select salary*1384 from employees;
--문자로 변환, 천 단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

-- null 값 검색: is null
select * from stu where name is null;

select * from employees;
select commission_pct from employees where commission_pct is not null;

select salary from employees;
select salary,salary*12 from employees;
select salary,salary*12,salary*12*1384 from employees;
-- 커미션이 없는 사원은 null 값이 있는데, null 값에는 +-*/하면 null값이 나온다
select salary, salary*12, salary*12+(salary*12)*commission_pct*0.01 from employees;

-- 컬럼명 별칭 사용 as
select salary, salary*12 as 연봉, salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as real_yearsalary from employees;

-- nvl() 함수
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu; -- nvl(kor,0) kor에 null이 있으면 0으로 표시

--컬럼명을 이름 국어 영어 수학 합계 입력일 별칭 사용
select * from students;
select no as 번호, name as 이름, kor as 국어, eng as 영어, math as 수학, total as 합계, avg as 평균, rank as 등수 from students;

-- 사원번호, 이름,이메일을 합쳐서 출력
select * from employees;
select employee_id || emp_name || email from employees;
select emp_name || ' is a ' || job_id from employees;
select concat(concat(employee_id,emp_name),email) from employees;


-- 중복제거
select distinct(department_id) from employees;
-- 정렬 asc,desc
select distinct(department_id) from employees order by department_id asc;

-- job_id를 중복 제거 해서 출력하시오
select distinct(job_id) from employees;

--문자열 자르기 substr(job_id,0,2) job_id의 0번째,1번째 출력
select substr(job_id,0,2) from employees;
-- job_id의 4번째 컬럼부터 중복을 제거한 상태에서 가져옴
select distinct(substr(job_id,4)) from employees;

-- where : 조건비교연산자
select * from employees;
select * from employees where manager_id = 124;
select * from employees where job_id = 'ST_CLERK';
select * from employees where employee_id > 100;

-- students 테이블에서 합계가 250점 이상인 것만 출력
select * from students where total >= 250;

-- 합계가 250이상이고, 국어점수가 90점 이상인 것만 출력
select * from students where total >= 250 and kor >= 90;

-- 영어 점수가 70점이상, 90점이하인 것만 출력
select * from students where eng between 70 and 90;

-- 월급이 5000이상, 8000이하인 것만 출력
select * from employees where salary between 5000 and 8000;

-- 월급이 7000이 아닌 것을 모두 출력
select * from employees where salary != 7000;

--부서(depaerment_id)가 50인것의 개수 출력
select count(*) from employees where department_id = 50;

--null 값 검색
select count(*) from employees where department_id is null;

-- 급여가 4000이하인 사원의 사원번호, 사원명, 급여컬럼을 출력
select employee_id as 사원번호, emp_name as 사원명, salary as 급여 from employees where salary <= 4000;

--숫자인 경우 비교 연산자 가능, 날짜 비교 연산자가 가능
select emp_name,hire_date from employees;

select emp_name,hire_date from employees where hire_date >= '2002/01/01';

-- 1999년 12월 31일 이전에 입사한 사람을 출력
select emp_name,hire_date from employees where hire_date >= '1999/12/31';

-- 2001년 01월 01일부터 2004년 12월31일까지 출력
select emp_name,hire_date from employees where hire_date between '2001/01/01' and '2004/12/31';

--국어 점수가 90점 이상 또는 영어점수가90점 이상인것을 출력
select count(*) from students where kor >= 90 or eng >= 90;
select count(*) from students where kor >= 90 and eng >= 90;
select count(*) from students where not kor >= 90;

-- 부서번호(department_id)가 80번이면서, job이 man인 경우
select * from employees;
select * from employees where department_id = 80 and job_id like '%MAN%';
select * from employees where department_id = 80 and substr(job_id,4)='MAN';

--0.2,0.3,0.5만 출력
select commission_pct from employees where commission_pct is not null;
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct =0.5;
select commission_pct from employees where commission_pct in(0.2,0.3,0.5);

--사원번호(employee_id)가 110,120,130 출력
select employee_id from employees where employee_id in (110,120,130);
select employee_id from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;

-- 150-170 사원번호 출력
select * from employees where employee_id > 150 and employee_id <170;
-- between(~~이상~~이하)
select * from employees where employee_id between 150 and 170;

select hire_date from employees;
select hire_date from employees where hire_date in('2004/02/17','2002/06/07');

select hire_date from employees where hire_date between '20020617' and '20041231';

-- job의 MAN 출력하시오
select job_id from employees where substr(job_id,4)='MAN';
--like 연산자
select job_id from employees where job_id like '%MAN%';
select job_id from employees where job_id like 'ST%';

-- EMP_NAME에서 'a'가 포함된 이름 출력
select EMP_NAME from employees where emp_name like '%a%';

--2번째 자리에 't'가 들어가 있는 이름 출력
select emp_name from employees where emp_name like '_t%';
--4번째 자리에 'v'가 들어가 있는 이름 출력
select emp_name from employees where emp_name like '___v%';

-- 뒤에서 2번째 자리에 l이 들어가 있는 이름 출력
select emp_name from employees where emp_name like '%l_';

-- 첫번째 자리에 'D'가 들어가 있는 이름 출력
select emp_name from employees where emp_name like 'D%';


