document.getElementById('imageInput').addEventListener('change', function(event) {
    const imageContainer = document.getElementById('uploadedImage');
    const file = event.target.files[0];

    if (file) {
        console.log("File");
        const reader = new FileReader();

        reader.onload = function(e) {
            // Set the src attribute of the img tag to the uploaded file data
            imageContainer.src = e.target.result;
            imageContainer.style.display = 'block';  // Make the image visible
        }

        // Read the image file as a data URL
        reader.readAsDataURL(file);
    }
});