// static/js/favorites-list.js

document.addEventListener("DOMContentLoaded", function () {
  const favoritesList = document.getElementById("favorites-list");
  const userId = favoritesList.getAttribute("data-user-id");

  fetch(`/api/user/${userId}/favorites/`)
    .then((response) => response.json())
    .then((data) => {
      data.forEach((favorite) => {
        fetch(`/api/pets/${favorite.pet}`)
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
          })
          .then((pet) => {
            const petItem = createPetItem(pet);
            favoritesList.appendChild(petItem);
          })
          .catch((error) => {
            console.error("Error fetching pet details:", error);
          });
      });
    })
    .catch((error) => {
      console.error("Error fetching favorites:", error);
    });
});
