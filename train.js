
/* F-TASK (NodeJS)

Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa
true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi 
*/

// Masalani yechimi:

function getReverse(task) {
    const misol = task.split("");

    for (let i = 0; i < misol.length; i++) {
        if (misol.filter(harf => harf === misol[i]).length > 1) {
            return true;
        }
    }
    return false
}
const result = getReverse("hello")
console.log(result)









/*
E-TASK (NodeJS)

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/

// Masalani yechimi:
// node train.js

// function getReverse(teskari) {
//     return teskari.split("").reverse().join("");
// };
// console.log(getReverse("hello"));






/* D-TASK (NodeJS)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta
qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini. */

// Masalani yechimi:


// function getHighestIndex(raqam) {
//     let katta = Math.max(...raqam);
//     const index = raqam.indexOf(katta)
//     return index
// }

// const result = getHighestIndex([5, 21, 12, 21, 8])
// console.log(result)




/*
C-TASK (NodeJS)

Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string
bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/

// Masalani yechimi:

// function checkContent(birinchi, ikkinchi) {
//     let birinchiSorted = birinchi.split("").sort().join("");
//     let ikkinchiSorted = ikkinchi.split("").sort().join("");

//     return birinchiSorted === ikkinchiSorted;
// }

// console.log(checkContent("mitgroup", "gmtiprou"));





/*
B-TASK (NodeJS)

Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// Masalani yechimi:

// function countDigits(data) {
//     return data.split("")
//         .filter(filterred => filterred >= "0" && filterred <= "9")
//         .length;
// }


// console.log(countDigits("ad2a54y79wet0sfgb9"));

// ====================================================================
/* A-TASK:

Savol: 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


// Masalani yechimi:

// function countLetter(letter, word, callback) {
//     let count = 0;
//     if (typeof letter !== "string") callback("insert only letter", null);
//     else {
//         for (let i = 0; i < word.length; i++) {
//             if (letter === word[i]) {
//                 count++
//             }
//         }
//     }
//     callback(null, count);
// };

// countLetter("a", "Mashaqqat", (err, data) => {
//     if (err) console.log("ERROR:", err);
//     else {
//         console.log("data:", data);
//     }
// });