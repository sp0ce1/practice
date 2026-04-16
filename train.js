/* A-TASK: 

Savol: 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


// Masalani yechimi:

function countLetter(letter, word, callback) {
    let count = 0;
    if (typeof letter !== "string") callback("insert only letter", null);
    else {
        for (let i = 0; i < word.length; i++) {
            if (letter === word[i]) {
                count++
            }
        }
    }
    callback(null, count);
};

countLetter("a", "Mashaqqat", (err, data) => {
    if (err) console.log("ERROR:", err);
    else {
        console.log("data:", data);
    }
});