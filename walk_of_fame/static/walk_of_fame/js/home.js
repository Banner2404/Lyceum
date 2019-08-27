window.onload = function() {
    var menu = document.getElementById("menu");
    var offset = menu.offsetTop - 30;
    window.onscroll = function() { updateMenuBar(offset) };

    console.log(menu);
}
function updateMenuBar(offset) {
    if (window.pageYOffset > offset) {
        menu.classList.add("sticky");
    } else {
        menu.classList.remove("sticky");
    }
}