
import GradientDescent from "/static/js/math/gradient_descent.js";

var g = document.getElementById('scatter_options');
const interactive = document.getElementById("interactive-3d");

for (var i = 0, len = g.children.length; i < len; i++) {
  (function (index) {
    g.children[i].onclick = function () {
      alert(index);
    };
  })(i);
}

document.addEventListener("DOMContentLoaded", () => {
  fetch('/live-descent', {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  })
  .then(res => res.json())
  .then(src => {
  const dataZ3 = {x: src.M, y:src.C,z: src.E,type: 'surface', opacity: 0.15 };
  const X = [1, 2, 3, 4, 5];
  const y = [2, 5, 18, 22, 27];
  const gdLoss = new GradientDescent(X, y);

  var w = -10; //m
  var b = 0; //c
  var e = gdLoss.cost(w,b);
  

  var gdLiveScatter = {
      x:[w], y: [b], z: [e],
      mode: 'markers',
      marker: {
        size: 5,
        line: {
        color: 'rgba(0, 0, 0, 0.14)',
        width: 0.5},
        opacity: 1},
      type: 'scatter3d'
  };
  var layout = {
    scene:{
    xaxis: {
      nticks: 5,
      range: [-10, 20],
    },
    yaxis: {
      nticks: 7,
      range: [-10, 10],
    },
    zaxis: {
    nticks: 8,
    range: [0, 17500],
    }},
  };


  Plotly.react(interactive, [dataZ3, gdLiveScatter], layout);

  const iterations = 50;
  
  var cnt = 0;

  var interval = setInterval(function() {
    
    let alpha = cnt < 100 ? 0.001: 0.01;

    // Calculate the gradients of the cost function with respect to w and b
    const [dj_dw, dj_db] = gdLoss.gradient(w, b);

    // Update w and b by taking a step in the opposite direction of the gradients
    w = w - alpha * dj_dw;
    b = b - alpha * dj_db;
    e = gdLoss.cost(w,b);
        
    Plotly.extendTraces(interactive, {x: [[w]], y: [[b]], z: [[e]]}, [1])
    

    if(++cnt === 400) clearInterval(interval);
  }, 100);

  })
})





