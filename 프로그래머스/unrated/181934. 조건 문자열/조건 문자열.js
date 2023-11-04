function solution(ineq, eq, n, m) {
    return (
        (ineq === '>' && ((eq === '=' && n >= m) || (eq === '!' && n > m))) ||
        (ineq === '<' && ((eq === '=' && n <= m) || (eq === '!' && n < m)))
    ) ? 1 : 0;
}
