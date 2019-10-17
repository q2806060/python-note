//轮播
$(()=>{
    $(()=>{
        var LIWIDTH=1300,timer=null,moved=0,duration=500,wait=3000;
        var $ul=$("ul.sub-img");
        $ul.css("width",LIWIDTH*5);
        var $ulInds=$("ul.sub-case");
        $ulInds.children().first().addClass("sub-active");
        function move(){
            $ul.animate({
                left:-LIWIDTH*moved
            },duration,function(){
                if(moved==4){
                    moved=0;
                    $ul.css("left",0);
                }
                $ulInds.children(`:eq(${moved})`).addClass("sub-active")
                    .siblings().removeClass("sub-active");
            })
        }
        timer=setInterval(()=>{
            moved++;
            move();
        },wait+duration);

        $ulInds.on("mouseenter","li",e=>{
            moved=$(e.target).index();
            //防止动画叠加
            clearInterval(timer);
            $ul.stop(true);
            move();
        });
        $(".sub-img").hover(
            ()=>{clearInterval(timer)},
            ()=>{
                timer=setInterval(()=>{
                    moved++;
                    move();
                },wait+duration)
            }
        );
    })
});

//登录跳转
$(()=>{
    $(".btn-login").click((e)=>{
        e.preventDefault();
        console.log("denglu ");
        $(location).attr("href","login.html");
    })
});