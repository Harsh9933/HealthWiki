document.addEventListener("DOMContentLoaded", function () {
    const mapAreas = document.getElementsByTagName("area");
    const areaInfo = document.getElementById("area-info");

    areaInfo.innerHTML = "No Part Selected"; // Initialize with default message

    for (let i = 0; i < mapAreas.length; i++) {
        mapAreas[i].addEventListener("mouseover", function (e) {
            const areaName = e.target.getAttribute("data-name");
            areaInfo.innerHTML = areaName;
        });

        mapAreas[i].addEventListener("mouseout", function () {
            areaInfo.innerHTML = "No Part Selected";
        });
    }
});