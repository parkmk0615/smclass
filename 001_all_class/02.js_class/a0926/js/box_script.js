//제이쿼리 선언
let num=0;
let num2=0;
$(function(){
  //우측버튼
  $("#right").click(function(){
    //alert("우측버튼");
    if(num>=900){
      alert("끝에 도달했습니다.");
      return false;
    }
    $("#box").stop();
    num+=100;
    num2+=360;
    $("#box").animate({ 
      left: num, "rotate": num2+"deg"
    },1000);
  });



  $("#left").click(function(){
    //좌측버튼
    if(num<=0){
      alert("끝에 도달했습니다.");
      return false;
    }
    $("#box").stop();
    num-=100;
    num2-=360;
    $("#box").animate({
      left:num, "rotate":num2+"deg"
    },1000);
  })

}); //제이쿼리 선언