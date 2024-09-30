// 1. ajax를 사용해서 데이터 가져오기
var id_num;
let count =1;
let temp=0  ;
let tr_this;
$(function(){
  
  $.ajax({ //ajax
    url:"js/stuData.json",
    type:"get",
    data:"",
    dataType:"json",
    success:function(data){
      console.log(data);
      let s_data="";
      for(var i = 0; i<data.length; i++){
        count++;
        
        let total = data[i].kor+data[i].eng+data[i].math;
        let avg= (total/3).toFixed(2);
         s_data += "<tr id= '"+data[i].no+"'>"
         s_data += "<td>"+data[i].no+"</td>"
         s_data += "<td>"+data[i].name +"</td>"
         s_data += "<td>"+data[i].kor +"</td>"
         s_data += "<td>"+data[i].eng +"</td>"
         s_data += "<td>"+data[i].math +"</td>"
         s_data += "<td>"+total+"</td>"
         s_data += "<td>"+avg+"</td>"
         s_data += "<td><button class='updateBtn'>수정</button>"
         s_data += "<button class ='delBtn'>삭제</button></td>"
         s_data += "</tr>"
       }
      $("#tbody").html(s_data);
    },
    error:function(data){
      alert("실패");
    }
    
  }) //ajax

  $(document).on("click","#create",function(){
    if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
      alert("데이터를 입력하셔야 됩니다.");
      return false;
    }

    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());

    let total = kor+eng+math;
    let avg= (total/3).toFixed(2);
    let s_data="";
    s_data += "<tr id='"+count+"'>"
    s_data += "<td>"+count+"</td>"
    s_data += "<td>"+name +"</td>"
    s_data += "<td>"+kor +"</td>"
    s_data += "<td>"+eng +"</td>"
    s_data += "<td>"+math +"</td>"
    s_data += "<td>"+total+"</td>"
    s_data += "<td>"+avg+"</td>"
    s_data += "<td><button class='updateBtn'>수정</button>"
    s_data += "<button class='delBtn'>삭제</button></td>"
    s_data += "</tr>"

    //데이터 지우기
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    $("#tbody").prepend(s_data);

    count++;
  })//create문
  
  $(document).on("click",".delBtn",function(){
   id_num = $(this).closest("tr").attr("id");
   if(confirm("삭제하시겠습니까")){
    $("#"+id_num).remove();
   }
  }) //delBtn문

  $(document).on("click",".updateBtn",function(){
    
    //수정버튼 연속 클릭 막는 문장
    if(temp==1){
      alert("수정완료 또는 수정 취소 버튼을 먼저 클릭하셔야 합니다.");
      return false;
    }
    $(this).css({"color":"red","font-weight":"600"});

    id_num = $(this).closest("tr").attr("id");
    console.log("id: "+id_num);
    
    let u_data = $(this).parent().prev().prev().prev();
    $("#name").val(u_data.prev().prev().prev().text());
    $("#kor").val(u_data.prev().prev().text());
    $("#eng").val(u_data.prev().text());
    $("#math").val(u_data.text());

    $("#create, #update, #updateCancel").toggle();
    temp=1;
  }) // updateBtn문

  $(document).on("click","#update", function(){
    $(this).css({"color":"white","font-weight":"600"});

    if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
      alert("데이터를 입력하셔야 됩니다.");
      return false;
    }

    
    let name = $("#name").val();
    let kor = Number($("#kor").val());
    let eng = Number($("#eng").val());
    let math = Number($("#math").val());
    
    let total = kor+eng+math;
    let avg= (total/3).toFixed(2);
    let s_data="";
    s_data += "<td>"+id_num+"</td>"
    s_data += "<td>"+name +"</td>"
    s_data += "<td>"+kor +"</td>"
    s_data += "<td>"+eng +"</td>"
    s_data += "<td>"+math +"</td>"
    s_data += "<td>"+total+"</td>"
    s_data += "<td>"+avg+"</td>"
    s_data += "<td><button class='updateBtn'>수정</button>"
    s_data += "<button class='delBtn'>삭제</button></td>"
    
    $("#"+id_num).html(s_data);
    
    //데이터 지우기
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    $("#create, #update, #updateCancel").toggle();
    temp=0;
  }) //update문

  $(document).on("click","#updateCancel",function(){
    $(this).css({"color":"blue","font-weight":"600"});

    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

    $("#create, #update, #updateCancel").toggle();
    temp=0;
  })//updateCancel문
  
});