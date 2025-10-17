// ===============================
// SweetAlert2 Toast Notifications
// Global message handler for Django messages
// ===============================

document.addEventListener("DOMContentLoaded", function() {
  // Django'dan gelen mesajlar varsa global değişkenle alınır
  if (typeof django_messages !== "undefined" && django_messages.length > 0) {
    django_messages.forEach(msg => {
      Swal.fire({
        toast: true,
        position: 'top-end',
        icon: msg.tags.includes("success") ? "success"
             : msg.tags.includes("error") ? "error"
             : "info",
        title: msg.text,
        showConfirmButton: false,
        timer: 2500,
        timerProgressBar: true,
        background: "#fff",
        color: "#333",
        iconColor: msg.tags.includes("success") ? "#0d6efd"
                   : msg.tags.includes("error") ? "#dc3545"
                   : "#6c757d",
        didOpen: (toast) => {
          toast.addEventListener("mouseenter", Swal.stopTimer);
          toast.addEventListener("mouseleave", Swal.resumeTimer);
        }
      });
    });
  }
});
