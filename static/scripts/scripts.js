$('#idOfInput').key(
  function(){
      var inputString = $('#idOfInput').val();
      var shortenedString = inputString.substr(21,(inputString.length -1));
      $('#idOfInput').val(shortenedString);
  });