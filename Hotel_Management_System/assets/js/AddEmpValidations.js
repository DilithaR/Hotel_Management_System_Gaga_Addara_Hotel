const empImgUpload = document.getElementById('empImgUpload');
const addEmpFname = document.getElementById('addEmpFname');
const addEmpLname = document.getElementById('addEmpLname');
const addEmpNIC = document.getElementById('addEmpNIC');
const addEmpEmail = document.getElementById('addEmpEmail');
const addEmpPhone = document.getElementById('addEmpPhone');



const empImgUploadError = document.querySelector('#empImgUpload + span.error');
const addEmpFnameError = document.querySelector('#addEmpFname + span.error');
const addEmpLnameError = document.querySelector('#addEmpLname + span.error');
const addEmpNICError = document.querySelector('#addEmpNIC + span.error');
const addEmpEmailError = document.querySelector('#addEmpEmail + span.error');
const addEmpPhoneError = document.querySelector('#addEmpPhone + span.error');


document.write("connected validations")

form.addEventListener('submit', function (event) {

    if (empImgUpload.validity.valueMissing) {
        empImgUploadError.textContent("Image is essecial");
        event.preventDefault();
    } 
    else if (addEmpFname.Validity.valueMissing) {
        addEmpFnameError.textContent("First Name Cannot be null");
        event.preventDefault();
    } 
    else if (addEmpLname.Validity.valueMissing) {
        addEmpLnameError.textContent = ('Last Name cannot be null');
        event.preventDefault();
    } 
    else if (addEmpNIC.Validity.valueMissing) {
        addEmpNICError.textContent = ('NIC cannot be null');
        event.preventDefault();
    }
    else if (addEmpNIC.Validity.tooLong) {
        addEmpNICError.textContent = ('NIC value is too long');
        event.preventDefault();
    }
    else if (addEmpNIC.Validity.tooShort) {
        addEmpNICError.textContent = ('NIC value is too short');
        event.preventDefault();
    }
    else if (addEmpEmail.Validity.valueMissing) {
        addEmpEmailError.textContent = ('Email cannot be null');
        event.preventDefault();
    }
    else if (addEmpEmail.Validity.patternMismatch) {
        addEmpEmailError.textContent = ('Enter a valid Email');
        event.preventDefault();
    }
    else if (addEmpPhone.Validity.valueMissing) {
        addEmpPhoneError.textContent = ('Phone number cannot be null');
        event.preventDefault();
    }
    else if (addEmpPhone.Validity.tooLong) {
        addEmpPhoneError.textContent = ('Enter a valid phone number');
        event.preventDefault();
    }
    else if (addEmpPhone.Validity.tooShort) {
        addEmpPhoneError.textContent = ('Enter a valid phone number');
        event.preventDefault();
    }
});
