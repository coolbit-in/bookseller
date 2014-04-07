/*
 说明：初始化状态，要求输入焦点定位在用户名输入框，并产生验证码
 参数：无
 返回值：无
 */
function iniState(){
    //默认获得输入焦点
    document.frm_register.username.focus();
    //产生验证码
    getValidateCode();
}

/*
 说明：去除字符串两边空格函数
 参数str：要去除空格的字符串
 返回值：去除空格之后的字符串
 */
function trim(str){
    return String(str).replace(/(^\s*)|(\s*$)/g,"");
}
/*
 说明：判断目标字符串与源字符串是否匹配
 参数sV：目标字符串，即要判断的字符串
 参数sR：源字符串，即目标字符串要跟哪个字符串判断匹配
 返回值：若匹配：返回true，不匹配：返回false；
 */
function isMatch (sV,sR){
    var s_V = trim(sV);
    var s_R = trim(sR);
    var sTmp;
    if(s_V.length==0){
        return (false);
    }
    for (var i=0; i < s_V.length; i++){
        sTmp= s_V.substring(i, i+1);
        if (s_R.indexOf (sTmp, 0)==-1) {
            return (false);
        }
    }
    return (true);
}

///*/显示用户名输入错误提示信息
// function verifyUName(UName,eId){
// var msg = "";
// //用户名必须6-20位
// if (String(UName).length < 6 || String(UName).length > 20){
// msg = "用户名必须6-20位";
// showErrorMsg(eId,msg);
// return(false);
// }
// var firstBit = UName.substring(0,1);
// if( isMatch(firstBit,"0123456789")){
// msg = "用户名不能以数字开头";
// showErrorMsg(eId,msg);
// return(false);
// }
// if(isMatch(UName,"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")){
// clearMsg(eId);
// return(true);
// }else{
// msg = "用户名含有非法字符";
// showErrorMsg(eId,msg);
// return(false);
// }
// }
// */

