function createXhr(){
    if(window.XMLHttpRequest){
        var xhr = new XMLHttpRequest();
    }else{
        var xhr = new ActiveXObject(Microsoft.XMLHTTP);
    }
    return xhr;
}