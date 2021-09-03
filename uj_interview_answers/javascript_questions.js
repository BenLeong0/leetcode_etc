const FIB_LIMIT = 4000000;
const TEST_STRING = 'they mostly come at night. Mostly.';

///////////////

const threeFiveMultiplesSum = (n) => [...Array(n).keys()].reduce((a,b)=>(b%3&&b%5)?a:a+b);

console.log(threeFiveMultiplesSum(10))    // 23
console.log(threeFiveMultiplesSum(1000))  // 233168

///////////////

const fibSum = (n) => {
  var stack = [0,1];
  while (stack[stack.length-1] < n) {stack.push(stack[stack.length-1]+stack[stack.length-2])}
  return stack.slice(0,stack.length-1).reduce((a,b)=>(b%2===0)?a+b:a);
}

const fibSumIterative = (n) => {
  var prev = 0;
  var curr = 1;
  var sum = 0;
  var next;
  while (curr < n) {
    if (curr % 2 === 0) {sum += curr}
    next = curr + prev;
    prev = curr
    curr = next
  }
  return sum
}

console.log(fibSum(FIB_LIMIT))            // 4613732
console.log(fibSumIterative(FIB_LIMIT))   // 4613732

///////////////

const sortedNoDupes = (s) => [...new Set(s)].sort().join('');

const reverseSentence = (s) => s.split(' ').reverse();

console.log(sortedNoDupes(TEST_STRING))   // " .Maceghilmnosty"
console.log(reverseSentence(TEST_STRING)) // [ 'Mostly.', 'night.', 'at', 'come', 'mostly', 'they' ]
