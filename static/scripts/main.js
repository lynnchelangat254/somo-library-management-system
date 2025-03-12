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
  let deleteModal = document.getElementById("deleteMemberBtn");

  // Add an event listener to the modal's 'show.bs.modal' event
  deleteModal?.addEventListener("click", function (event) {
    console.log("test");
    let button = event.delegateTarget; // Button that triggered the modal
    let memberId = button.getAttribute("data-id"); // Get the member ID passed in data-id

    // Replace the placeholder '0' in the URL with the actual member ID
    let deleteUrl = `/librarian/members/${memberId}/delete/`;
    console.log(deleteUrl);

    // Set the href attribute of the confirmDelete button
    document.getElementById("confirmDelete").setAttribute("href", deleteUrl);
  });

  let deleteBookModal = document.getElementById("deleteBookBtn");

  // Add an event listener to the modal's 'show.bs.modal' event
  deleteBookModal?.addEventListener("click", function (event) {
    console.log("test");
    let button = event.delegateTarget; // Button that triggered the modal
    let bookId = button.getAttribute("data-id"); // Get the book ID passed in data-id
    let deleteUrl = `/librarian/books/${bookId}/delete/`;

    // add new a tag to the modal
    let newATag = document.createElement("a");
    newATag.textContent = "Confirm Delete";
    newATag.id = "confirmDeleteBook";
    newATag.href = deleteUrl;
    document.getElementById("deleteBookModalBody").appendChild(newATag);

    document
      .getElementById("confirmDeleteBook")
      .setAttribute("href", deleteUrl);
  });
};