/*
 说明：验证用户名是否符合要求
 规则：英文字母阿拉伯数字下划线组合，长度为6－20位，只能以字母开头
 参数UName：用户输入的用户名
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifyUName(UName,eId){
    var msg = "";
    var strUserName = trim(UName);
    //用户名必须6-20位
    if (String(strUserName).length < 6 || String(strUserName).length > 20){
        msg = "用户名必须6-20位";
        showErrorMsg(eId,msg);
        return(false);
    }
    //使用正则表达式验证
    var pattern = /^[a-zA-Z]{1}[a-zA-Z0-9_]{5,19}$/;
    if(pattern.test(strUserName)){
        clearMsg(eId);
        return(true);
    }else{
        msg = "用户名输入错误";
        showErrorMsg(eId,msg);
        return(false);
    }
}

/*
 说明：验证输入密码是否符合要求
 规则：英文字母或阿拉伯数字组合，英文区分大小写，长度为6－20位
 参数UName：用户输入的用户名
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifyPwd(Pwd,eId){
    var msg = "";
    var strPassWord = trim(Pwd);
    if (String(strPassWord).length < 6 || String(strPassWord).length > 20){
        msg = "密码必须6位以上";
        showErrorMsg(eId,msg);
        return(false);
    }

    if(isMatch(strPassWord,"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")){
        clearMsg(eId);
        return(true);
    }else{
        msg = "密码中含有非法字符";
        showErrorMsg(eId,msg);
        return(false);
    }
}
/*
 说明：验证密码输入是否符合要求
 规则：与输入密码一致
 参数pwd：用户输入的密码
 参数chkpwd：用户输入的验证密码
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifychkPwd(pwd,chkpwd,eId){
    var msg="";
    if(pwd !=chkpwd){
        msg="两次输入密码不一致";
        showErrorMsg(eId,msg);
    } else{
        clearMsg(eId);
        return(true);
    }
}

/*
 说明：验证验证密码提示答案是否符合要求
 规则：3-32位，不允许存在$<>%=字符
 参数pwdAnswer：用户输入的验证码答案
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifyPwdAnswer(pwdAnswer,eId){
    var msg = "";
    var strPwdAnswer = trim(pwdAnswer);
    if (String(strPwdAnswer).length < 3){
        msg = "密码提示答案必须3位以上";
        showErrorMsg(eId,msg);
        return(false);
    }

    if(isMatch(strPwdAnswer,"$<>%=")){
        msg = "$<>%=为非法字符，请修改";
        showErrorMsg(eId,msg);
        return(false);
    } else{
        clearMsg(eId);
        return(true);
    }
}

/*
 说明：验证手机号码是否符合要求
 规则：阿拉伯数字组合，长度为11位
 参数Tel：用户输入的手机号码
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifyTel(Tel,eId){
    var msg = "";
    var strPhoneNumber = trim(Tel);
    if (String(strPhoneNumber).length !=11){
        msg = "电话号码必须符合格式";
        showErrorMsg(eId,msg);
        return(false);
    }

    if(isMatch(strPhoneNumber,"0123456789")){
        clearMsg(eId);
        return(true);
    }else{
        msg = "电话中含有非法字符";
        showErrorMsg(eId,msg);
        return(false);
    }
}

/*
 说明：验证QQ号码是否符合要求
 规则：阿拉伯数字组合，长度为5～15位
 参数QQ：用户输入的QQ号
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifyQQ(QQ,eId){
    var msg = "";
    var strQQNumber = trim(QQ);
    if (String(strQQNumber).length <6 || String(strQQNumber).length >15){
        msg = "QQ号码必须符合格式";
        showErrorMsg(eId,msg);
        return(false);
    }

    if(isMatch(strQQNumber,"0123456789")){
        clearMsg(eId);
        return(true);
    }else{
        msg = "QQ号码中含有非法字符";
        showErrorMsg(eId,msg);
        return(false);
    }
}


/*
 说明：验证e_mail是否符合要求
 规则：
 e_mail位数必须大于6
 e_mail中必须包含@,且@不能在第二位之前，且@后最少四位
 e_mail中必须包含.，且最后一个.后最少二位
 例：最短e_mail:a@x.cn
 参数email：用户输入的email地址
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function verifyEmail(email,eId){
    var msg = "";
    var emailLength = 0;
    emailLength = String(email).length;
    //e_mail位数必须大于等于6
    if ( emailLength < 6){
        msg = "邮箱地址必须5位以上";
        showErrorMsg(eId,msg);
        return(false);
    }
    var atPos = -1;
    //@不能在第二位之前，即@位置>=1
    atPos = email.indexOf("@");
    var afterAtStr = "";
    var afterAtLength = -1;
    afterAtStr = email.substring(atPos+1 , emailLength);
    afterAtLength = afterAtStr.length;

    if(atPos == -1){
        msg = "邮箱地址中没有@";
        showErrorMsg(eId,msg);
        return(false);
    }else if((atPos < 1) || (afterAtLength < 4)){
        msg = "邮箱地址中@位置不对";
        showErrorMsg(eId,msg);
        return(false);
    }

    var lastDotPos = 0;
    lastDotPos = email.lastIndexOf(".");
    if(email.indexOf(".") == 0){
        msg = "邮箱地址不能以.开头";
        showErrorMsg(eId,msg);
        return(false);
    }   //e_mail中必须包含.，且.后最少二位
    if(lastDotPos == -1){
        msg = "邮箱地址中没有.";
        showErrorMsg(eId,msg);
        return(false);
    }else if((lastDotPos < 3 ) || (email.length - lastDotPos) <= 2){
        msg = "邮箱地址中.位置不对";
        showErrorMsg(eId,msg);
        return(false);
    }
    //@ 在最后一个.前面最少一位
    if((lastDotPos - atPos)< 2 ){
        msg = "邮箱地址中@位置要在最后一个.位置之前";
        showErrorMsg(eId,msg);
        return(false);
    }else{
        clearMsg(eId);
        return(true);
    }
}
/*
 说明：验证是否接受服务请求
 规则：用户必须接受服务请求
 参数form：输入请求复选框所在的form
 参数eId：错误提示div的id
 返回值：若符合要求：返回true，不符合：返回false；
 */
function checkAccept(form,eId){
    var msg = "";
    //用户是否选择
    if(form.chk_accept.checked){
        clearMsg(eId);
        return(true);
    }else{
        msg = "请阅读并接受服务条款";
        showErrorMsg(eId,msg);
        return(false);
    }
}
/*
 说明：显示错误信息函数
 参数 eId：要显示div的id
 参数 msg：要显示的信息内容
 */
function showErrorMsg(eId,msg){
    document.getElementById(eId).innerHTML = msg;
    document.getElementById(eId).style.display = "";
}
/*
 隐藏错误提示信息div
 参数eId：要隐藏的div的id
 */
function clearMsg(eId){
    document.getElementById(eId).style.display = "none";
}
/*
 说明：主验证函数，验证所有输入选择是否符合要求
 规则：依次验证，要求所有验证都符合要求
 返回值：若所有验证均通过：返回true，有一个不通过：返回false；
 */
function verifyInput(){
    //通过表单名称，得到输入表单
    var form = document.frm_register;
    //依次验证
    if (verifyUName(form.username.value,"div_uname_hint") && verifyPwd(form.txt_pwd.value,"div_pwd_hint") &&
        verifychkPwd(form.txt_pwd.value,form.txt_chkpwd.value,"div_chkpwd_hint")&&
        verifyvCode(form.txt_vcode.value,"div_vcode","div_vcode_hint") && checkAccept(form,"div_accept_hint"))
    {
        alert("^_^ 恭喜，注册成功！");
        form.submit;
        return(true);
    }else{
        alert("注册失败，请按红色提示信息修改！");
        return(false);
    }
}