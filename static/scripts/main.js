window.onload = function () {
  let year = document.getElementById("year");
  if (year) {
    year.textContent = new Date().getFullYear();
  }

  setTimeout(function () {
    let alert = document.querySelector(".alert"); // Select the alert element
    if (alert) {
      alert.classList.remove("show"); // Remove the 'show' class to hide the alert
      alert.classList.add("fade"); // Add the 'fade' class to apply fading effect
    }
  }, 5000); // 5 seconds delay

  // Get the delete modal
  var deleteModal = document.getElementById("deleteMemberBtn");
  console.log(deleteModal)

  // Add an event listener to the modal's 'show.bs.modal' event
  console.log(deleteModal);
  deleteModal.addEventListener("click", function (event) {
    console.log("test");
    var button = event.delegateTarget; // Button that triggered the modal
    var memberId = button.getAttribute("data-id"); // Get the member ID passed in data-id

    // Replace the placeholder '0' in the URL with the actual member ID
    var deleteUrl = `/librarian/members/${memberId}/delete/`;
    console.log(deleteUrl);

    // Set the href attribute of the confirmDelete button
    document.getElementById("confirmDelete").setAttribute("href", deleteUrl);
  });
};
