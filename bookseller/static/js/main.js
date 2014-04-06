/**
 * Created by kokdemo on 14-4-6.
 */

//$(function(){
//    $("#id_username").blur(function(){//用户名文本框失去焦点触发验证事件
//        if(!$(this).val() || !$(this).val.match(/([w]){2,15}$/))//只处验证不能为空并且只能为英文或者数字或者下划线组成的２－１５个字符
//        {
//            $("#usernameHelp").html("用户名不能为空且只能为英文或者数字");
//        }
//        else
//        {
//            $("#usernameHelp").html("输入正确");
//        }
//    });
//    $("#id_password").blur(function(){//用户密码框失去焦点触发验证事件
//        if(!$(this).val() || !$(this).val.match(/([w]){2,15}$/))//只处验证和上面一样
//        {
//            $("#passwordHelp").html("密码不能为空且只能为英文或者数字");
//        }
//        else
//        {
//            $("#passwordHelp").html("输入正确");
//        }
//    });
//    $("#reInput").blur(function(){//用户密码确认框失去焦点触发验证事件
//        if(!$(this).val() || $(this).val() != $("#id_password").val() )//此处验证和上面一样
//        {
//            $("#repasswordHelp").html("密码为空或者和上面的密码不致");
//        }
//        else
//        {
//            $("#repasswordHelp").html("输入正确");
//        }
//    });
//})