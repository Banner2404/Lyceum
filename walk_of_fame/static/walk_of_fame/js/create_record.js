window.onload = function() {
    var image = document.getElementById("profile-image");
    var imageInput = document.getElementById("id_image");
    image.onclick = imageClick;
    imageInput.onchange = function() { imageInputChanged(imageInput, image) };
}

function imageClick() {
    var imageInput = document.getElementById("id_image");
    imageInput.click();
}

function loadFile(file, image) {
    var reader = new FileReader();
    reader.onload = function(e) {
        image.src = e.target.result;
    }

    reader.readAsDataURL(file);
}

function imageInputChanged(input, image) {
    if (input.files && input.files[0]) {
        loadFile(input.files[0], image)
    }
}