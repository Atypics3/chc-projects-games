// selects the id called "tip-form" and whenever a change occurs, the function activates
document.querySelector('#tip-form').onchange = function(){
  // let bill be a number that is gotten from the id "billTotal" and turns it into a number
  let bill = Number(document.getElementById('billTotal').value);
  
  // let tip be a number that is gotten by the id "tipInput"
  let tip = document.getElementById('tipInput').value;

  // outputs the value of tip into "tipOutput" and displays it in the HTML file
  document.getElementById('tipOutput').innerHTML = `${tip}%`;

  // calculates the tip value given a bill and a tip
  let tipValue = bill * (tip / 100);

  // gets the final bill value that will need to be paid
  let finalBill = bill + tipValue;

  // returns the value of tipAmount into the ID "tipAmount"
  let tipAmount = document.querySelector('#tipAmount');

  // returns the value of totalBillWithTip into the ID "totalBillWithTip"
  let totalBillWithTip = document.querySelector('#totalBillWithTip');

  // sets the tip amount and total bill w/ tip to 2 decimal places past the decimal
  tipAmount.value = tipValue.toFixed(2);  
  totalBillWithTip.value = finalBill.toFixed(2);

  // shows results
  document.getElementById('results').style.display='block';
}