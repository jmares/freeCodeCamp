function telephoneCheck(str) {
    var regex = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/;
    return regex.test(str);
}  

console.log("555-555-5555: " + telephoneCheck("555-555-5555"));
console.log("1 555-555-5555: " + telephoneCheck("1 555-555-5555"));
console.log("1 (555) 555-5555: " + telephoneCheck("1 (555) 555-5555"));
console.log("5555555555: " + telephoneCheck("5555555555"));
console.log("(555)555-5555: " + telephoneCheck("(555)555-5555"));
console.log("1(555)555-5555: " + telephoneCheck("1(555)555-5555"));
console.log("555-5555: " + telephoneCheck("555-5555"));
console.log("5555555: " + telephoneCheck("5555555"));
console.log("1 555)555-5555: " + telephoneCheck("1 555)555-5555"));
console.log("1 555 555 5555: " + telephoneCheck("1 555 555 5555"));
console.log("1 456 789 4444: " + telephoneCheck("1 456 789 4444"));
console.log("123**&!!asdf#: " + telephoneCheck("123**&!!asdf#"));
console.log("55555555: " + telephoneCheck("55555555"));
console.log("(6054756961): " + telephoneCheck("(6054756961)"));
console.log("2 (757) 622-7382: " + telephoneCheck("2 (757) 622-7382"));
console.log("0 (757) 622-7382: " + telephoneCheck("0 (757) 622-7382"));
console.log("-1 (757) 622-7382: " + telephoneCheck("-1 (757) 622-7382"));
console.log("2 757 622-7382: " + telephoneCheck("2 757 622-7382"));
console.log("10 (757) 622-7382: " + telephoneCheck("10 (757) 622-7382"));
console.log("27576227382: " + telephoneCheck("27576227382"));
console.log("(275)76227382: " + telephoneCheck("(275)76227382"));
console.log("2(757)6227382: " + telephoneCheck("2(757)6227382"));
console.log("2(757)622-7382: " + telephoneCheck("2(757)622-7382"));
console.log("555)-555-5555: " + telephoneCheck("555)-555-5555"));
console.log("(555-555-5555: " + telephoneCheck("(555-555-5555"));
console.log("(555)5(55?)-5555: " + telephoneCheck("(555)5(55?)-5555"));
