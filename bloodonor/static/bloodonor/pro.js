$(function(){


 $('#request').on('click',function(e) {
    e.preventDefault();
    var csrf_token = $('[name=csrfmiddlewaretoken]').val();
    var user = $('#user').val();
    alert( $('#user').val());
    var bloodGroup = $('#blood').val();
    var bag = $('#bagNumber').val();
    var day = $('#datefield').val();
    var location = $('#location').val();
    alert(location+bloodGroup);
    var Request = {
      user: id,
      bloodGroup: bloodGroup,
      location:location,
      time: day,
      bags: bag,
      csrfmiddlewaretoken:csrf_token,
      };
alert(user.text() + " " + location.text()+" "+bloodGroup.text());
    $.ajax({
      type: 'POST',
      url:  'http://localhost:8000/api/request/',
      dataType: 'json',
      contentType:"application/json",
      data: Request,
      success: function(newUser){
        alert('yes');
      },

      beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken",  csrf_token );
                               },

      error: function (err) {
          alert(user.text() + " " + location.text()+" "+bloodGroup.text());
          alert(err.text());
        }
    });

  });


});
