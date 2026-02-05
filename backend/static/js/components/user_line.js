const sliderM = document.getElementById('slider_m');
const sliderC = document.getElementById('slider_c');
const imageSvg = document.getElementById("svg-plot");
const tooltip = document.querySelector('#tooltip');

let sliderArr = [sliderM, sliderC];

let totalError = document.getElementById("error-total");
totalError = totalError.getElementsByTagName("span")[0];
let errorArray;
let last5;

imageSvg.addEventListener('mouseover', (e) => {
  // Check if the hovered element is the path inside #line2d_18
  const g = e.target.closest('g');
  const index = last5.findIndex(el => el === g);
  if (index != -1) {

    console.log("hovered");

    const popperInstance = Popper.createPopper(e.target, tooltip, {
      modifiers: [
        {
          name: 'offset',
          options: {
            offset: [0, 8],
          },
        },
      ],
    });

    function show() {
      tooltip.setAttribute('data-show', '');
      tooltip.innerText = errorArray[index];
      popperInstance.update();
    }

    function hide() {
      tooltip.removeAttribute('data-show');
    }

    const showEvents = ['mouseenter', 'focus'];
    const hideEvents = ['mouseleave', 'blur'];

    showEvents.forEach((event) => {
      e.target.addEventListener(event, show);
    });

    hideEvents.forEach((event) => {
      e.target.addEventListener(event, hide);
    });
  }
});

sliderArr.forEach((elem) => {
  elem.addEventListener("change", function () {
    fetch('/update-plot', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ m: sliderM.value, c: sliderC.value })
    })
      .then(res => res.json())
      .then(src => {
        totalError.innerText = src.error;
        imageSvg.innerHTML = src.url;
        errorArray = src.errorArray;

        // populating variables not dependant on request response
        const axes = document.querySelector('#figure_1 #axes_1');
        const lines = [...axes.querySelectorAll('g[id^="line2d"]')];
        last5 = lines.slice(-5);
      });
      
  });
});
