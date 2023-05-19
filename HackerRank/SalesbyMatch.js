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
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

function sockMerchant(n, ar) {
  const cntArr = [];
  const checkArr = [];

  let cnt = 0;
  let total = 0;

  for (let i = 0; i < ar.length; i++) {
    if (checkArr.indexOf(ar[i]) === -1) {
      let j = i;
      checkArr.push(ar[i]);
      cnt++;
      while (ar.indexOf(ar[i], j + 1) !== -1) {
        j = ar.indexOf(ar[i], j + 1);
        cnt++;
      }
      cntArr.push(cnt);
      cnt = 0;
    }
  }

  for (let i = 0; i < cntArr.length; i++) {
    if (cntArr[i] > 1) {
      if (cntArr[i] % 2 === 0) {
        total += cntArr[i] / 2;
      } else {
        total += (cntArr[i] - 1) / 2;
      }
    }
  }

  return total;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const ar = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arTemp) => parseInt(arTemp, 10));

  const result = sockMerchant(n, ar);

  ws.write(result + "\n");

  ws.end();
}
