// var selectedText = '';
// if (window.getSelection) {
//     selectedText = window.getSelection().toString();
// } else if (document.selection && document.selection.type != 'Control') {
//     selectedText = document.selection.createRange().text;
// }
// console.log(selectedText);
document.getElementById("btn").addEventListener("click", function() {
  let tweet=document.getElementById('text').value;
  if (tweet.length > 0) {
    axios.post('http://127.0.0.1:5000/predict', {
    text: tweet
    
  })
    .then(
        (response)=>{
          if (response.data!=="not bullying"){
            document.getElementById('result').innerHTML ="Cyberbullying detected! Type of cyberbullying: " + response.data;
            document.getElementById('result').style.backgroundColor="red";
            alert("Cyberbullying detected! Report the tweet immediately!")

          }

          else{
            document.getElementById('result').innerHTML = "No cyberbullying detected!";
            document.getElementById('result').style.backgroundColor="green";
          }
        }

        )
    .catch(error => console.error(error));

    }

    else{
      document.getElementById('result').innerHTML = "No text entered";
    }
    

});



