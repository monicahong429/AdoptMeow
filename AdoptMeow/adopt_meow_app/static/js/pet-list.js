// static/js/pet-list.js

document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/pets/")
    .then((response) => response.json())
    .then((data) => {
      const petList = document.getElementById("pet-list");
      data.forEach((pet) => {
        const petItem = createPetItem(pet);
        petList.appendChild(petItem);
      });
    })
    .catch((error) => console.error("Error fetching pets:", error));
});

function createPetItem(pet) {
  const petItem = document.createElement("li");
  petItem.className = "pet-item";

  const petDetails = document.createElement("div");
  petDetails.className = "pet-details";

  if (pet.image) {
    const petImage = createPetImage(pet.image);
    petDetails.appendChild(petImage);
  }

  const petInfo = createPetInfo(pet);
  petDetails.appendChild(petInfo);

  petItem.appendChild(petDetails);
  return petItem;
}

function createPetImage(imageUrl) {
  const petImageContainer = document.createElement("div");
  petImageContainer.className = "pet-image-container";
  const petImage = document.createElement("img");
  petImage.className = "pet-image";
  petImage.src = imageUrl;
  petImageContainer.appendChild(petImage);
  return petImageContainer;
}

function createPetInfo(pet) {
  const petInfo = document.createElement("p");
  petInfo.innerHTML = `
    <strong>${pet.name}</strong><br>
    ${pet.breed}<br>
    ${pet.age} years old<br>
    ${pet.adoption_status ? "Not Available to adopt" : "Available to adopt!"}
  `;
  return petInfo;
}
