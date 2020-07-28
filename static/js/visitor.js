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

$(".my-ajax-form").on("keypress paste", function(e){
    var c = this.selectionStart, v = $(this).val();
    if (e.type == "keypress")
        var key = String.fromCharCode(!e.charCode ? e.which : e.charCode)
    else
        var key = e.originalEvent.clipboardData.getData('Text')
    var val = v.substr(0, c) + key + v.substr(c, v.length)
    if (!val.match(/\d{0,500}/) || val.match(/\d{0,500}/).toString() != val) {
        e.preventDefault()
        return false
    }
})
