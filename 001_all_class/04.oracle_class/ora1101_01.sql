--  입사일과 입사일의 마지막 달 출력
select hire_date, last_day(hire_date) from employees;

-- 가입일
select sdate from students;
-- 가입 후 1년 후 날짜 출력
select sdate, add_months(sdate,12) from students;
-- 가입일이 6개월 이내의 회원만 출력
select sdate,add_months(sdate,-6) from students;
-- 현재일 기준으로 가입일이 6개월 이내의 회원만 출력
select sdate from students where sdate >= add_months(sysdate,-6) order by sdate asc;
-- 월별로 가입 인원을 출력
select substr(last_day(mdate),1,5) as md, count(*) from member group by last_day(mdate) order by md asc;
-- employees 테이블에서 부서별(department_id) 인원수 출력
select department_id,count(*) from employees group by department_id;


--구조와 내용까지 똑같은 형태로 복사
create table emp3
as
select * from employees;
--구조만 똑같은 형태로복사
create table emp4
as
select * from employees where 1=2;

-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
insert into emp4 select * from employees;
-- 테이블 구조가 있는 상태에서 특정 데이터만 입력하는 방법
insert into emp4(employee_id,emp_name,hire_date) select employee_id,emp_name,hire_date from employees;

-- create: 생성, alter: 변경, drop: 테이블 삭제


select * from emp4;
alter table emp4 add hire_date3 date;
-- 컬럼변경 
alter table emp4 modify email varchar2(70);
alter table emp4 modify email varchar2(50);

-- 컬럼 타입 변경 -> 컬럼 안의 데이터가 null이면 가능
alter table emp4 modify email number(4);
-- 다른 타입인 경우 데이터를 null로 변경한 후 타입 변경 가능
alter table emp4 modify emo_name number(20);


-- email 컬럼에 employee_id 값을 복사
update emp4 set email = employee_id;

-- employee_id 값을 phone_number 입력하시오
update emp4 set phone_number = employee_id;

select * from emp4;
update emp4 set phone_number='198a' where employee_id=198;

commit;

-- 문자형 타입을 숫자형 타입에 복사
-- 내부 데이터가 모두 숫자형이기에 가능
-- 문자가 포함되어 있으면 불가능
update emp4 set manager_id=phone_number;


-- 컬럼 이름 변경
desc emp4;
alter table emp4 rename column phone_number to p_number;

--속성 변경 가능
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제
alter table emp4 drop column hire_date2;

-- 테이블 삭제
drop table emp3;

-- 테이블 이름 변경
rename emp4 to emp44;


-- 
select * from departments;


-- primary key : 중복,null 불가능
-- unique : 중복 불가능
-- not null : null 불가능
-- default : 값이 입력 되지 않았을때, 기본으로 입력되는 값
create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30)not null,
nicname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in ('Male','Female')),
email varchar2(20),
bdate date default sysdate
);
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) 
values('aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate);

insert into bmember(id,pw,name,nicname,age,gender,email) 
values('bbb','2222','유관순','관순스',20,'Female','bbb@bbb.com');
-- check : Male,Female 외에는 입력 불가능
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) 
values('ccc','1111','이순신','순신스',20,'Male','ccc@ccc.com',sysdate);

--not null / 빈공백은 허용
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) 
values('ddd',' ','강감찬','감찬스',20,'Male','ddd@ddd.com','2024/01/01');

-- primary key : 중복 불가능, null 불가능
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) 
values('eee',' ','김구','구스',20,'Male','eee@eee.com','2024/02/21');

commit;

create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 
values(1,'홍','01',01);
insert into emp3 
values(2,'유','02',02);
insert into emp3(ename,job,deptno) 
values('이','03',03);
--unique : 중복 불가능
insert into emp3 
values(2,'강','04',04);

select * from emp3;


-- member 테이블에 primary key 추가하기
-- constraint id_pk :이름 설정
alter table member add constraint id_pk primary key(id);

select * from member;
--primary key : 중복 불가, null 불가
insert into member 
values('fff','1111','홍길자','aaa@aaa.com','123-456-789','Female','golf',sysdate);

-- primary key 삭제
alter table member drop constraint id_pk;

alter table member add constraint id_pk primary key(id);




create table board(
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhint number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);

insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);

insert into board values(
board_seq.nextval,'제목3','내용3','aaa',board_seq.currval,0,0,0,sysdate,''
);

insert into board values(
board_seq.nextval,'제목5','내용5','ddd',board_seq.currval,0,0,0,sysdate,''
);

commit;

select * from board;
select * from bmember;


-- foreign key 추가,변경



select bno,btitle,bcontent,nicname,email, bgroup, bstep, bindent, bhint,bfile from board,bmember
where board.id = bmember.id; -- bmember.id: primary key,board.id :foreign key ;

-- join
select employee_id, emp_name, email, salary, employees.department_id,department_name
from employees, departments where employees.department_id = departments.department_id;

select department_id,department_name from departments where department_id=20;




