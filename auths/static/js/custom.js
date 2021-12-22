function showPassword() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function showPassword2() {
    var x = document.getElementById("password2");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
};

$(document).ready(function() {

    // calculate age from date of birth

    $("#div_age").hide();
    $("#date_of_birth").focusout(function() {
        var userDate = new Date($("#date_of_birth").val());
        console.log(userDate)
        if (userDate == 'Invalid Date') {
            alert('Date is invalid. Provide a valid date in YYYY-MM-DD format');
        } else {
            let dd = String(userDate.getDate()).padStart(2, '0');
            let mm = String(userDate.getMonth() + 1).padStart(2, '0'); //January is 0!
            let yyyy = userDate.getFullYear();
            userDate = yyyy + '-' + mm + '-' + dd
            calculateAge(userDate);
        }
    });

    function calculateAge(userDate) {
        let ageDiff = Date.now() - new Date(userDate).getTime();
        let ageDate = new Date(ageDiff);
        let calcAge = Math.abs(ageDate.getUTCFullYear() - 1970)
        $("#age").attr('readonly', 'true');
        $("#age").val(calcAge);
        $("#div_age").show();
    };

    // calculate years for number of service year

    $("#service_year").hide();
    $("#first_appointment").focusout(function() {
        var serviceDate = new Date($("#first_appointment").val());
        console.log(serviceDate)
        if (serviceDate == 'Invalid Date') {
            alert('Date is invalid. Provide a valid date in YYYY-MM-DD format');
        } else {
            let dd = String(serviceDate.getDate()).padStart(2, '0');
            let mm = String(serviceDate.getMonth() + 1).padStart(2, '0'); //January is 0!
            let yyyy = serviceDate.getFullYear();
            serviceDate = yyyy + '-' + mm + '-' + dd
            calculateServiceAge(serviceDate);
        }
    });

    function calculateServiceAge(serviceDate) {
        let ageDiff = Date.now() - new Date(serviceDate).getTime();
        let ageDate = new Date(ageDiff);
        let calcAge = Math.abs(ageDate.getUTCFullYear() - 1970)
        $("#years_in_service").attr('readonly', 'true');
        $("#years_in_service").val(calcAge);
        $("#service_year").show();
    };

    // display schools by selected zone
    $('#current_posting_zone').focusout(function() {
        $(".current_posting_school").empty();
        var selectedZone = $('#current_posting_zone option:selected').val()
        $.ajax({
            url: '/auths/get_school_by_zone/',
            data: {
                'selected_zone': selectedZone
            },
            dataType: 'json',
            success: function(schools) {
                console.log(schools.data)
                $('.current_posting_school').append(schools.data)
            }
        });
    });

    // add multiple images
    $('input#add_image').on('click', function(e) {
        e.preventDefault()
        var images = document.getElementById('images');

        var newInput = document.createElement('input');
        newInput.type = 'file';
        newInput.name = 'documents'

        var preview = document.createElement('img')
        preview.style.width = '200px'
        preview.style.height = '300px'

        newInput.onchange = function() {
            if (this.files && this.files[0]) {
                var fileReader = new FileReader()
                fileReader.onload = function(ev2) {
                    preview.src = ev2.target.result;
                };

                fileReader.readAsDataURL(this.files[0])
            }
        }

        var newClose = document.createElement('i');
        newClose.className = 'fa fa-times';
        newClose.id = 'close_btn';

        var br = document.createElement('br')
        var br1 = document.createElement('br')

        images.appendChild(preview)
        images.appendChild(newInput)
        images.appendChild(newClose)
        images.appendChild(br)
        images.appendChild(br1)
    });

    $('#close_btn').on('click', function() {
        $(this).remove()
    })

});