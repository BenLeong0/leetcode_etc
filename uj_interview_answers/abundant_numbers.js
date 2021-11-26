// A perfect number is a number for which the sum of its proper divisors is
// exactly equal to the number. For example, the sum of the proper divisors of
// 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

// A number n is called deficient if the sum of its proper divisors is less than
// n and it is called abundant if this sum exceeds n.
// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
// number that can be written as the sum of two abundant numbers is 24. By
// mathematical analysis, it can be shown that all integers greater than 28123
// can be written as the sum of two abundant numbers. However, this upper limit
// cannot be reduced any further by analysis even though it is known that the
// greatest number that cannot be expressed as the sum of two abundant numbers
// is less than this limit.

// Find the sum of all the positive integers which cannot be written as the sum
// of two abundant numbers.


const getProperDivisors = (n) => new Set([...Array(n).keys()].filter(a=>n%a===0));
console.log(getProperDivisors(12));     // Should be { 1, 2, 3, 4, 6 }


const isAbundant = (n) => [...getProperDivisors(n)].reduce((a,b)=>a+b,false) > n;
console.log(isAbundant(12));            // Should be true


const abundantNumbers = [...Array(28123).keys()].slice(1).filter(n=>isAbundant(n));
console.log(abundantNumbers)
console.log(abundantNumbers.length)


const getAbundantSums = () => {
    abundantSums = new Set();
    for (let i=0; i<parseInt(abundantNumbers.length/2)+1; i++) {
        for (let j=i; j<abundantNumbers.length-i; j++) {
            abundantSums.add(abundantNumbers[i] + abundantNumbers[j]);
        }
    }
    return abundantSums
}

abundantSums = getAbundantSums()

const nonAbundantSums = [...Array(28124).keys()].filter(n=>!abundantSums.has(n));

const sumOfNonAbundantSums = nonAbundantSums.reduce((a,b)=>a+b);

console.log(sumOfNonAbundantSums)   // 4179871
