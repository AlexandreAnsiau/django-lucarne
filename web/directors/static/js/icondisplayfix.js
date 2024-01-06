var windHeight = window.innerHeight;
const autoScroll = document.getElementById('autoscroll');

var contentHeight = autoScroll.scrollHeight;
var displayedHeight = autoScroll.offsetHeight;
var scrollMax = contentHeight - displayedHeight;

const getLogo = document.getElementsByClassName('logo-lucarne')[0];
const getTeam = document.getElementsByTagName('nav')[0];
const getLink = document.getElementsByTagName('footer')[0].children[0];
const getTrad = document.getElementsByTagName('footer')[0].children[1];

window.addEventListener('resize', () => {
    var windHeight = window.innerHeight;
    var contentHeight = autoScroll.scrollHeight;
    var displayedHeight = autoScroll.offsetHeight;
});

if (contentHeight > displayedHeight) {

    getLink.style.zIndex = -1;
    getTrad.style.zIndex = -1;
};

autoScroll.addEventListener('scroll', function mainOverlap () {      
            
    let scrolled = autoScroll.scrollTop;

    let topLimit = 0.04 * windHeight;
    let bottomLimit = scrollMax - 0.05 * windHeight;

    if (scrolled > topLimit) {
        getLogo.style.zIndex = 0;
        getTeam.style.zIndex = 0;
    } else {
        getLogo.style.zIndex = 2;
        getTeam.style.zIndex = 2;
    };
    if (scrolled < bottomLimit) {
        getLink.style.zIndex = -1;
        getTrad.style.zIndex = -1;
    } else {
        getLink.style.zIndex = 2;
        getTrad.style.zIndex = 2;
    };
})