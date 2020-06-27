// const axios = require('axios');

// const text = 'We can remove most sins if we have a witness standing by as we are about to go wrong.'

// axios.post('http://localhost:9000/?properties={"annotators":"tokenize,ssplit,parse"}', {data: text}).then((res) => {

//     console.log(res.data.sentences[0].enhancedDependencies)
// })

let sentence =
  "That is , wanting the past to be more than what it was -LRB- different , better , still here , etc. -RRB- or wanting the future to unfold exactly as you expect -LRB- with hardly a thought as to how that might affect other people -RRB- .";

console.log(sentence + "\n\n");

const clauses = [
  "what it was",
  "as you expect -LRB- with hardly a thought as to how that might affect other people -RRB-",
  "how that might affect other people",
].reverse();

let newClauses = [];

clauses.forEach((clause, index) => {
  if (index === 0) {
    newClauses.push(clause);
  } else if (clause.indexOf(clauses[index - 1]) >= 0) {
    clause.split(clauses[index - 1]).forEach((v) => {
      newClauses.push(v);
    });
  } else {
    newClauses.push(clause);
  }
});

newClauses = newClauses.filter((v) => {
  return v !== "";
});

console.log({ newClauses });

const result = [];

newClauses.forEach((clause, index) => {
  // if (index) return;

  const rSentence = sentence.split("").reverse().join("");
  const rClause = clause.split("").reverse().join("");

  const startIndex = rSentence.indexOf(rClause);
  const endIndex = startIndex + rClause.length;

  if (startIndex > 0) {
    const prev = rSentence.slice(0, startIndex - 1);
    result.unshift(prev.split("").reverse().join(""));
  }

  result.unshift(clause);

  if (rSentence.length > endIndex && index === newClauses.length - 1) {
    const post = rSentence.slice(endIndex + 1);
    result.unshift(post.split("").reverse().join(""));
  }

  sentence = rSentence
    .slice(endIndex + 1)
    .split("")
    .reverse()
    .join("");

  console.log(sentence);
});

console.log(result);

let cau = "";

result.forEach((v) => {
  cau = cau + " " + v;
});

console.log(cau.split(" ,").join(",").split(" .").join(".").trim());
