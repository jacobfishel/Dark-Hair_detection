document.getElementById('file-input').addEventListener('change', replaceImage);

function replaceImage() {
    const fileInput = document.getElementById('file-input');
    const displayedImage = document.getElementById('displayed-image');

    // Check if a file was selected
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            // Set the new image source
            displayedImage.src = e.target.result;
        };

        // Read the file as a data URL (base64 encoded string)
        reader.readAsDataURL(fileInput.files[0]);
    }
}
