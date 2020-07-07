/*!
 * jQuery.tipsy
 * Copyright (c) 2014 CreativeDream
 * Website: http://creativedream.net/plugins/
 * Version: 1.0 (18-11-2014)
 * Requires: jQuery v1.7.1 or later
 */
(function(e){e.fn.tipsy=function(t){if(typeof t=="string"&&["show","hide"].indexOf(t)>-1){switch(t){case"show":$(this).trigger("tipsy.show");break;case"hide":$(this).trigger("tipsy.hide");break}return this}var n=e.extend({arrowWidth:10,attr:"data-tipsy",cls:null,duration:150,offset:7,position:"top-center",trigger:"hover",onShow:null,onHide:null},t);return this.each(function(t,r){var i=e(r),s=".tipsy",o=e('<div class="tipsy"></div>'),u=["top-left","top-center","top-right","bottom-left","bottom-center","bottom-right","left","right"],a={init:function(){var e={};switch(n.trigger){case"hover":e={mouseenter:a._show,mouseleave:a._hide};break;case"focus":e={focus:a._show,blur:a._hide};break;case"click":e={click:function(e){if(!a._clSe){a._clSe=true;a._show(e)}else{a._clSe=false;a._hide(e)}}};break;case"manual":a._unbindOptions();e={"tipsy.show":function(e){a._clSe=true;a._show(e)},"tipsy.hide":function(e){a._clSe=false;a._hide(e)}};break}i.on(e);o.hide()},_show:function(e){$(s).remove();a._clear();if(a.hasAttr(n.attr+"-disabled")){return false}a._createBox();if(n.trigger!="manual"){a._bindOptions()}},_hide:function(e){a._fixTitle(true);o.stop(true,true).fadeOut(n.duration,function(){n.onHide!=null&&typeof n.onHide=="function"?n.onHide(o,i):null;a._clear();$(this).remove()})},_showIn:function(){o.stop(true,true).fadeIn(n.duration,function(){n.onShow!=null&&typeof n.onShow=="function"?n.onShow(o,i):null})},_bindOptions:function(){e(window).bind("contextmenu",function(){a._hide()}).bind("blur",function(){a._hide()}).bind("resize",function(){a._hide()}).bind("scroll",function(){a._hide()})},_unbindOptions:function(){e(window).unbind("contextmenu",function(){a._hide()}).unbind("blur",function(){a._hide()}).unbind("resize",function(){a._hide()}).unbind("scroll",function(){a._hide()})},_clear:function(){o.attr("class","tipsy").empty();a._lsWpI=[];a._lsWtI=[]},hasAttr:function(e){e=i.attr(e);return typeof e!==typeof undefined&&e!==false},_fixTitle:function(e){if(e){if(a.hasAttr("data-title")&&!a.hasAttr("title")&&a._lsWtI[0]==true){i.attr("title",a._lsWtI[1]||"").removeAttr("data-title")}}else{if(a.hasAttr("title")||!a.hasAttr("data-title")){a._lsWtI=[true,i.attr("title")];i.attr("data-title",i.attr("title")||"").removeAttr("title")}}},_getTitle:function(){a._fixTitle();var e=i.attr("data-title");e=""+e;return e},_position:function(e){var t={top:0,left:0},r=e?e:a.hasAttr(n.attr+"-position")?i.attr(n.attr+"-position"):n.position,s=r.split("-"),l=a.hasAttr(n.attr+"-offset")?i.attr(n.attr+"-offset"):n.offset,c={offsetTop:i.offset().top,offsetLeft:i.offset().left,width:i.outerWidth(),height:i.outerHeight()},h={width:o.outerWidth(),height:o.outerHeight()},d={width:$(window).outerWidth(),height:$(window).outerHeight(),scrollTop:$(window).scrollTop(),scrollLeft:$(window).scrollLeft()};if($.inArray(r,u)==-1||$.inArray(r,a._lsWpI)!==-1){a._hide();return t}else{a._lsWpI.push(r)}switch(s[0]){case"bottom":t.top=c.offsetTop+c.height+l;if(t.top>=d.height+d.scrollTop){return a._position("top"+"-"+s[1])}o.addClass("arrow-top");break;case"top":t.top=c.offsetTop-h.height-l;if(t.top-d.scrollTop<=0){return a._position("bottom"+"-"+s[1])}o.addClass("arrow-bottom");break;case"left":t.top=c.offsetTop+c.height/2-h.height/2;t.left=c.offsetLeft-h.width-l;if(t.left<=0){return a._position("right")}o.addClass("arrow-side-right");return t;break;case"right":t.top=c.offsetTop+c.height/2-h.height/2;t.left=c.offsetLeft+c.width+l;if(t.left+h.width>d.width){return a._position("left")}o.addClass("arrow-side-left");return t;break}switch(s[1]){case"left":t.left=c.offsetLeft+c.width/2-h.width+n.arrowWidth;if(t.left<=0){return a._position(s[0]+"-"+"right")}o.addClass("arrow-right");break;case"center":t.left=c.offsetLeft+c.width/2-h.width/2;if(t.left+h.width>d.width){return a._position(s[0]+"-"+"left")}if(t.left<=0){return a._position(s[0]+"-"+"right")}o.addClass("arrow-center");break;case"right":t.left=c.offsetLeft+c.width/2-n.arrowWidth;if(t.left+h.width>d.width){return a._position(s[0]+"-"+"left")}o.addClass("arrow-left");break}return t},_createBox:function(){o.html(a._getTitle()).appendTo("body");if(n.cls!=null&&typeof n.cls=="string"||a.hasAttr(n.attr+"-cls")){o.addClass(a.hasAttr(n.attr+"-cls")?i.attr(n.attr+"-cls"):n.cls)}o.css(a._position());a._showIn()},_lsWtI:[],_lsWpI:[]};a.init();return this})}})(jQuery);
