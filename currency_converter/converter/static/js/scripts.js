$(document).ready(function() {
    $('.currency-select').select2({
        width: '100%',
        theme: 'default'
    });

    $('#converter-form').on('submit', function(event) {
        event.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#result').text('Результат: ' + response.result).fadeIn();
            },
            error: function(xhr, status, error) {
                alert('Произошла ошибка: ' + error);
            }
        });
    });
});
