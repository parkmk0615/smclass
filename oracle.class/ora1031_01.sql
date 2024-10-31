select * from member;

update member set pw =1111 where name='박민규';

commit;

select * from member;

update member set pw='1111' where id='Towell';

commit;

select * from member;

select sysdate-1 from dual;

select hire_date,round(hire_date,'month') from employees;

select hire_date,trunc(hire_date,'month') from employees; 

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip요금제로 변경하면 다음 달 1일부터 혜택이 주어짐
select sysdate,add_months(trunc(sysdate,'month'),1) from dual;

-- 입사일 기준 다음 달 1일부터 혜택을 주겠다고 함
-- 입사일 다음 달 1일 출력
select * from employees;
select hire_date as 입사일,add_months(trunc(hire_date,'month'),1) as 입사일_다음달 from employees;

-- 입사일 기준, 1년 후 날짜 출력
select hire_date as 입사일, add_months(hire_date,12) from employees;

-- 입사일 기준, 1년 후 날짜와 그 달의 마지막 날짜 출력
select hire_date, add_months(hire_date,12), last_day(hire_date) from employees;

-- 입력일 기준, 1년 후 마지막 날짜가 9월 30일 또는 10월 31일인 학생 출력
select name, last_day(add_months(sdate,12)) as lastday from students 
where last_day(add_months(sdate,12)) in ('240930','250930','241031','251031');




select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

-- systimstamp : 년월일시분초
-- extract함수 : 년월일시분초 만 분리해서 가져오는 함수
select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

-- substr 함수 : 문자에서 시작위치, 가져올 개수
select sysdate, substr(sysdate,4,2) from dual;

select sdate from students
where substr(sdate,4,2)=8;

select sdate, last_day(sdate+365)as sdate2 from students
where substr(last_day(sdate+365),4,2) in (6,8,12)
order by sdate2;




-- 날짜 -> 문자 : to_char() ## 날짜 포맷
-- 문자 -> 날짜 : to_date() ## 날짜 사칙연산
-- 숫자 -> 문자 : to_char() ## 천단위, 숫자 앞에 0 을 표시, 통화 표시
-- 문자 -> 숫자 : to_number() ## 천단위 표시 , 천단위 삭제해서 사칙연산

--날짜 형 변환
--date 타입 -> char 타입으로 변경해서 포맷
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day')from dual;
select sysdate,to_char(sysdate,'yy-mm-dd am hh:mi:ss dy')from dual;
select sysdate,to_char(sysdate,'yyyy-mon-dd hh24:mi:ss MON')from dual;

SELECT hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss')from employees;

-- students 테이블의 sdate를 2024/01/01 형태로 출력
select sdate,to_char(sdate,'yyyy/mm/dd') from students;


select kor from students where kor =70;

-- 숫자 타입을 문자 타입으로 변경해서 포맷 천 단위 표시
select salary *1382.86 * 12 from employees;

-- 자릿수 채우기 9: 빈 공백으로 채움, 0: 0으로 채움
-- L : 국가통화기호 사용표시, $:$모양 표시
select to_char(salary*1382.86*12,'999,999,999,999') from employees;
select to_char(salary*1382.86*12,'000,000,999,999') from employees;
select to_char(salary*1382.86*12,'L999,999,999,999') from employees;
select to_char(salary*1382.86*12,'$999,999,999,999') from employees;

select to_char(123456,'0000000000') from dual;
select to_char(123456,'9999999999') from dual;

