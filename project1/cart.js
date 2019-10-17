$(function (){
    countItem();
    //1.全选和取消全选
    var isChecked = false; //标识选中状态
    $("#checkAll").click(function (){
        //点击事件修改按钮的选中状态
        isChecked = !isChecked;
        if(isChecked){
            $("[name=check]").prop("checked","true");
        }else{
            $("[name=check]").removeAttr("checked");
        }
        countItem();
    })

    //2.反选
    $("[name=check]").change(function(){
        //未被选中的商品数量 == 0 对应全选
        //not()标识否定筛选
        //input:checked用于匹配被选中的元素
        //size()用于获取元素数量 (length)
        if($("[name=check]").not("input:checked").size()==0){
            $("#checkAll").prop("checked","true");
            //修改全选的标记
            isChecked = true;
        }else{
            $("#checkAll").removeAttr("checked");
            isChecked = false;
        }
        countItem();
    })

    //3.数量加减
    $(".add").click(function(){
        //获取前一个兄弟元素的文本内容
        var value = $(this).prev().val();
        //修改文本框的值
        $(this).prev().val(++value);
        //价格联动
        var priceStr = $(this).parent().prev().html(); //$188
        var price = priceStr.substring(1); //截取---> 188
        var sum = price * value;
        //修改小计
        $(this).parent().next().html("<b>&yen;"+sum+"</b>");
        countItem();
    })
    $(".minus").click(function(){
        //获取后一个兄弟元素的文本内容
        var value = $(this).next().val();
        //修改文本框的值
        if(value>1){
            $(this).next().val(--value);
            var priceStr = $(this).parent().prev().html(); //$188
            var price = priceStr.substring(1); //截取---> 188
            var sum = price * value;
            //修改小计
            $(this).parent().next().html("<b>&yen;"+sum+"</b>");
        }
        countItem();
    })

    //4.价格联动(输入框失去焦点)
    $(".count input").blur(function(){
        //数量
        var value = $(this).val();
        var priceStr = $(this).parent().prev().html(); //$188
        var price = priceStr.substring(1); //截取---> 188
        var sum = price * value;
        //修改小计
        $(this).parent().next().html("<b>&yen;"+sum+"</b>");
        countItem();
    })

    //5.移除
    $(".g-item .action").click(function(){
        $(this).parent().remove();
        countItem();
    })

    //6.工具栏价格和数量统计
    function countItem(){
        var count = 0;//保存总数量
        var price = 0;//保存总价格
        //获取被选中的商品数量/价格做累加
        $("[name=check]:checked").each(function(){
            //each()用于遍历数组或集合，每取到一个元素，自动调用相关函数
            count += Number($(this).parents(".g-item").find(".count input").val());
            //获取价格
            var priceStr = $(this).parents(".g-item").find(".sum b").html();
            //截取和转换
            var priceNum = Number(priceStr.substring(1));
            price += priceNum
        })
        //显示在工具栏
        $(".submit-count span").html(count);
        $(".submit-price span").html("&yen;"+price);
    }



})

























