// فتح الصورة في نافذة منبثقة عند الضغط عليها
document.querySelectorAll('.post-image').forEach(image => {
    image.addEventListener('click', function () {
        const modal = document.getElementById('imageModal');
        const modalImg = document.getElementById('modalImg');
        modal.style.display = 'block';
        modalImg.src = this.src;
    });
});

// إغلاق النافذة المنبثقة عند الضغط على الزر
document.getElementById('closeModal').addEventListener('click', function () {
    const modal = document.getElementById('imageModal');
    modal.style.display = 'none';
});
