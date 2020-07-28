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

 
