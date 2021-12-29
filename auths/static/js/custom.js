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
        if (userDate == 'Invalid Date') {
            alert('Date is invalid. Provide a valid date');
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

    // calculate age from date of birth for update profile

    $("#update_date_of_birth").focusout(function() {
        var userDateUpdate = new Date($("#update_date_of_birth").val());
        if (userDateUpdate == 'Invalid Date') {
            alert('Date is invalid. Provide a valid date');
        } else {
            let dd = String(userDateUpdate.getDate()).padStart(2, '0');
            let mm = String(userDateUpdate.getMonth() + 1).padStart(2, '0'); //January is 0!
            let yyyy = userDateUpdate.getFullYear();
            userDateUpdate = yyyy + '-' + mm + '-' + dd
            calculateUpdateAge(userDateUpdate);
        }
    });

    function calculateUpdateAge(userDateUpdate) {
        let ageDiff = Date.now() - new Date(userDateUpdate).getTime();
        let ageDate = new Date(ageDiff);
        let calcAge = Math.abs(ageDate.getUTCFullYear() - 1970)
        $("#update_age").attr('readonly', 'true');
        $("#update_age").val(calcAge);
    };


    // calculate years for number of service year

    $("#service_year").hide();
    $("#first_appointment").focusout(function() {
        var serviceDate = new Date($("#first_appointment").val());
        if (serviceDate == 'Invalid Date') {
            alert('Date is invalid. Provide a valid date');
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


    // calculate years for number of service year update

    $("#update_first_appointment").focusout(function() {
        var serviceDateUpdate = new Date($("#update_first_appointment").val());
        if (serviceDateUpdate == 'Invalid Date') {
            alert('Date is invalid. Provide a valid date');
        } else {
            let _dd = String(serviceDateUpdate.getDate()).padStart(2, '0');
            let _mm = String(serviceDateUpdate.getMonth() + 1).padStart(2, '0'); //January is 0!
            let _yyyy = serviceDateUpdate.getFullYear();
            serviceDateUpdate = _yyyy + '-' + _mm + '-' + _dd
            calculateServiceAgeUpdate(serviceDateUpdate);
        }
    });

    function calculateServiceAgeUpdate(serviceDateUpdate) {
        let _ageDiff = Date.now() - new Date(serviceDateUpdate).getTime();
        let _ageDate = new Date(_ageDiff);
        let _calcAge = Math.abs(_ageDate.getUTCFullYear() - 1970)
        $("#update_years_in_service").attr('readonly', 'true');
        $("#update_years_in_service").val(_calcAge);
    };

    // display schools by selected zone
    $('#current_posting_zone').focusout(function() {
        $(".current_posting_school").empty();
        var selectedZoneId = $('#current_posting_zone option:selected').val()
        $.ajax({
            url: '/auths/get_school_by_zone/',
            data: {
                'selected_zone_id': selectedZoneId
            },
            dataType: 'json',
            success: function(schools) {
                $('.current_posting_school').append(schools.data)
            }
        });
    });

    // add multiple images
    $('input#add_image').on('click', function(e) {
        e.preventDefault()
        var images = document.getElementById('images');

        // create input file element
        var newInput = document.createElement('input');
        newInput.type = 'file';
        newInput.name = 'documents'

        /* create input text element
        var newInputText = document.createElement('input');
        newInputText.type = 'text';
        newInputText.name = 'document_title'
        */

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
            //images.appendChild(newInputText)
        images.appendChild(newInput)
        images.appendChild(newClose)
        images.appendChild(br)
        images.appendChild(br1)
    });

    $('#close_btn').on('click', function() {
        $(this).remove()
    })

    // display button for zones and schools in update profile
    $('button#show_zone').click(function(e) {
        e.preventDefault()
        $('#current_posting_zone').show()
        $('.current_posting_school').show()
    });

    // solve two variable simultaneous equations

    $('form#simultaneous_two').submit(function(e) {
        e.preventDefault()
        $('.show_result').empty()
        var a = $("input[name='a']").val()
        var b = $("input[name='b']").val()
        var c = $("input[name='c']").val()
        var p = $("input[name='p']").val()
        var q = $("input[name='q']").val()
        var r = $("input[name='r']").val()
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            //method: 'POST',
            url: '/mathematics/simultaneous_eqn_answer/',
            data: {
                'a': a,
                'b': b,
                'c': c,
                'p': p,
                'q': q,
                'r': r,
                'csrfmiddlewaretoken': csrfmiddlewaretoken
            },
            dataType: 'json',
            success: function(data) {
                $('.show_result').append(`
                    <h3>Value of unknown 1 = ${data.unknown_1}</h3>
                    <h3>Value of unknown 2 = ${data.unknown_2}</h3>
                `)
                $('.show_result').show()
            }
        });
    })

    // solve three variable simultaneous equations

    $('form#simultaneous_three').submit(function(e) {
        e.preventDefault()
        $('.show_answer').empty()
        var a1 = $("input[name='a1']").val()
        var b1 = $("input[name='b1']").val()
        var c1 = $("input[name='c1']").val()
        var d1 = $("input[name='d1']").val()

        var a2 = $("input[name='a2']").val()
        var b2 = $("input[name='b2']").val()
        var c2 = $("input[name='c2']").val()
        var d2 = $("input[name='d2']").val()

        var a3 = $("input[name='a3']").val()
        var b3 = $("input[name='b3']").val()
        var c3 = $("input[name='c3']").val()
        var d3 = $("input[name='d3']").val()
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            //method: 'POST',
            url: '/mathematics/simultaneous_3_eqn_answer/',
            data: {
                'a1': a1,
                'b1': b1,
                'c1': c1,
                'd1': d1,
                'a2': a2,
                'b2': b2,
                'c2': c2,
                'd2': d2,
                'a3': a3,
                'b3': b3,
                'c3': c3,
                'd3': d3,
                'csrfmiddlewaretoken': csrfmiddlewaretoken
            },
            dataType: 'json',
            success: function(data) {
                $('.show_answer').append(`
                    <h3>Value of unknown 1 = ${data.unknown_1}</h3>
                    <h3>Value of unknown 2 = ${data.unknown_2}</h3>
                    <h3>Value of unknown 3 = ${data.unknown_3}</h3>
                `)
                $('.show_answer').show()
            }
        });
    })

});