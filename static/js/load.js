window.addEventListener('DOMContentLoaded', function () {
    if (sessionStorage.getItem("visited") === null) {
        
        var intro = document.getElementsByClassName('intro')[0];

        intro.style.display = 'flex';

        setTimeout (function introDisappear () {

            intro.style.display = 'none';

        }, 6000);

        sessionStorage.setItem("visited", true);
    }
})