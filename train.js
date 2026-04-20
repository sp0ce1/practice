
/*
B-TASK (NodeJS)

Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// Masalani yechimi:

function countDigits(data) {
    return data.split("")
        .filter(filterred => filterred >= "0" && filterred <= "9")
        .length;
}


console.log(countDigits());

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