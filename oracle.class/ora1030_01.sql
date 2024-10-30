-- dual 가상 테이블
select sysdate from dual;

-- employees 테이블 안에 hire_date 컬럼 출력
select hire_date+1, hire_date -1, hire_date from employees;

-- 날짜 범위 검색 가능, 정렬
select hire_date -30, hire_date from employees;
select emp_name,hire_date from employees where hire_date >= '020101' and hire_date <='041231'
order by hire_date desc;

select emp_name,hire_date from employees where hire_date between '020101' and '041231'
order by hire_date desc;

--like
select emp_name from employees where emp_name like '___a%';
select emp_name from employees where emp_name like '%a_';

-- 정렬 desc 내림차순 정렬(null 값이 제일 위로 온다), asc 오름차순 정렬(null 값이 제일 밑으로 온다)
select department_id from employees order by department_id desc;

-- 월급 내림차순 정렬
select emp_name, salary from employees order by salary desc;

-- students테이블에서 total 역순 정렬
select no,name,total from students order by total desc;

-- hire_date 기준, 순차정렬
select hire_date from employees order by hire_date asc;
select name,kor,eng,math from students order by kor desc, eng desc;

-- 한국어 내림차순 정렬
select name from students order by name desc;

-- 입사일이 빠른 순으로 정렬하는데, 이름은 역순으로 정렬
select hire_date, emp_name from employees order by hire_date asc, emp_name desc;

-- 절대값
select-10, abs(-10) as abs from dual; 
select kor,kor-eng,abs(kor-eng) from students;


-- floor 소수점 이하버림
select 3.141592, floor(3.141592) from dual;
-- 소수점 첫째 자리에서 반올림
select 34.5678, round(34.5678) from dual;
-- round 반올림,자리수 범위지정 가능
-- 소수점 두번째 자리까지 출력
select 34.5678, round(34.5678,2) from dual;
-- 소수점 앞에서 반올림 
select 34.5678,round(34.5678,-1) from dual;
-- trunc:버림, 소수점자리 지정가능
select 34.5678,trunc(34.5678,2) from dual;
select 34.5678,trunc(34.5678,-1) from dual;
-- 소수점 이하 올림
select 34.5678, ceil(34.5678) from dual;

-- mod 나머지
select 27/2,mod(27,2) from dual;
select 30/3, mod(30,3) from dual;

-- 사원번호가 홀수인 사원번호 출력
select employee_id,emp_name from employees where mod(employee_id,2)=1;


-- 최종 연봉 : 월급*12+(월급*12)*커미션, 소수점 두번째 짜리에서 반올림
select salary, round(salary*12+((salary*12)*nvl(commission_pct,0))*1381.86795,1) as ysalay from employees;








-- 시퀀스 : 자동으로 번호 부여
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

- 현재 시퀀스 번호 출력
select stu_seq.currval from dual;

-- 시퀀스 번호생성
select stu_seq.nextval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2(30),
bhit number(10),
bdate date
);

insert into board
values(1,'제목입니다','내용입니다.','aaa',1,sysdate);
insert into board
values(2,'제목입니다','내용입니다.','bbb',2,sysdate);

insert into board
values(stu_seq.nextval,'제목입니다','내용입니다.','aaa',1,sysdate);

select * from board;
commit;

delete from board where bno=14;

create sequence board_seq
start with 14   -- 시작번호
increment by 1  -- 증가값
minvalue 1      -- 최소값
maxvalue 9999   -- 최대값
nocycle         -- cycle: 최대값을 넘어가면 다시 1부터시작하는 것 / nocycle: 반복하지 않는 것
nocache         -- 메모리에 시퀀스 값을 미리 할당할지 정하는 것
;


insert into board values(board_seq.nextval,'제목14','내용14','aaa',1,sysdate);

select * from board;

update board set btitle = '제목을 다시 변경' where bno=14;

commit;

drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob,      -- 대용량 글자타입
id varchar2(20),
bgroup number(4),   -- 답변달기 그룹핑
bstep number(4),    -- 답변달기 경우 순서정의
bindent number(4),  -- 답변달기 들여쓰기
bhit number(10),    -- 조회수
bdate date          -- 등록일
);

select board_seq.currval from dual;

