$(document).ready(function(){$(".preloader").hide();$("#Form").on("submit",function(){$(".preloader").fadeIn();});});function logoutFunction(){swal.fire({title:"Sure Want to Logout ?",type:"warning",showCancelButton:true,confirmButtonColor:"#3085d6",cancelButtonColor:"#d33",confirmButtonText:"OK",closeOnConfirm:true,closeOnCancel:false,}).then((result)=>{if(result.value===true){$("#logoutform").submit();}});}
function confirmFunction(){event.preventDefault();var form=event.target.form;Swal.fire({title:"Are you sure?",text:"You won't be able to revert this!",type:"warning",showCancelButton:true,confirmButtonColor:"#3085d6",cancelButtonColor:"#d33",confirmButtonText:"Yes, delete it!",}).then((result)=>{if(result.value){form.submit();}});}
function confirmLogoutFunction(){event.preventDefault();var form=event.target.form;Swal.fire({title:"Are you sure?",text:"Want to Logout !",type:"warning",showCancelButton:true,confirmButtonColor:"#3085d6",cancelButtonColor:"#d33",confirmButtonText:"Yes,Logout!",}).then((result)=>{if(result.value){form.submit();}});}
(function(){"use strict";var tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));tooltipTriggerList.forEach(function(tooltipTriggerEl){new bootstrap.Tooltip(tooltipTriggerEl);});})();$(document).ready(function(){$("#table").DataTable();});;$(document).ready(function(){$("ul.navbar-nav > li").click(function(e){$("ul.navbar-nav > li").removeClass("active1");$(this).addClass("active1");});});$(document).ready(function(){$("#sidebarsrink").click(function(){$(".wrapper").toggleClass("toggled");});$("#srink").click(function(){$(".wrapper.").toggleClass("toggled1");});});;