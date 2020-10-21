const Edit_E_Fname = document.getElementById('Edit_E_Fname');
const Edit_E_Lname = document.getElementById('addEmpLname');
const Edit_E_nic = document.getElementById('Edit_E_nic');
const Edit_E_email = document.getElementById('Edit_E_email');
const Edit_E_phone = document.getElementById('Edit_E_phone');


const Edit_E_FnameError = document.querySelector('#addEmpFname + span.error');
const Edit_E_LnameError = document.querySelector('#addEmpLname + span.error');
const Edit_E_nicError = document.querySelector('#Edit_E_nic + span.error');
const Edit_E_emailError = document.querySelector('#Edit_E_email + span.error');
const Edit_E_phoneError = document.querySelector('#Edit_E_phone + span.error');


document.write("connected validations")

form.addEventListener('submit', function (event) {

    if (Edit_E_Fname.Validity.valueMissing) 
    {
        Edit_E_FnameError.textContent("First Name Cannot be null");
        event.preventDefault();
    } else if (Edit_E_Lname.Validity.valueMissing) 
    {
        Edit_E_LnameError.textContent = ('Last Name cannot be null');
        event.preventDefault();
    } else if (Edit_E_nic.Validity.valueMissing)
     {
        Edit_E_nicError.textContent = ('NIC cannot be null');
        event.preventDefault();
    } else if (Edit_E_nic.Validity.tooLong) 
    {
        Edit_E_nicError.textContent = ('NIC value is too long');
        event.preventDefault();
    } else if (Edit_E_nic.Validity.tooShort) 
    {
        Edit_E_nicError.textContent = ('NIC value is too short');
        event.preventDefault();
    } else if (Edit_E_email.Validity.valueMissing) 
    {
        Edit_E_emailError.textContent = ('Email cannot be null');
        event.preventDefault();
    } else if (Edit_E_email.Validity.patternMismatch) 
    {
        Edit_E_emailError.textContent = ('Enter a valid Email');
        event.preventDefault();
    } else if (Edit_E_phone.Validity.valueMissing) 
    {
        Edit_E_phoneError.textContent = ('Phone number cannot be null');
        event.preventDefault();
    } else if (Edit_E_phone.Validity.tooLong) 
    {
        Edit_E_phoneError.textContent = ('Enter a valid phone number');
        event.preventDefault();
    } else if (Edit_E_phone.Validity.tooShort) 
    {
        Edit_E_phoneError.textContent = ('Enter a valid phone number');
        event.preventDefault();
    }
});
