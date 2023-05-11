"use strict";

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
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
  let plusCnt = 0;
  let minusCnt = 0;
  let zeroCnt = 0;

  for (let i = 0; i < arr.length; i++) {
    switch (true) {
      case arr[i] < 0:
        minusCnt++;
        break;
      case arr[i] === 0:
        zeroCnt++;
        break;
      case arr[i] > 0:
        plusCnt++;
        break;
    }
  }

  console.log((plusCnt / arr.length).toFixed(6));
  console.log((minusCnt / arr.length).toFixed(6));
  console.log((zeroCnt / arr.length).toFixed(6));
}

function main() {
  const n = parseInt(readLine().trim(), 10);

  const arr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  plusMinus(arr);
}
