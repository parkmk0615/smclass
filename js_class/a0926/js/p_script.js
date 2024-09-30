$(function(){
 
  $("#searchBtn").click(function(){
    alert("검색버튼 클릭");
  
    let surl="https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=o4zrb2RU91sBRYTpUt81H9tPSRi65mIf8x3jaatN6Io5%2FluP6u22rytp5R8vcNUkr1uneEJh7TADsIpFNBs77w%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl+= searchWord;
    $.ajax({
      url: surl,
      type:"get",
      data:"",
      datatype:"json",
      success:function(data){
        alert("성공");
        console.log(data);

        var g_item = data.response.body.items.item;
        var h_data="";
        for(var i = 0; i<g_item.length; i++ ){
          h_data+="<tr>"
          h_data+="<td>"+g_item[i].galContentId+"</td>"
          h_data+="<td>"+g_item[i].galTitle+"</td>"
          h_data+="<td>"+g_item[i].galPhotographer+"</td>"
          h_data+="<td>"+g_item[i].galModifiedtime+"</td>"
          h_data+="<td><img src="+g_item[i].galWebImageUrl+">"+"</td>"
          h_data+="</tr>"
        }
        $("#tbody").html(h_data);
        
      },
      error:function(){
        alert("실패");

      }
      
      
    }) //ajax
}); //searchBtn

});//제이쿼리