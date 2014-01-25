define(function(require) {
    var $ = require("jquery");

    $(".top_mid span").each(function(index) {
        alert(index + ': ' + $(this).text());
    });
});