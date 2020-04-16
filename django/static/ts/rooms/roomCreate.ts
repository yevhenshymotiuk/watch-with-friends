import showVideoField from "./showVideoField";

let nameInput = document.getElementById("id_name");
let videoTypeSelectElement = document.getElementById("id_video_type");

nameInput && nameInput.focus();

showVideoField();
if (videoTypeSelectElement) {
    videoTypeSelectElement.onchange = showVideoField;
}
