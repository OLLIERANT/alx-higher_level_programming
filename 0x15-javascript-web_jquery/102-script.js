$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const len = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/hello/?lang=' + len,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
