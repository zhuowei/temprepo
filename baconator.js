"use strict";
(function() {
function encypher(inputStr) {
	var outputArr = [];
	for (var i = 0; i < inputStr.length; i++) {
		var charCode = inputStr.charCodeAt(i);
		for (var a = 0; a < charCode; a++) {
			var word = a == 0? "Bacon" : "bacon";
			if (a == charCode - 1) {
				word = word + ".";
			} else if (Math.random() < 0.2) {
				word = word + ",";
			}
			outputArr.push(word);
		}
	}
	return outputArr.join(" ");
}

function decypher(inputStr) {
	var input = inputStr.split(" ");
	var currentChar = 0;
	var output = "";
	for (var i = 0; i < input.length; i++) {
		if (input[i].charAt(input[i].length - 1) == ".") {
			output += String.fromCharCode(currentChar + 1);
			currentChar = 0;
		} else {
			currentChar++;
		}
	}
	return output;
}

function loadHandler() {
	document.getElementById("cipher").onclick = function() {
		document.getElementById("output").value = encypher(document.getElementById("input").value);
	};
	document.getElementById("decipher").onclick = function() {
		document.getElementById("input").value = decypher(document.getElementById("output").value);
	};
}

window.onload = loadHandler;
})();
