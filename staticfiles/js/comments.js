document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("commentForm").addEventListener("submit", function(event) {
        event.preventDefault();  // منع التحديث الافتراضي للصفحة

        let formData = new FormData(this);

        fetch(this.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"  // التأكد من أن الطلب هو AJAX
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
                document.getElementById("commentForm").reset();  // مسح حقل الإدخال بعد الإرسال
            }
        })
        .catch(error => console.error("Error:", error));
    });
});
function quoteComment(commentId) {
    // تحديد parent_id في النموذج لتحديد التعليق المقتبس
    document.getElementById("parent_id").value = commentId;

    // إضافة نص الاقتباس في حقل التعليق
    var commentText = document.querySelector(`#comment-${commentId} .card-body p`).innerText;
    var commentForm = document.querySelector('#commentForm textarea');
    commentForm.value = `اقتباس: ${commentText}\n\n` + commentForm.value;
}

// JavaScript لإضافة التعليق باستخدام AJAX
document.getElementById("commentForm").onsubmit = function(event) {
    event.preventDefault();  // منع إعادة تحميل الصفحة

    var formData = new FormData(this);
    fetch("{% url 'content' course.id %}", {
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

            // إذا كان هناك اقتباس، إظهار التعليق المقتبس
            if (data.parent_id) {
                newComment.querySelector(".card-body").innerHTML += `
                    <blockquote class="blockquote mt-2">
                        <footer class="blockquote-footer">اقتباس من <strong>${data.parent_user}</strong></footer>
                        <p>${data.parent_content}</p>
                    </blockquote>
                `;
            }

            // إضافة التعليق إلى أعلى القائمة
            commentSection.prepend(newComment);
            document.getElementById("commentForm").reset();  // مسح الحقول بعد الإرسال
        }
    });
};