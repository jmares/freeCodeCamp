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
  return Number.parseFloat(amount).toFixed(2);
}

function checkCashRegister(price, cash, cid) {
  let change = cash - price;
  let output = { status: null, change: [] };
  let amountCID = cashInDrawer(cid);
  if (amountCID < change) {
    output.status = "INSUFFICIENT_FUNDS";
  } else if ( amountCID == change) {
    output.status = "CLOSED";
    output.change = cid;
  } else {
    let revCID = [...cid].reverse();
    let newChange = change;
    let arr = [];
    for (let i = 0; i < denom.length; i++) {
      if ((newChange >= 0.0 ) && (newChange >= denom[i].val) && (revCID[i][1] > 0.0)) {
        let x = Math.floor(newChange / denom[i].val);
        let y = Math.floor(revCID[i][1] / denom[i].val);
        if (x == 0) {
          continue;
        }
        else if (x >= y) {
          newChange = Number.parseFloat(newChange - denom[i].val * y).toFixed(2);
          arr.push([revCID[i][0], Number.parseFloat(y * denom[i].val).toFixed(2)]);
        } else {
          newChange = Number.parseFloat(newChange - denom[i].val * x).toFixed(2);
          arr.push([revCID[i][0], Number.parseFloat(revCID[i][1] - (y-x) * denom[i].val).toFixed(2)]);
        }
      } 
    }
    if (newChange == 0.0) {
      output.status = "OPEN";
      output.change = arr;
    } else {
      output.status = "INSUFFICIENT_FUNDS";
      output.change = [];  
    }
  }
  return output;
}
  
console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));

console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
