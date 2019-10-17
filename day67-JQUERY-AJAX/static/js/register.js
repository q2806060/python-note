$(function(){
    $("#register").click(function(){
        var data = {
            "uname":$("#uname").val(),
            "upwd":$("#upwd").val(),
            "uemail":$("#uemail").val()
        };
        $.post("/register",data,function(resText){
            alert(resText);
        });
    });
});