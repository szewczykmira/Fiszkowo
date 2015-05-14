$(document).ready(function(){
  $('#formSubmit').on('click', function(){
    var frm = $('#addCat');
    $.ajax({
      type: frm.attr('method'),
      url: frm.attr('action'),
      data: frm.serialize(),
      success: function(data.n_url){
        html_i = '<li><div class="timeline-image"><img class="img-circle img-responsive" alt=""></div><div class="timeline-panel"><div class="timeline-body"><a href="' + data.n_url +'"><h4 class="subheading">' + data.name +'</h4></a></div></div></li>'; 
        $('#time').prepend(html_i);
        $('#addCat').restet();
      } else {
        
      },
    });
  });
});
