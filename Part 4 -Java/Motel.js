const customer = {
  firstName: 'Danny',
  lastName: 'Bill',
  birthDate: 'Aug 7, 1999',
  gender: 'Male',
  roomPreferences: [101, 111, 121],
  paymentMethod: 'Credit Card',
  mailingAddress: {
    street: '123 Water St.',
    city: 'St. Johns',
    province: 'NL',
    postal: 'A1F6J7',
    country: 'CANADA',
  },
  phoneNumber: `709-123-4567`,
  checkInDate: {
    date: 'Dec 01, 2023',
    timeOfDay: ['Morning', 'Evening', 'Night'],
  },
  checkOutDate: {
    date: 'Jan 20, 2024',
    timeOfDay: ['Morning', 'Evening', 'Night'],
  },

  

  getAge: function() {
    const birthYear = new Date(this.birthDate).getFullYear();
    const currYear = new Date().getFullYear();
    age = currYear - birthYear;
    return age;
  },

  
  getStayPeriod: function () {
    const checkIn = new Date(this.checkInDate.date);
    const checkOut = new Date(this.checkOutDate.date);
    const timeDiff = Math.abs(checkOut - checkIn);
    const dayDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
    return dayDiff+" days";
  },
};

let CustAge = customer.getAge();
console.log("Customer's age:", CustAge);

let timeStayed = customer.getStayPeriod();
console.log("Customer's stay period:", timeStayed);

let greeting = `Hello ${customer.firstName}! Welcome to Sleep Tite Motel, where you can rest your weary head, and be sure to sleep tite!`;
console.log(greeting);

let html = `
  <ul>
    <center><h1>${greeting}</h1></center>
    <p></p>
    <h3>Customer information</h3>
    <li>First Name: ${customer.firstName}</li>
    <li>Last Name: ${customer.lastName}</li>
    <li>Age: ${customer.getAge()}</li>
    <li>Gender: ${customer.gender}</li>
    <li>Phone Number: ${customer.phoneNumber}</li>
    <li>Room Preferences: ${customer.roomPreferences.join(", ")}</li>
    <li>Payment Method: ${customer.paymentMethod}</li>
    <p></p>
    <h3>Mailing Address:</h3>
    <li>Street Address: ${customer.mailingAddress.street}</li>
    <li>Province: ${customer.mailingAddress.province}</li>
    <li>Postal Code: ${customer.mailingAddress.postal}</li>
    <li>Country: ${customer.mailingAddress.country}</li> 
    <p></p>
    <h3>Stay Information:</h3>
    <li>Check-in Date: ${customer.checkInDate.date}, At time of day: ${customer.checkInDate.timeOfDay[0]}</li>
    <li>Check-out Date: ${customer.checkOutDate.date}, At time of day: ${customer.checkInDate.timeOfDay[2]}</li>
    <li>Time stayed: ${timeStayed}</li>
  </ul>
`;

console.log(html);
document.body.innerHTML = html;
