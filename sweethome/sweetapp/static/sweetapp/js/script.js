function calculate() {
  var price = parseFloat(document.getElementById('price').value);
  var deposit = parseFloat(document.getElementById('deposit').value);
  var term = parseFloat(document.getElementById('term').value);
  var rate = parseFloat(document.getElementById('rate').value);

  var loan = price - deposit;
  var monthlyRate = rate / 1200;
  var months = term * 12;

  var payment = (loan * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -months));

  document.getElementById('payment').innerHTML = payment.toFixed(2) + ' руб.';
}