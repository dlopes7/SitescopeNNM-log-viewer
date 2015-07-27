    $(function() {
			$('#filter-bar').bootstrapTableFilter({
				connectTo: '#table',
				onAll: function(name, args) {
					var d = new Date();
					$('#log').prepend(d.toLocaleString() + ': ' + name + "\n");
				},
				onSubmit: function(data) {
					var data = $('#filter-bar').bootstrapTableFilter('getData');
					var d = new Date();
					$('#log').prepend(d.toLocaleString() + ': ' + JSON.stringify(data) + "\n");
				}
			});
		});

    $(function(){

    $('#refresh').on('click', function(e){
      e.preventDefault(); // preventing default click action
      $('#loading_gif').show();
      $.ajax({
        url: '/refresh',
        type: 'get',
        success: function (response) {
          //Feito!
          location.reload();
        }, error: function (response) {
          alert('ajax failed');
          // ajax error callback
        },
      });
    });
  });

    $(document).ajaxComplete(function() {
    $('td').filter(function() {

        return $(this).text().indexOf('Mailto') === 0;
    }).closest('tr').addClass('info');
    });

        $(document).ajaxComplete(function() {
    $('td').filter(function() {

        return $(this).text().indexOf('Run') === 0;
    }).closest('tr').addClass('success');
    });