$(()=>{
    var move=0;
    var $point=$(".point");
    //var $pro=$(".pre");
    var $form=$(".contain>form");
    $(".next").click((e)=>{
        $tar=$(e.target);
        move++;
        $(".prev").removeAttr("disabled");
        $point.children(`:lt(${move})`).find("b").css("background-color","#10C642")
        $point.children(`:eq(${move})`).find("b").css("background-color","#FF8F03")
        console.log(move);
        if(move==4){
            $tar.html("提交");
        }
        if(move==5){
            $(location).attr("href","index.html");
        }
        $form.children(`:eq(${move})`).css("display","block").siblings().css("display","none");
    });
    $(".prev").click((e)=>{
        $tar=$(e.target);
        move--;
        if(move<=0){
            $tar.attr("disabled",true);
        }
        $(".next").html("下一步");
        $point.children(`:gt(${move})`).find("b").css("background-color","#DEDCD8")
        $point.children(`:eq(${move})`).find("b").css("background-color","#FF8F03")
        $form.children(`:eq(${move})`).css("display","block").siblings().css("display","none");
        console.log(move);
    })
})