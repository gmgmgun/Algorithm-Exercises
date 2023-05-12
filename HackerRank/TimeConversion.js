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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s) {
  const numbers = s.match(/\d+/g);
  const merd = s.charAt(s.length - 2) + s.charAt(s.length - 1);
  let hour = numbers[0];

  if (merd === "AM") {
    if (hour === "12") {
      hour = "00";
    }
  } else if (merd === "PM") {
    if (hour !== "12") {
      hour = `${Number(hour) + 12}`;
    }
  }

  const result = `${hour}:${numbers[1]}:${numbers[2]}`;

  return result;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const s = readLine();

  const result = timeConversion(s);

  ws.write(result + "\n");

  ws.end();
}
