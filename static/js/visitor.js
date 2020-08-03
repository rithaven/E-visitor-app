$(document).ready(function(){
    var $myForm=$(".my-ajax-form");
    $myForm.submit(function(event){
        event.preventDefault();
        var $formData=$myForm.serialize();
        $.ajax({
            method:'POST',
            data: $formData,
            success:handleSuccess,
            error: handleError,
        });
        function handleSuccess(data){
            console.log(data.message);
            $myForm[0].reset()
        }
        function handleError(throwError){
            console.log(throwError);
        }
    });
});
$(document).ready(function(){
    $(".my-ajax-form").keydown(function(e){
        if(e.which==17 || e.which==74){
            e.preventDefault();
        }else{
            console.log(e.which);
        }
    })
});


// $(".my-ajax-form").on("keypress paste", function(e){
//     var c = this.selectionStart, v = $(this).val();
//     if (e.type == "keypress")
//         var key = String.fromCharCode(!e.charCode ? e.which : e.charCode)
//     else
//         var key = e.originalEvent.clipboardData.getData('Text')
//     var val = v.substr(0, c) + key + v.substr(c, v.length)
//     if (!val.match(/\d{0,21}/) || val.match(/\d{0,21}/).toString()!= val) {
//         e.preventDefault()
//         return false
//     }
// })
// function isNumber (text) {
//     if(text) {
//       var reg = new RegExp('[0-9]+$');
//       return reg.test(text);
//     }
//     return false;
//   }
  
//   function removeSpecial (text) {
//     if(text) {
//       var lower = text.toLowerCase();
//       var upper = text.toUpperCase();
//       var result = "";
//       for(var i=0; i<lower.length; ++i) {
//         if(isNumber(text[i]) || (lower[i] != upper[i]) || (lower[i].trim() === '')) {
//           result += text[i];
//         }
//       }
//       return result;
//     }
//     return '';
//   }