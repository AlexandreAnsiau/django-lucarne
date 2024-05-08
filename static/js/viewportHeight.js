// We listen to the load event
// window.addEventListener('load', resizePhoneFix () );
// We listen to the resize event
window.addEventListener('resize', resizePhoneFix () );
// We listen to the load event
window.addEventListener('DOMContentLoaded', resizePhoneFix () );

function resizePhoneFix () {
  // We set a --vh variable in the root element, so vh fit
  // the inner height, even on phone with the browser bar issue.
  let vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', `${vh}px`);

  console.log(vh);
};