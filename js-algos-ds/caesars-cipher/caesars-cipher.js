function rot13(str) {
    let newArr = [];
    for (let i = 0; i < str.length; i++) {
        let code = str.charCodeAt(i);
        if (code < 65 || code > 90) {
            newArr.push(str[i]);
        } else if (code < 78) {
            newArr.push(String.fromCharCode(code + 13)) ;
        } else  {
            newArr.push(String.fromCharCode(code - 13)) ;
        }
    }
    return newArr.join("");
}
  
  console.log(rot13("SERR PBQR PNZC"));
  console.log(rot13("SERR CVMMN!"));
  console.log(rot13("SERR YBIR?"));
  console.log(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT."));

  