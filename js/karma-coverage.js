const percentage = {
    lines: 100,
    statements: 100,
    functions: 100,
    branches: 100
}
var summary = require('./karma/coverage/coverage-summary.json');

for (let res in summary.total) {
    if (summary.total[res].pct < percentage[res]) {
        throw new Error(
            `Coverage too low on ${res},
            expected: ${percentage[res]},
            got: ${summary.total[res].pct}`
        );
    }
}