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
    //===========================================================================================
    // add multiple images
    /*
    $('input#add_image').on('click', function(e) {
        e.preventDefault()
        var images = document.getElementById('images');

        // create input file element
        var newInput = document.createElement('input');
        newInput.type = 'file';
        newInput.name = 'documents'

         create input text element
        var newInputText = document.createElement('input');
        newInputText.type = 'text';
        newInputText.name = 'document_title'
        

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
    */
    //=====================================================================================================
    // add multiple images new
    var maxField = 20; // input fields increment limitation
    //var addButton = $('.add_button'); // add button selector
    var images = $('#images'); // input field wrapper
    var fieldHTML = `
    <div>
        <input name='document_title[]' type="text" value="" class="form-control" placeholder="Add Name OF Document">
        <input type="file" name="documents">
        <i class="fa fa-times close_btn"></i>
    </div>
    <br>`
        //  onchange="showPreview(event);
    var x = 1

    $('input#add_image').on('click', function(e) {
        e.preventDefault()
            // check maximum number of input fields
        if (x < maxField) {
            images.append(fieldHTML);
            x++
        }
    });

    $(images).on('click', '.close_btn', function(e) {
        e.preventDefault()
        $(this).parent('div').remove()
        x--
    });

    function showPreview(event) {
        console.log('working')
        if (event.target.files.length > 0) {
            var src = URL.createObjectURL(event.target.files[0]);
            var preview = $('#preview')
            preview.src = src;
            preview.style.display = 'block'
        }
    }

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
    });

    // solve quadratic equations

    $('form#quadratic_eqn').submit(function(e) {
        e.preventDefault()
        $('.result').empty()
        var a_1 = $("input[name='a_1']").val()
        var b_1 = $("input[name='b_1']").val()
        var c_1 = $("input[name='c_1']").val()
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        if (parseInt(a_1) == 0) {
            alert('The Coefficient of x 2 cannot be Zero')
        } else {
            $.ajax({
                //method: 'POST',
                url: '/mathematics/quadratic_eqn_answer/',
                data: {
                    'a_1': a_1,
                    'b_1': b_1,
                    'c_1': c_1,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                dataType: 'json',
                success: function(data) {
                    $('.result').append(`
                        <h3>${data.info}</h3>
                        <h3>Value of root 1 = ${data.root_1}</h3>
                        <h3>Value of root 2 = ${data.root_2}</h3>
                    `)
                    $('.result').show()
                }
            });
        }
    })

    // Convert from base 10 to another base

    $('form#convert_from_10').submit(function(e) {
        e.preventDefault()
        $('.from_base_10').empty()
        var num_10 = $("input[name='num_10']").val()
        var num_x = $("input[name='num_x']").val()
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        if ((parseInt(num_10) < 0) || (parseInt(num_x) < 0)) {
            alert('Number cannot be negative')
        } else if (parseInt(num_x) < 2) {
            alert('Base cannot be less than 2')
        } else if ((parseInt(num_10) == 0) || (parseInt(num_x) == 0)) {
            alert('Number cannot be Zero')
        } else if (parseInt(num_10) % 1 != 0) {
            alert('The base 10 number must be a whole number')
        } else {
            $.ajax({
                //method: 'POST',
                url: '/mathematics/from_base_10_answer/',
                data: {
                    'num_10': num_10,
                    'num_x': num_x,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                dataType: 'json',
                success: function(data) {
                    $('.from_base_10').append(`
                        <h3>The value of ${num_10} from base 10 to base ${num_x} = ${data.value}</h3>
                    `)
                    $('.from_base_10').show()
                }
            });
        }
    });

    // Convert from another base to base 10

    $('form#to_base_10').submit(function(e) {
        e.preventDefault()
        $('.to_base_10').empty()
        var number = $("input[name='number']").val()
        var base = $("input[name='base']").val()
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        if (greatestDigit(number) >= parseInt(base)) {
            alert('The base of the number cannot be less or equal to the largest digit of the number')
        } else if ((parseInt(number) < 0) || (parseInt(base) < 0)) {
            alert('Number cannot be negative')
        } else if (parseInt(number) == 0) {
            alert('The base 10 number cannot be Zero')
        } else if (parseInt(number) % 1 != 0) {
            alert('The base 10 number must be a whole number')
        } else {
            $.ajax({
                //method: 'POST',
                url: '/mathematics/to_base_10_answer/',
                data: {
                    'number': number,
                    'base': base,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                dataType: 'json',
                success: function(data) {
                    $('.to_base_10').append(`
                        <h3>The value of ${number} from base ${base} to base 10 = ${data.converted}</h3>
                    `)
                    $('.to_base_10').show()
                }
            });
        }
    });

    // Addition in number bases
    $("input.add_more_number").on('click', function(event) {
        event.preventDefault()
        var new_fields = `
            <div class="more_inputs">
                <h3>Add Another Number:</h3>
                <div class="form-group">
                    <label>Enter the new number*</label>
                    <input name="nums" id="nums" class="form-control" type="text" required>
                </div>
    
                <div class="form-group">
                    <label>Enter the base of the new number*</label>
                    <input name="bases" id="bases" class="form-control" type="number" required>
                </div>
            </div>
        `
        $(".add_input").append(new_fields)
        $(".add_input").show();
    })

    $('form#add_bases').submit(function(e) {
        e.preventDefault()
        $('.add_bases').empty()
        var num1 = $("input[name='num1']").val()
        var base1 = $("input[name='base1']").val()
        var num2 = $("input[name='num2']").val()
        var base2 = $("input[name='base2']").val()
        var add_base = $("input[name='add_base']").val()
        var nums = $("input[name^='nums']")
        var bases = $("input[name^='bases']")
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        var bases_list = bases.map(function(index, elem) {
            return $(elem).val()
        }).get()
        bases_list = bases_list.map(Number)

        var nums_list = nums.map(function(index, elem) {
            return $(elem).val()
        }).get()
        nums_list = nums_list.map(Number)

        // do: add condition to reject if number is not a - f
        checkValidInput(num1)
        checkValidInput(num2)
            /*
            for (var i = 0; i < bases_list.length; i++) {
                checkValidInput(bases_list[i])
            }

            for (var j = 0; j < nums_list.length; j++) {
                //console.log(nums_list[j])
                //checkValidInput(nums_list[j])
                var inputs = /^[0-9a-fA-F]+$/;
                if (nums_list[j].match(inputs)) {
                    return true
                } else {
                    alert(nums_list[j] + ' contains invalid characters');
                    history.go(0);
                }
            }
            */

        if ((greatestDigit(num1) >= parseInt(base1)) && (greatestDigit(num2) >= parseInt(base2))) {
            alert('The base of the number cannot be less or equal to the largest digit of the number')
        } else if ((parseInt(num1) < 0) && (parseInt(base1) < 0) && (parseInt(num2) < 0) && (parseInt(base2) < 0) && (parseInt(add_base) < 0)) {
            alert('Number cannot be negative')
        } else if ((parseInt(num1) == 0) && (parseInt(base1) == 0) && (parseInt(num2) == 0) && (parseInt(base2) == 0)) {
            alert('Number cannot be Zero')
        } else if (parseInt(add_base) % 1 != 0) {
            alert('The base 10 number must be a whole number')
        } else if (parseInt(add_base) < 2) {
            alert('Base cannot be less than 2')
        } else {
            $.ajax({
                //method: 'POST',
                url: '/mathematics/add_bases_answer/',
                data: {
                    'num1': num1,
                    'base1': base1,
                    'num2': num2,
                    'base2': base2,
                    'add_base': add_base,
                    'nums_list': nums_list,
                    'bases_list': bases_list,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                dataType: 'json',
                success: function(data) {
                    $('.add_bases').append(`
                    <h3>${num1}<sub>${base1}</sub> + ${num2}<sub>${base2}</sub> = ${data.result}<sub>${add_base}</sub></h3>                
                `)
                    $('.add_bases').show()
                }
            });
        }
    });

    // Subtraction in number bases

    $('form#subtract_bases').submit(function(e) {
        e.preventDefault()
        $('.subtract_bases').empty()
        var sub_num1 = $("input[name='sub_num1']").val()
        var sub_base1 = $("input[name='sub_base1']").val()
        var sub_num2 = $("input[name='sub_num2']").val()
        var sub_base2 = $("input[name='sub_base2']").val()
        var subtract_base = $("input[name='subtract_base']").val()
            //var sub_nums = $("input[name^='sub_nums']")
            //var sub_bases = $("input[name^='sub_bases']")
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();

        // do: add condition to reject if number is not a - f
        checkValidInput(sub_num1)
        checkValidInput(sub_num2)
            /*
            for (var i = 0; i < bases_list.length; i++) {
                checkValidInput(bases_list[i])
            }

            for (var j = 0; j < nums_list.length; j++) {
                //console.log(nums_list[j])
                //checkValidInput(nums_list[j])
                var inputs = /^[0-9a-fA-F]+$/;
                if (nums_list[j].match(inputs)) {
                    return true
                } else {
                    alert(nums_list[j] + ' contains invalid characters');
                    history.go(0);
                }
            }
            */
            // convert numbers to base 10
        var x = toBase10(sub_num1, sub_base1)
        var y = toBase10(sub_num2, sub_base2)
        if (x <= y) {
            alert(`
                ${sub_num1} base ${sub_base1} is less than ${sub_num2} base ${sub_base2}. Subtraction Impossible.
            `)
            history.go(0);
        } else if ((greatestDigit(sub_num1) >= parseInt(sub_base1)) && (greatestDigit(sub_num2) >= parseInt(sub_base2))) {
            alert('The base of the number cannot be less or equal to the largest digit of the number')
        } else if ((parseInt(sub_num1) < 0) && (parseInt(sub_base1) < 0) && (parseInt(sub_num2) < 0) && (parseInt(sub_base2) < 0) && (parseInt(subtract_base) < 0)) {
            alert('Number cannot be negative')
        } else if ((parseInt(sub_num1) == 0) && (parseInt(sub_base1) == 0) && (parseInt(sub_num2) == 0) && (parseInt(sub_base2) == 0)) {
            alert('Number cannot be Zero')
        } else if (parseInt(subtract_base) % 1 != 0) {
            alert('The base 10 number must be a whole number')
        } else if (parseInt(subtract_base) < 2) {
            alert('Base cannot be less than 2')
        } else {
            $.ajax({
                //method: 'POST',
                url: '/mathematics/subtract_bases_answer/',
                data: {
                    'sub_num1': sub_num1,
                    'sub_base1': sub_base1,
                    'sub_num2': sub_num2,
                    'sub_base2': sub_base2,
                    'subtract_base': subtract_base,
                    'csrfmiddlewaretoken': csrfmiddlewaretoken
                },
                dataType: 'json',
                success: function(data) {
                    $('.subtract_bases').append(`
                        <h3>${sub_num1}<sub>${sub_base1}</sub> - ${sub_num2}<sub>${sub_base2}</sub> = ${data.result}<sub>${subtract_base}</sub></h3>                
                    `)
                    $('.subtract_bases').show()
                }
            });
        }
    });

    // Subtraction in number bases
    $("input.multiply_more_number").on('click', function(event) {
        event.preventDefault()
        var new_inputs = `
            <div class="more_inputs">
                <h3>Multiply Another Number:</h3>
                <div class="form-group">
                    <label>Enter the new number*</label>
                    <input name="mul_nums" class="form-control" type="text" required>
                </div>
    
                <div class="form-group">
                    <label>Enter the base of the new number*</label>
                    <input name="mul_bases" class="form-control" type="number" required>
                </div>
            </div>
        `
        $(".multiply_input").append(new_inputs)
        $(".multiply_input").show();
    });

    // multiply bases
    $('form#multiply_bases').submit(function(e) {
        e.preventDefault()
        $('.multiply_bases').empty()
        var mul_num1 = $("input[name='mul_num1']").val()
        var mul_base1 = $("input[name='mul_base1']").val()
        var mul_num2 = $("input[name='mul_num2']").val()
        var mul_base2 = $("input[name='mul_base2']").val()
        var multiply_base = $("input[name='multiply_base']").val()
        var mul_nums = $("input[name^='mul_nums']")
        var mul_bases = $("input[name^='mul_bases']")
        var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        var new_list = []; // converted numbers to be multiplied
        var mul_list = 1; // multiplication result of converted numbers
        var mul_bases_list = mul_bases.map(function(index, elem) {
            return $(elem).val()
        }).get()
        mul_bases_list = mul_bases_list.map(Number)

        var mul_nums_list = mul_nums.map(function(index, elem) {
            return $(elem).val()
        }).get()
        mul_nums_list = mul_nums_list.map(Number)

        // do: add condition to reject if number is not a - f
        checkValidInput(mul_num1)
        checkValidInput(mul_num2)
        if (mul_nums_list.length !== 0 && mul_bases_list !== 0) {
            for (var i = 0; i < mul_nums_list.length; i++) {
                console.log(mul_nums_list[i], mul_bases_list[i])
                var m = parseInt(mul_nums_list[i], mul_bases_list[i])
                new_list.push(m)
            }
        } else {
            mul_list = 1;
        }
        console.log(mul_list)
        console.log(new_list)
        if (new_list.length > 0) {
            for (var x = 0; x < new_list.length; x++) {
                while (x < new_list.length) {
                    var y = new_list[x] * new_list[x + 1]
                    mul_list *= y;
                    x += 2;
                }
            }
        } else {
            mul_list = 1;
        }
        console.log(mul_list)
        if ((greatestDigit(mul_num1) >= parseInt(mul_base1)) && (greatestDigit(mul_num2) >= parseInt(mul_base2))) {
            alert('The base of the number cannot be less or equal to the largest digit of the number')
        } else if ((parseInt(mul_num1) < 0) && (parseInt(mul_base1) < 0) && (parseInt(mul_num2) < 0) && (parseInt(mul_base2) < 0) && (parseInt(multiply_base) < 0)) {
            alert('Number cannot be negative')
        } else if ((parseInt(mul_num1) == 0) && (parseInt(mul_base1) == 0) && (parseInt(mul_num2) == 0) && (parseInt(mul_base2) == 0)) {
            alert('Number cannot be Zero')
        } else if (parseInt(multiply_base) % 1 != 0) {
            alert('The base 10 number must be a whole number')
        } else if (parseInt(multiply_base) < 2) {
            alert('Base cannot be less than 2')
        } else {
            // convert all numbers to base 10
            var num_10 = toBase10(mul_num1, mul_base1);
            var num_20 = toBase10(mul_num2, mul_base2);
            // multiply numbers in base 10
            var multiplied = num_10 * num_20 * mul_list;
            // convert back to the needed base
            var result = fromBase10(multiplied, multiply_base);
            $('.multiply_bases').append(`
                <h3>${mul_num1}<sub>${mul_base1}</sub> X ${mul_num2}<sub>${mul_base2}</sub> = ${result}<sub>${multiply_base}</sub></h3>                
            `)
            $('.multiply_bases').show()
        }
    });

    // function to get largest digit in a number
    const greatestDigit = (num = 0, greatest = 0) => {
        if (num) {
            const max = Math.max(num % 10, greatest);
            return greatestDigit(Math.floor(num / 10), max);
        };
        return greatest
    }
    return greatestDigit(num);

    // check if inputs include numbers and letters a to f only
    function checkValidInput(inputTexts) {
        var letters = /^[0-9a-fA-F]+$/;
        if (inputTexts.match(letters)) {
            return true
        } else {
            alert(inputTexts + ' contains invalid characters');
            history.go(0);
        }
    };

    function toBase10(inputs, base) {
        return parseInt(inputs, base);
    }

    function fromBase10(numb, base) {
        return numb.toString(base)
    }
});