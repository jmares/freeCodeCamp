var denom = [
  { name: "ONE HUNDRED", val: 100.0 },
  { name: "TWENTY", val: 20.0 },
  { name: "TEN", val: 10.0 },
  { name: "FIVE", val: 5.0 },
  { name: "ONE", val: 1.0 },
  { name: "QUARTER", val: 0.25 },
  { name: "DIME", val: 0.1 },
  { name: "NICKEL", val: 0.05 },
  { name: "PENNY", val: 0.01 }
];

function cashInDrawer(cid) {
  let amount = 0;
  for (let i = 0; i < cid.length; i++) {
    amount += cid[i][1];
  }
  return amount;
}

function checkCashRegister(price, cash, cid) {
  let change = cash - price;
  let output = { status: null, change: [] };
  let amountCID = cashInDrawer(cid);
  //console.log("amountCID = " + amountCID + "| change = " + change);
  if (amountCID < change) {
    output.status = "INSUFFICIENT_FUNDS";
  } else if ( amountCID == change) {
    output.status = "CLOSED";
    output.change = cid;
  } else {
    let revCID = cid.reverse();
    for (let i = 0; i < denom.length; i++) {
      if ((change > 0 ) && (change > denom[i].value) && (revCID[i][1] > 0)) {
        // hier komt rest van de code
      } 
      console.log(denom[i]);
    }
    output.status = "BUSY";
    output.change = [0];
    console.log(revCid);
  }
  return output;
}
  
console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));