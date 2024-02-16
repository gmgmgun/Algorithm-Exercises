function solution(n) {
  return fibonacci(n);
}

const fibonacci = (n) => {
  let a = 1, b = 1;

  for (let i = 2; i <= n; i++) {
    let next = (a + b) % 1234567;
    a = b;
    b = next;
  }

  return n === 0 ? 0 : b;
}
