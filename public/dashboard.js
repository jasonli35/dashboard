document.addEventListener("DOMContentLoaded", (event)=> {
    headNode = document.querySelector("#head");
    template = document.querySelector("#template");

    //fetch data from server and parse data to webpage
    fetch("/allIdeas")
    .then(respnse => {
        return respnse.json();
    })
    .then((data) => {
        var length = Object.keys(data).length;
        console.log(length);
        for(let i = 0; i < length; i++){
            let newNode = template.cloneNode(true);
            
            newNode.querySelector("#title").innerHTML = data[i]["title"];
            console.log(data[i]["title"]);
            newNode.querySelector("#competitors").innerHTML = data[i]["competitors"];
            newNode.querySelector("#price").innerHTML = data[i]["price"];
            newNode.querySelector("#cost").innerHTML = data[i]["cost"];
            newNode.querySelector("#size").innerHTML = data[i]["market_size"];
            newNode.querySelector("#delete_button").addEventListener('click', () => {
                console.log(`trying to delete ${data[i]["title"]}`);
                fetch(`/deleteidea/${data[i]["title"]}`, {method:'DELETE'})
                .then((response) => response.json())
                .then((data) => console.log(JSON.stringify(data)))
                .catch(error => console.error('Error: ', error));
           
            });
            headNode.appendChild(newNode);
        }
        // console.log(JSON.stringify(data[0]["id"]));
    })
   

    let add_form = document.getElementById('add-form');

    add_form.addEventListener('submit', (event) => {
        // Stop the default form behavior
        event.preventDefault();
   
        // Grab the needed form fields
        const action = add_form.getAttribute('action');
        const method = add_form.getAttribute('method');
        const formData = new FormData(add_form);


    fetch(`/addidea/${formData.get("input_title")}/${formData.get("input_competitor")}/${formData.get("input_price")}/${formData.get("input_cost")}/${formData.get("market_size")}`,{method:'POST'})
    .then(respnse => {
        return respnse.json();
    })
    .then((data) => {
       

        let newNode = template.cloneNode(true);
           
            newNode.querySelector("#title").innerHTML = input_title;
            console.log(data[i]["title"]);
            newNode.querySelector("#competitors").innerHTML = input_competitor;
            newNode.querySelector("#price").innerHTML = input_price;
            newNode.querySelector("#cost").innerHTML = input_cost;
            newNode.querySelector("#size").innerHTML = market_size;
            headNode.appendChild(newNode);
        
        

         console.log("data added sucessfully");
    })
    .catch(error => console.error('Error: ', error));

      });


      //form for editing market size

      let modify_form = document.getElementById('modify-form');

      modify_form.addEventListener('submit', (event) => {
        // Stop the default form behavior
        event.preventDefault();
   
        // Grab the needed form fields
       
        const modifyFormData = new FormData(modify_form);



    fetch(`/modify/${modifyFormData.get("input_title")}/${modifyFormData.get("new_size")}`,{method:'PUT'})
    .then(respnse => {
        return respnse.json();
    })
    // .then((data) => {
        
    //     console.log(data);

    //      console.log("data added sucessfully");
    // })
    .catch(error => console.error('Error: ', error));
        

   
       
       
      });
  


    


});