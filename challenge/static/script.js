const vue = new Vue({
    el: "#content"
})

document.getElementById("clear-icon").addEventListener("click", async () => {
    await fetch("/api/clear");
    location.reload();
});

const input_form = document.getElementById("input-form");
input_form.addEventListener("submit", async () => {
    event.preventDefault();
    const data = new URLSearchParams(new FormData(input_form))
    await fetch("/api/mark", {
        method: "POST",
        body: data
    });
    location.reload();
});

document.getElementById("submit-icon").addEventListener("click", async () => {
    const response = await fetch("/api/check");
    const response_text = await response.text();
    const submit_message = document.getElementById("submit-message");
    console.log(response_text);
    submit_message.innerText = response_text;
    submit_message.classList.remove("hidden");
    setTimeout(()=>{submit_message.classList.add("hidden")}, 3000);
});