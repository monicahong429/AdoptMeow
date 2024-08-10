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
  const petImage = document.createElement("img");
  petImage.className = "pet-image";
  petImage.src = imageUrl;
  return petImage;
}

function createPetInfo(pet) {
  const petInfo = document.createElement("div");
  petInfo.innerHTML = `
    <strong>${pet.name}</strong> - ${pet.breed} - ${pet.age} years old<br>
    <em>Adoption Status:</em> ${
      pet.adoption_status ? "Not Available" : "Available"
    }<br>
    <em>Health Records:</em> ${pet.health_records}<br>
    <em>Additional Info:</em> ${pet.additional_info || "N/A"}
  `;
  return petInfo;
}
