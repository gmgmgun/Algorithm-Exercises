"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'pangrams' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function pangrams(s) {
  const usedArr = Array(26).fill(false);
  const lowerStr = s.replaceAll(" ", "").toLowerCase();

  for (let i = 0; i < lowerStr.length; i++) {
    const charCode = lowerStr.charCodeAt(i);
    if (charCode >= 97 && charCode <= 122) {
      usedArr[charCode - 97] = true;
    }
  }

  if (usedArr.indexOf(false) === -1) return "pangram";

  return "not pangram";
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const s = readLine();

  const result = pangrams(s);

  ws.write(result + "\n");

  ws.end();
}
