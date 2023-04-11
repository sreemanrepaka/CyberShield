
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




document.getElementById("btn2").addEventListener("click", function() {

  let bully=0;
  let non_bully=0;
  let total=0;


axios.get('http://127.0.0.1:5000/predict')
  .then(function (response) {
    if (response.data.length > 0) {
      for (let index = 0; index < response.data.length; index++) {
        total++;
        if (response.data[index]=="not bullying"){
          non_bully++;


        }
        else{
          bully++;
        }
 
      }
      document.getElementById('result').innerHTML =""
      
      document.getElementById('stats-container').style.visibility="visible";
      document.getElementById('total').innerHTML =total;
      document.getElementById('bullying').innerHTML =bully;
      document.getElementById('not-bullying').innerHTML =non_bully;
      alert("Cyberbullying detected in "+bully+" tweet(s). Report the tweets immediately!")

      
    }

   
  })
  .catch(error => console.log(error))


  setTimeout(() => {
    document.getElementById('result').innerHTML = "Scraping tweets...";
  }, 1000);

  setTimeout(() => {
    document.getElementById('result').innerHTML = "Calling API...";
  }, 4000);

  setTimeout(() => {
    document.getElementById('result').innerHTML = "Fetching results...";
  }, 7000);

  
});
