window.onload = function() {
    const id_input_update = document.getElementById("idInput-update-form");
    const id_input_delete = document.getElementById("idInput-delete-form");
    const username_input = document.getElementById("usernameInput-update-form");
    const password_input = document.getElementById("passwordInput-update-form");
    const submit_input_update = document.getElementById("submitInput-update-form");
    const submit_input_delete = document.getElementById("submitInput-delete-form");

    if (window.location["href"].endsWith("update-form/")) {

        id_input_update.addEventListener("input", function() {
            if (id_input_update.value != "") {
                $.ajax({
                    url: read_view_url,
                    type: "GET",
                    dataType: "json",
                    data: {"id" : id_input_update.value},
                    success: function(response, textStatus, xhr) {
                        if (xhr.status == 200) {
                            username_input.removeAttribute("disabled");
                            username_input.value = response["username"]
                            password_input.removeAttribute("disabled");
                            submit_input_update.removeAttribute("disabled");
                        }
                    },
                    error: function(error) {
                        username_input.value = "";
                        username_input.setAttribute("disabled", true);
                        password_input.value = "";
                        password_input.setAttribute("disabled", true);
                        submit_input_update.setAttribute("disabled", true);
                    }
                });
            }
            else {
                username_input.value = "";
                username_input.setAttribute("disabled", true);
                password_input.value = "";
                password_input.setAttribute("disabled", true);
                submit_input_update.setAttribute("disabled", true);
            }
    
        });
        
    }
    

    if (window.location["href"].endsWith("delete-form/")) {

    id_input_delete.addEventListener("input", function() {
        if (id_input_delete.value != "") {
            submit_input_delete.removeAttribute("disabled");
        }
        else {
            submit_input_delete.setAttribute("disabled", true);
        }
    });

    }
}