var g = document.getElementById('scatter_options');

const variableScenario = document.getElementById("variable_scenario");
const vsFirstSpan = variableScenario.getElementsByTagName('span')[0];
const vsSecondSpan = variableScenario.getElementsByTagName('span')[1];

for (var i = 0, len = g.children.length; i < len; i++) {
  (function (index) {
    g.children[i].onclick = function () {
      alert(index);
    };
  })(i);
}

katex.render("distance = x", vsFirstSpan, {
  throwOnError: false
});

katex.render("fuel consumed = y", vsFirstSpan, {
  throwOnError: false
});
