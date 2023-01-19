var el = x => document.getElementById(x);

// For Image
var dataImage = localStorage.getItem('imgData');
saved_image = el('saved_image');
saved_image.src = "data:image/jpeg;base64," + dataImage;

// let url = "http://localhost:8000/";
url = "/api/predict-breed/";

headers = {
    "Content-Type": "application/json"
}
data = {
    method: "POST",
    headers: headers,
    body: JSON.stringify({
        "image_bytes": dataImage,
        "top_n": 4
    })
}
console.log("Sending request to:", url);
let result_=0;

fetch(url, data).then(response => response.json()).then(data => {
    console.log("data", data);
    result_ = data;
    // el('result_txt').innerHTML = JSON.stringify(data);
    // iterate result_ Object
    let resultText = "";
    for (let key in result_) {
        let chance = (result_[key]*100).toFixed(1);
        if(chance > 5) {
        resultText += `${key}: ${chance} %<br>`;
        }
        if (resultText.length < 1) {
            resultText = "This is no dog😌";
        }
    }
    el('result_txt').innerHTML = resultText;
}
)
