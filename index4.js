document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const terms = document.getElementById('terms').checked;

    if (name && email && gender && terms) {
        alert(`Name: ${name}\nEmail: ${email}\nGender: ${gender}\nTerms accepted: ${terms}`);
        // Here you can handle the form data as needed
    } else {
        alert('Please fill out all required fields.');
    }
});
