/**
 * @file jquery.add-input-area
 * @version 4.9.2
 * @author Yuusaku Miyazaki <toumin.m7@gmail.com>
 * @license MIT
 */
!function(a){"object"==typeof module&&"object"==typeof module.exports?a(require("jquery"),window,document):a(jQuery,window,document)}(function(a,b,c,d){a.fn.addInputArea=function(b){return this.each(function(){new a.addInputArea(this,b)})},a.addInputArea=function(b,d){this.elem=b,this.option=this._setOption(d,a(this.elem).attr("id")),this._setDelBtnVisibility();var e=this;a(c).on("click",this.option.btn_add,function(){e._ehAddBtn.call(e)}),a(e.elem).on("click",e.option.btn_del,function(a){e._ehDelBtn.call(e,a)}),this._renumberFieldAll(),this.option.original=a(this.elem).find(this.option.area_var).eq(0).clone(this.option.clone_event)},a.extend(a.addInputArea.prototype,{_setOption:function(b,c){return b=a.extend({btn_del:c?"."+c+"_del":".aia_del",btn_add:c?"."+c+"_add":".aia_add",area_var:c?"."+c+"_var":".aia_var",area_del:null,after_add:null,clone_event:!0,maximum:0},b),b.area_del||(b.area_del=b.btn_del),b},_setDelBtnVisibility:function(){1==a(this.elem).find(this.option.area_var).length&&a(this.elem).find(this.option.area_del).hide()},_ehAddBtn:function(){this._addNewArea(),a(this.elem).find(this.option.area_del).show(),this.option.maximum>0&&a(this.elem).find(this.option.area_var).length>=this.option.maximum&&a(this.option.btn_add).hide(),"function"==typeof this.option.after_add&&this.option.after_add()},_addNewArea:function(){var b=a(this.elem).find(this.option.area_var).length,c=a(this.option.original).clone(!0);this._renumberFieldEach(b,c);var d=this;a(c).find("[name]").each(function(){d._initFieldVal.call(d,this)}).end().appendTo(this.elem)},_initFieldVal:function(b){return"false"!=a(b).attr("empty_val")&&"false"!=a(b).attr("data-empty-val")&&("checkbox"==a(b).attr("type")||"radio"==a(b).attr("type")?b.checked=!1:"SELECT"!=a(b).prop("tagName")&&"submit"!=a(b).attr("type")&&"reset"!=a(b).attr("type")&&"image"!=a(b).attr("type")&&"button"!=a(b).attr("type")&&a(b).val(""),!0)},_ehDelBtn:function(b){b.preventDefault();var c=a(this.elem).find(this.option.btn_del).index(b.target);a(this.elem).find(this.option.area_var).eq(c).remove(),this._setDelBtnVisibility(),this._renumberFieldAll(),this.option.maximum>0&&a(this.elem).find(this.option.area_var).length<this.option.maximum&&a(this.option.btn_add).show()},_renumberFieldAll:function(){var b=this;a(this.elem).find(this.option.area_var).each(function(a,c){b._renumberFieldEach.call(b,a,c)})},_renumberFieldEach:function(b,c){var d=this;a(c).find("[name]").each(function(){a(this).attr("name",d._getValOfAttr(this,b,"name")),a(this).attr("id",d._getValOfAttr(this,b,"id"))}).end().find("[for]").each(function(){a(this).attr("id",d._getValOfAttr(this,b,"for"))})},_getValOfAttr:function(b,c,d){var e=!1;if(/^.+_\d+$/.test(a(b).attr(d)))e=a(b).attr(d).replace(/^(.+_)\d+$/,"$1"+c);else{var f;f="name"==d?a(b).attr("name_format")||a(b).attr("data-name-format"):a(b).attr("id_format")||a(b).attr("data-id-format"),f&&(e=f.replace("%d",c))}return e}})});