create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);
-- 숫자형 타입은 숫자 앞에 0 이 있어도 표시가 되지 않음. 문자형 타입에만 가능
-- 천 단위 표시는 숫자형 타입에 입력이 안됨, 문자형 타입에만 가능
insert into chartable values(1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000'));

select * from chartable2;

create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

insert into chartable2 values(3,3000000,3000000,003000000);

commit;


select * from chartable;


-- 숫자형 타입과 문자형(숫자) 타입은 사칙연산 가능
-- 숫자형 타입과 문자 천단위 표시 숫자 타입은 사칙연산 불가능, 천단위 표시는 문자형 타입
-- 숫자형 타입+문자(숫자형) 타입= 두타입 결과값 출력
select kor+kor_char from chartable;
select kor+kor_mark from chartable;


desc chartable;
desc chartable2;





-- 2일 이후의 날짜를 출력해 줘
select to_date('20241031')+2 from dual;
select sysdate+2 from dual;

select to_date('241031')+2 from dual;


select to_date('20231031') from dual;

--number타입 -> 날짜형 타입으로 변경
--문자형 타입 -> 날짜형 타입
select sysdate-to_date('20231030') from dual;
select sysdate-to_date(20231030) from dual; 

-- 문자형-> 숫자형 타입으로 변경
select '20,000' from dual;
-- 천단위 문자형 타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select *from chartable;
select kor,to_number(kor_mark,'999,999,999') from chartable;


insert into chartable values(3,30000,'0030000','3,000,000');
select * from chartable;

-- 숫자형타입 이기에 사칙연산 가능
select kor+to_number(kor_mark,'999,999,999') from chartable;


select department_id from employees;

select department_id from employees where department_id is null;

select commission_pct from employees where commission_pct is null;
select commission_pct from employees where commission_pct is not null;

--월급 *커미션을 계산하시오
select * from employees;
select salary+salary*nvl(commission_pct,0) from employees;


select department_id from employees;
-- null인 경우 : 0 표시
select nvl(department_id,0) from employees;
-- null인 경우 : ceo 표시 숫자형 타입을 문자형 타입으로 변경
select nvl(to_char(department_id),'CEO') from employees;







-- group 함수
-- sum, avg, max,min,count
select salary from employees;
select sum(salary) from employees;
select to_char(sum(salary),'999,999,999') from employees;
select avg(salary) from employees;
-- 소수점 2자리까지 반올림
select round(avg(salary),2) from employees;
select trunc(avg(salary),4) from employees;

-- 최대값, 최소값 
select min(salary) from employees;
select max(salary) from employees;

-- 평균 값보다 월급이 높은 사원출력
select * from employees;
select count(salary) from employees where salary >=6461.83;
select count(salary) from employees where salary >=(select avg(salary)from employees);

-- emo_name: 단일 함수, avg(salary): 그룹 함수
select emp_name, avg(salary) from employees;

-- students 테이블 모든 학생의 kor 점수 합계, 평균, 최대값, 최소값, 중간값을 구하시오
select sum(kor), round(avg(kor),2), max(kor), min(kor), median(kor) from students;

--부서번호가 50인 사원들의 월급의 합계,평균, 최대값,최소값을 출력
select * from employees;
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id =50;

-- 부서번호가 30인 ~~~~
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id =30;

-- group by: 단일 함수를 출력하고 싶을 때, group by에 단일 함수를 입력하면 됨
select department_id, max(salary)from employees group by department_id;


select emp_name,salary from employees;

--107명의 전체 평균 월급
select avg(salary)from employees;
-- 부서번호별 평균 월급
select department_id, round(avg(salary)), max(salary) from employees 
group by department_id order by department_id asc;

-- 평균 월급보다 높은 사람 수를 출력
select * from employees;
select count(salary) from employees where salary >= (select avg(salary) from employees);



-- 수학함수 : abs: 절대값, ceil: 올림, floor: 버림, round: 반올림,trunc:절사, mod: 나머지, power: 제곱, sqrt:제곱근
-- 제곱
select power(3,3),3*3*3 from dual;

-- 문자,숫자형 타입 -> 날짜형 타입 변경 가능
-- 숫자, 날짜형 타입 -> 문자형 타입 변경 가능
-- 문자형 타입 -> 숫자형 타입 변경 가능
-- 날짜형 타입 -> 숫자형 타입 변경 불가능, 형태를 변경해서 문자형으로 변경한 후, 숫자형으로 변경 가능
select 20240101,to_date(20240101) from dual;
select '2',to_number('2')from dual;

select '20240101',to_number('20240101') from dual;
select to_number(to_date('20240101')) from dual;

select sysdate,to_number(sysdate) from dual;

-- 날짜형 -> 문자형으로 변환
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;


-- 년월일 추가하는 법
select sysdate, to_char(sysdate,'yyyy"년"mm"월"dd"일" day') from dual;

select sysdate, to_char(sysdate,'yyyy-mm-dd day') from dual;


-- 문자형 함수
select email, emp_name from employees;

-- 문자형 타입을 합쳐서 +기호를사용해서 합치려고 하면 에러
select emp_name+email from employees;
-- 문자형 타입을 합치려면 || 또는 concat 함수사용
select emp_name||email from employees;
select concat(emp_name,email) from employees;


-- 숫자형 타입 : 사칙연산 계산해서 출력 됨
select kor+eng from students;

-- lower(): 소문자 치환,  upper() 대문자 치환, initcap: 첫글자 대문자 치환
select * from member where lower(name)='bryan';

select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

-- lpad : 왼쪽 자리수 채우기
select 'john',lpad('john',10,'#') from dual;
--rpad : 오른쪽 자리수 채우기
select 'john',rpad('john',10,'#') from dual;

-- trim : 빈 공백 없애기, ltrim : 왼쪽 공백 없애기, rtrim: 오른쪽 공백 없애기
select length('    aaa   '),length(trim('   aaa   ')) from dual;
--replace: 치환
select '   a b c  ',trim('   a b c  '),length(replace('   a b c  ',' ','')) from dual;

-- substr : 특정위치 자르기
select 'abcdefg',substr('abcdefg',0,3),substr('abcdefg',3,2) from dual;

-- 입사일이 3월인 사원을 출력
select emp_name from employees where substr(hire_date,4,2) >= '07';

-- translate 치환
-- 한 글자, 한 글자에 해당되는 단어를 각각의 단어로 치환
-- 순서에 없는 변환 글자는 삭제 처리
select 'axyz',translate('jxyzxkkcyaccx','xyk','ab') from dual;
select 'axyz',replace('jxyzxkkcyaccx','xy','ab') from dual;


-- length() : 문자열 길이
-- students 테이블 name 글자 길이가 5자 이상인 학생만 출력 하시오
select name from students where length(name)>=5;

-- 사원의 월급의 합, 평균을 구하시오
select sum(salary),round(avg(salary)) from employees;
-- 영어 점수의 합,평균, 최대값, 최소값을 구하시오
select sum(eng),round(avg(eng)), max(eng),min(eng) from students;
--students 테이블에서 홍길동, 등록일: 2023년 12월 02일 출력
select name,to_char(sdate,'"등록일 :" yyyy"년"mm"월"dd"일') from students;
