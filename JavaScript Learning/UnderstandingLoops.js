/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowelsList=['a', 'e', 'i', 'o', 'u']
    let newStringVowels = []
    let newStringOthers = []
    for(let char of s) {   
        if(vowelsList.includes(char)) {
            newStringVowels.push(char);  
        }
        else {
            newStringOthers.push(char);
        }
    }
    console.log(newStringVowels.join('\r\n'));
    console.log(newStringOthers.join('\r\n'));
}