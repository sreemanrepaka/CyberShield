// var selectedText = '';
// if (window.getSelection) {
//     selectedText = window.getSelection().toString();
// } else if (document.selection && document.selection.type != 'Control') {
//     selectedText = document.selection.createRange().text;
// }
// console.log(selectedText);
document.getElementById("btn").addEventListener("click", function() {
  let tweet=document.getElementById('text').value;
    axios.post('http://127.0.0.1:5000/predict', {
    text: tweet
    
  })
    .then(
        (response)=>{
           document.getElementById('result').innerHTML = response.data;
        }
        )
    .catch(error => console.error(error));

    

});


