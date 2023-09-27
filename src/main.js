var mj = require("mathjax-node");
var fs = require("fs")

var equation = '\\frac{1}{\\sqrt{x^2 + 1}}';



mj.typeset({ math: equation, format: "TeX", svg: true }, function (data) {
    fs.writeFile("out.svg",data.svg, err => {if(err) console.log("Error")})
});