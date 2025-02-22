$(document).ready(function() {
    // When like button is clicked
    $('.like-btn').click(function() {
        var form = $(this).closest('form');
        var postId = form.data('post-id');

        // Send AJAX request to like or remove like
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: form.serialize(),  // Send data including CSRF token
            success: function(response) {
                // Update the button text to reflect the change in like status
                var likeCount = response.like_count;
                var buttonText = response.button_text;

                form.find('.like-btn').text(buttonText);
                form.siblings('.like-count').text("Like Count: " + likeCount);
            },
            error: function() {
                alert("An error occurred while processing the request.");
            }
        });
    });
});
