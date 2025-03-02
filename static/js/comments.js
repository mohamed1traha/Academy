document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("commentForm").addEventListener("submit", function(event) {
        event.preventDefault();  
        let formData = new FormData(this);

        fetch(this.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"  
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                let commentHTML = `
                    <div class="card my-3">
                        <div class="card-body">
                            <strong>${data.user}</strong>
                            <p>${data.text}</p>
                            <small class="text-muted">${data.created_at}</small>
                        </div>
                    </div>
                `;
                document.getElementById("commentsSection").insertAdjacentHTML("afterbegin", commentHTML);
                document.getElementById("commentForm").reset();  
            }
        })
        .catch(error => console.error("Error:", error));
    });
});
document.getElementById("commentForm").onsubmit = function(event) {
    event.preventDefault();  // منع إعادة تحميل الصفحة

    var formData = new FormData(this);
    fetch("{% url 'content' course.id vido.id %}", {
        method: "POST",
        body: formData,
    }).then(response => response.json())
      .then(data => {
        if (data.success) {
            // إضافة التعليق الجديد مباشرةً في القسم
            let commentSection = document.getElementById("commentsSection");

            let newComment = document.createElement("div");
            newComment.classList.add("card", "my-3");
            newComment.id = "comment-" + data.comment_id;

            newComment.innerHTML = `
                <div class="card-body">
                    <strong>${data.user}</strong>
                    <p>${data.text}</p>
                    <small class="text-muted">${data.created_at}</small>
                    <button onclick="quoteComment(${data.comment_id})" class="btn btn-link">اقتباس</button>
                </div>
            `;



            commentSection.prepend(newComment);
            document.getElementById("commentForm").reset();  
        }
    });
};