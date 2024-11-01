desc board;
--닉네임: id_fk, foreign key: id, bmember테이블의 primary key: id 등록
alter table board add constraint id_fk foreign key(id) references bmember(id);
-- foreign key삭제
alter table board drop constraint id_fk;

select * from board;
select * from bmember; -- aaa,bbb,ccc,ddd,eee

-- 'abc' id로 글을 등록하면 등록이 안됨
insert into board values(board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,'');

-- 테이블 생성할때 foreign key 생성
create table board2(
bno number(4) primary key,
btitle varchar2(1000)not null,
bcontent clob,
id varchar2(30),
constraint fk_board2_id foreign key(id) references bmember(id)
);

-- bmember 테이블 id, foreign key로 board,board2에 등록
-- foreign key: 외래키
-- 원본의 primary key 데이터를 지우려면 foerign key의데이터를 모두삭제 해야 삭제 가능 또는 froigen key를 해제 해야가능
-- primary key: 기본키
select * from bmember;

delete from bmember where id='aaa';
delete from board where id='aaa';

select * from bmember;
select * from board;

alter table board drop constraint id_fk;

-- foreign key로 등록이 되면, primary key를삭제할때 foreign key에 데이터가 있으면 삭제가 안됨
-- on delete cascade: priamry key가 삭제가 되면, foreign key로 등록된 모든 글을 삭제시킴 
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;

-- 1. on delete restricted :
-- 기본값 : 입력하지 않을 시, 자식 데이터가 있을경우, 부모 데이터가 삭제가 되지 않음
alter table board add constraint id_fk foreign key(id) references bmember(id);
-- 자식 테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음
delete from bmember where id='aaa';
delete from board where bno=3;

-- 2. on delete cascade :
-- 부모 데이터 삭제시, 자식 데이터 모두 삭제
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;
-- 부모 데이터를 삭제하면, 자식 데이터의 모든 글이 삭제됨
delete from bmember where id ='aaa';
select * from board;

-- 3. on delete set null :
-- 부모 데이터 삭제 시,자식 데이터에 해당 되는 값이 null표시
alter table board drop constraint id_fk foreign key(id) references bmember(id) on delete null;
-- 부모데이터를 삭제하면 자식 데이터의 해당 컬럼만 null로 변경
delete bmember where id='aaa';




delete board where bno=3;

-- check :값의 범위 이외의 값이 오면 에러발생
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female'))
);
--check가 지정되어 있는 컬럼에 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
-- salary의 범위를 벗어나면 에러,Male,Female 이외의 단어 입력시 에러
insert into emp01 values(
2,'유관순',20000,'Female'
);
insert into emp01 values(
3,'이순신',20000,'male'
);


-- default : 아무런 값이 입력되지 않으면 자동으로 입력되는 값 / 문자,숫자,날짜를 넣을 수 있음
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female')),
edate date default sysdate
);
--
insert into emp02(empno,salary,gender) values(1,5000,'Male');

select * from emp02;

commit;


create table mem(
id varchar2(30) primary key,
pw varchar2(20) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date,
gender varchar2(6) check(gender in ('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem values('aaa','1111','홍길동',24,'2000-05-05','Male','golf',sysdate);
insert into mem values('bbb','2222','유관순',24,'2000-06-05','Female','book',sysdate);
insert into mem values('ccc','1111','이순신',23,'2001-07-25','Male','game',sysdate);

commit;

select count(*),department_id, from employees
where department_id=50 
group by department_id;

-- employees테이블 부서별 개수, 부서번호, 부서이름, 그룹 함수
select count(*) as no,a.department_id as dept,department_name as deptname 
from departments a,employees b
where a.department_id = b.department_id and a.department_id=50
group by a.department_id, department_name;

select * from students;
desc mem;
insert into mem(id,pw,name,age,birth,gender,hobby) values('ddd','1111','강감찬',22,'20220312','Male','game');
rollback;

commit;
select students_seq.nextval from dual;
delete from students where name='김유신';