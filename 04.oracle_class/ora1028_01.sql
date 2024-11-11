-- ###########                 system관리자에서 진행                  #####################
-- 주석
-- 실행 단축키 f9
-- 계정 이름 앞에 c## 생략 코드
-- alter session set "_ORACLE_SCRIPT" = true; (c##을 붙여야 되는 부분을 해제)

-- 사용자 생성
create user ora_user identified by 1111;

--  권한 부여: 접근 권한, 리소스 권한, db생성 권한
grant connect,resource,dba to ora_user;



























-- 권한 해제
revoke connect,resource,dba from ora_user;

-- 사용자 계정 삭제
drop user ora_user;


create user ora_user identified by 1111;
grant connect, resource, dba to ora_user;

