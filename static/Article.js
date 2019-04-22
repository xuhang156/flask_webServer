loadConfiguration('container');
function loadConfiguration(argument) {
    console.log('进入函数内部');
    //加载配置文件1
    // var new_element=document.createElement("script");
    // new_element.setAttribute("type","text/javascript");
    // new_element.setAttribute("src","./ueditor/utf8-jsp/ueditor.config.js");
    // document.head.appendChild(new_element);
    // //加载配置文件2
    // var new_element1=document.createElement("script");
    // new_element1.setAttribute("type","text/javascript");
    // new_element1.setAttribute("src","./ueditor/utf8-jsp/ueditor.all.js");
    // document.head.appendChild(new_element1);
    UE.getEditor('container');
    //window.UE.getEditor('container');
}