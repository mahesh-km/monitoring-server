if((typeof MMONIT==="undefined")||(!MMONIT)){var MMONIT={}}MMONIT.error=function(){return{show:function(a){$("#MMonitError").modal("hide").remove();$('<div id="MMonitError" class="modal hide fade" tabindex="-1" role="dialog"><div class="modal-body"><h2 class="text-error" id="myModalLabel">Error</h2><p>'+$("<div/>").text(a).html()+'</p></div><div class="modal-footer"><button class="btn" data-dismiss="modal" aria-hidden="true">Close</button></div></div>').appendTo("body").modal("show")},abort:function(a){MMONIT.error.show(a);throw (a)},json:function(f,i,h,d){if(i=="abort"){console.log("AJAX request aborted")}else{var c=f.statusText;var b=f.responseText?f.responseText:((h&&h!=f.statusText)?h:"");try{var a=$.parseJSON(b);if(a){c+=": "+a.error}}catch(g){c+=": "+b}finally{if(d){d.showTableMessage($("<div/>").text(c).html())}else{MMONIT.error.show(c)}}}}}}();MMONIT.assert=function(a){if((typeof a==="undefined")||(!a)){MMONIT.error.show("Assert failed: "+a.toString());throw"Assert failed:"+a.toString()}};