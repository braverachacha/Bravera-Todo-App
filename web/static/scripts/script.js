// flashed message dismiss
document.addEventListener("DOMContentLoaded", function () {
  const closeButtons = document.querySelectorAll(".close-button");
  closeButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      this.parentElement.style.display = "none";
    });
  });
});

// delete endpoint/function

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/journal";
  });
}

// note update 

function updateNote(noteId){
  window.location.href=`/update/${noteId}`;
}

// nav bar toggle

const menuToggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.navigation ul');
  menuToggle.addEventListener('click', () => {
    navList.classList.toggle('active');
});