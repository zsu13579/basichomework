$(function(){
	
    //Edit 
    $(".editbtn").click(function(){
    	
		var th=$(".text_holder");
		var bx=$(".edit_input_box");
		var num=$(this).parents('li').index();
		var orgval=$(this).parents('li').children('div').children('p').text();
		th.eq(num).hide();
		bx.eq(num).children('.itembox').val(orgval);
		bx.eq(num).show();
    	
    });
    
    //Submit 
    $(".submitbtn").click(function(){

    	$(".edit_input_box").hide();
    	$(".text_holder").show();

    });
    
    //Delete 
    $(".deletebtn").click(function(){
    	
    	var item=$(this).parents('li').children('div').children('p').text();
		$.get("/delete_ajax/",{"item": item},function(result){
//			alert(result.result);		
		});
		$(this).parents('li').children('div').children('p').addClass("completed_item");
    	
    });
	    	
});
