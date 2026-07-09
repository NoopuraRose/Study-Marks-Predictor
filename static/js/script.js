async function predictMarks() {

    let study = document.getElementById("study").value;

    if (study === "") {
        alert("Please enter study hours.");
        return;
    }

    const response = await fetch("/user", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            study: Number(study)
        })

    });

    const data = await response.json();

    document.getElementById("prediction").innerHTML =
        "🎯 " + data.marks + " Marks";

}