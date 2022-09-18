window.onload = function() {
    const id_input = document.getElementById("idInput-update-form");
    const username_input = document.getElementById("usernameInput-update-form");
    const password_input = document.getElementById("passwordInput-update-form");
    const submit_input = document.getElementById("submitInput-update-form");


    id_input.addEventListener("input", function() {
        if (id_input.value != "") {
            $.ajax({
                url: read_view_url,
                type: "GET",
                dataType: "json",
                data: {"id" : id_input.value},
                success: function(response, textStatus, xhr) {
                    if (xhr.status == 200) {
                        username_input.removeAttribute("disabled");
                        username_input.value = response["username"]
                        password_input.removeAttribute("disabled");
                        submit_input.removeAttribute("disabled");
                    }
                },
                error: function(error) {
                    username_input.value = "";
                    username_input.setAttribute("disabled", true);
                    password_input.value = "";
                    password_input.setAttribute("disabled", true);
                    submit_input.setAttribute("disabled", true);
                }
            });
        }
        else {
            username_input.value = "";
            username_input.setAttribute("disabled", true);
            password_input.value = "";
            password_input.setAttribute("disabled", true);
            submit_input.setAttribute("disabled", true);
        }

    });
}