insert into board
values(board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100 -> 101
-- 101,'홍길순',99,99,90,total,avg,rank,날짜
create sequence students_seq
start with 101
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;
insert into students
values(students_seq.nextval,'홍길순',99,99,90,(99+99+90),(99+99+90)/3,0,sysdate);

update students set name='유관순' where no=102;

select * from students order by no asc ;
select s.*, round(avg,2) from students s order by no desc;


select dept_seq.nextval from dual;


-- s_seq 생성
-- 시작 1,증분1, 최대값 99999
create sequence s_seq
start with 1
increment by 1
minvalue 1
maxvalue 99999
nocycle
nocache
;
select s_seq.nextval from dual;
select emp_seq.nextval from dual;
select emp_seq.currval from dual;




-- 타입
-- 문자형, 숫자형, 날짜형
-- char,varchar2, nchar,nvarchar2,long,clob
-- char,varchar2 : 한글 문자 입력시 3바이트 사용
-- varchar2(6) : 한글 2글자 입력 가능
-- nvarchar2(5) : 한글 입력을 5자리까지 입력 가능
-- number
-- date, timestamp
-- date- 초까지 입력, timestamp - 밀리세컨드까지 입력



select '홍길동' from dual;
select length('홍길동')from dual;
--lengthb: 바이트크기
select lengthb('홍길동') from dual;

select length(name) as a from students order by a asc;

-- 합계가 200점 이상이면서, 번호가 10이상,50이하이면서 이름의 2번째 자리가 e인 학생 출력
select * from students where total>=200 and no>=10 and no<=50 and name like'_e%';

select * from students where total>=200;

select * from(select*from students where total>=200) where name like '_e%' and no>=30;

rollback;

select * from students;

select no,name, total,rank from students;

-- 등수 함수 rank() over(기준점)입력
select no, rank() over(order by total desc) as 등수 from students;
select ranks from (select no,rank() over(order by total desc) as ranks from students);

select * from students;

select no,name,total,rank from students order by total desc;


-- 수정 : update
update students a
set rank=(select ranks from(select no, rank() over(order by total desc) as ranks from students)b
where a.no=b.no);

update students a
set rank =1
where a.no =101;

select * from students order by rank asc;



rollback;

select no,rank()over(order by total desc)as ranks from students;

update students a
set rank=(select ranks from (select no,rank()over(order by total desc)as ranks from students)b
where a.no=b.no);


-- 사원번호가 높은 순으로 등수를 생성하시오
select employee_id,emp_name,rank()over(order by employee_id desc)as ranks from employees;

--emp2 테이블 복사
create table emp2 as select * from employees;

select rank()over(order by employee_id desc) from employees;

desc emp2;

--테이블 컬럼 추가
alter table emp2 add rank number(4);

desc emp2;


update emp2 e 
set rank=(select ranks from(select employee_id, rank() over(order by employee_id desc) as ranks from employee)e2
where e.employee_id=e2.employee_id);

select * from emp2;


-- 컬럼의 순서 변경
-- emp_name뒤에 rank컬럼 배치
alter table emp2 modify email invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;
alter table emp2 modify JOB_ID invisible;

-- 컬럼을 나타내기
alter table emp2 modify email visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;
alter table emp2 modify JOB_ID visible;

select * from emp2;

-- 컬럼 삭제
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column hire_date;
alter table emp2 drop column salary;
alter table emp2 drop column commission_pct;
alter table emp2 drop column retire_date;
alter table emp2 drop column create_date;
alter table emp2 drop column update_date;

select * from emp2;

alter table emp2 add department_name varchar2(80);

select * from emp2;

select * from departments;

select department_id, department_name from emp2;
select department_id, department_name from departments;


update emp2 e
set e.department_name ='배송부'
where e.department_id = 50;

-- 부서명 입력
update emp2 a set a.department_name=
(select d from (select department_id, department_name as d from departments)b 
where a.department_id=b.department_id);


select department_id,department_name from emp2;





create table stu as select * from students;

desc stu;

alter table stu drop column avg;
select * from stu;

-- total, avg,  rank컬럼 추가
alter table stu add total number(10);
alter table stu add avg number(10);
alter table stu add rank number(10) ;

select * from stu;

-- sdate 컬럼 숨김,나타내기
alter table stu modify sdate invisible;
alter table stu modify sdate visible;

-- 합계
update stu a set a.total =
(select total from (select name,total from students)b
where a.name = b.name);
-- 평균
update stu set avg=(kor+eng+math)/3;
-- 랭크
update stu a set rank=
(select ranks from(select no,rank()over(order by total desc)as ranks from students)b
where a.no = b.no);


select * from students order by total desc;
commit;









----  날짜 함수
-- 현재 날짜 : sysdate
select sysdate from dual;
select sysdate -1 from dual;
select sysdate +30 from dual;

create table datetable(
no number(4),
predate date,
todat date,
nextdate date
);
-- 회원 가입 1달치, 6개월치, 1년치
insert into datetable
values(1,sysdate-30,sysdate,sysdate+180);

select * from datetable;
select no, predate,todat as 가입일, nextdate as 만기일 from datetable;

select * from member;

select id,name, mdate, round(sysdate-mdate) from member
where sysdate>=mdate+180;

-- 입사일 현재날짜와 입사일 몇일 지났는지 출력
-- employees, hire_date
select hire_date from employees;
select hire_date,round(sysdate-hire_date) from employees;

--15일 이상이면 1달을 올림, 15일 미만이면 일을 초기화
select hire_date,round(hire_date,'month') from employees;
-- 일의 숫자를 1로 초기화
select hire_date, trunc(hire_date,'month') from employees;

-- 입사일, 현재일 기준의 달수
-- months_between : 두 일자 가운데 지나간 달수를 알려줌
select hire_date,sysdate,round(months_between(sysdate,hire_date)) as 달수 from employees;

select hire_date,sysdate,round(sysdate-hire_date)as 일수 from employees;

select hire_date,add_months(hire_date,3) from employees;
-- next_day: 다음주 수요일 날짜를 알려줌
select sysdate,next_day(sysdate,'수요일')from dual;
select sysdate,next_day(sysdate,'토요일')from dual;


-- last_date : 그 달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date) from employees;
select sysdate, last_day(sysdate) from dual;


-- 타입 변경
-- to_char: 날짜형, 숫자형을 문자형으로 변환
-- to_date: 문자형을 날짜형으로 변환
-- to_number: 문자형ㅇ르 숫자형으로 변환
select sysdate from dual;
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') from dual;

select hire_date from employees;
select to_char(hire_date,'yyyy-mm-dd') from employees;

select * from member where id ='aaa' and pw ='1111';

update member set id = 'parkmk0615',pw='1111',name='박민규',email='parkmk0615@naver.com' where pw = 6216;
commit;
select * from member;

select * from member where id = 'eee';