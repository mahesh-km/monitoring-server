var ISPHONE=(window.outerWidth<768);var ISTABLET=(window.outerWidth<1025&&(window.orientation!==undefined));(function(a){a(document).on("vclick",'a[target="webapp"]',function(c){c.preventDefault();window.location=a(this).attr("href");return false});a(document).on("vclick",function(c){if(!a(c.target).is("input")){a("input:focus").blur()}});if(ISTABLET){var b=function(c){c.stopPropagation();c.preventDefault();return false};a('#menu li:has("ul")').find("a:first").each(function(c,d){a(d).unbind("vclick").on("vclick",b)})}if(ISPHONE){setTimeout(function(){window.scrollTo(0,0)},0);a("#logo").unbind("vclick").on("vclick",function(c){c.preventDefault();c.stopPropagation();window.scrollTo(0,0);a("#logo").toggleClass("active");a("#menu").toggle();return false})}})(jQuery);