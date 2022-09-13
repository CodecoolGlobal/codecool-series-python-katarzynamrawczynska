function buildResult(data){
    let myList = document.getElementById('my-list')
    myList.innerHTML = '';
    for (const person of data){
        myList.innerHTML += `
            <li>${person.name}</li>
        `
    }
}

function getActorInfo(){
    const characterDetails = document.getElementByClassName("characterDetails");
    for (let i = 0; i< characterDetails.length; i++){
        characterDetails[i].addEventListener('click', ()=> {
        return fetch(`http://127.0.0.1:5000/actor/`+ characterDetails[i].actor_id)
            .then((res) => res.json())
            .then((data) => {
                buildResult(data);
            })
    })
}

}
